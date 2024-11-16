import os
import stat
import errno
import fuse
from fuse import Fuse

fuse.fuse_python_api = (0, 2)

class MemoryFS(Fuse):
    def __init__(self, *args, **kwargs):
        self.root = {}
        super(MemoryFS, self).__init__(*args, **kwargs)

    def getattr(self, path, fh=None):
        node = self._find_node(path)
        if node is None:
            return -errno.ENOENT
        st = os.stat_result((
            stat.S_IFREG | 0o644,  # Тип файла (обычный файл) и права доступа
            0,  # inode
            0,  # device
            1,  # number of hard links
            0,  # user id
            0,  # group id
            len(node['content']) if 'content' in node else 0,  # size
            0,  # atime
            0,  # mtime
            0,  # ctime
        ))
        return st

    def readdir(self, path, fh):
        node = self._find_node(path)
        if node is None:
            return -errno.ENOENT
        entries = ['.', '..']
        if isinstance(node, dict):
            entries += node.keys()
        for r in entries:
            yield fuse.Direntry(r)

    def mkdir(self, path, mode):
        parent, name = self._split_path(path)
        if parent not in self.root:
            return -errno.ENOENT
        self.root[parent][name] = {}
        return 0

    def rmdir(self, path):
        parent, name = self._split_path(path)
        if parent not in self.root or name not in self.root[parent]:
            return -errno.ENOENT
        if self.root[parent][name]:
            return -errno.ENOTEMPTY
        del self.root[parent][name]
        return 0

    def unlink(self, path):
        parent, name = self._split_path(path)
        if parent not in self.root or name not in self.root[parent]:
            return -errno.ENOENT
        del self.root[parent][name]
        return 0

    def open(self, path, flags):
        node = self._find_node(path)
        if node is None:
            return -errno.ENOENT
        return 0

    def read(self, path, size, offset, fh):
        node = self._find_node(path)
        if node is None:
            return -errno.ENOENT
        return node['content'][offset:offset + size]

    def write(self, path, buf, offset, fh):
        node = self._find_node(path)
        if node is None:
            return -errno.ENOENT
        if 'content' not in node:
            node['content'] = bytearray()
        if offset > len(node['content']):
            node['content'].extend(b'\0' * (offset - len(node['content'])))
        node['content'][offset:offset + len(buf)] = buf
        return len(buf)

    def _find_node(self, path):
        parts = path.strip('/').split('/')
        node = self.root
        for part in parts:
            if part not in node:
                return None
            node = node[part]
        return node

    def _split_path(self, path):
        path = path.strip('/')
        if '/' in path:
            parent, name = path.rsplit('/', 1)
        else:
            parent, name = '', path
        return parent, name

if __name__ == '__main__':
    operations = MemoryFS()
    fuse = Fuse(operations, '/mnt/fuse_mount', usage="usage")