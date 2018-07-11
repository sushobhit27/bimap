from multiindex import MultiIndexContainer, HashedUnique, HashedNonUnique


class BiMapValue(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class View(object):
    def __init__(self, bm, view_type):
        self.bm = bm
        self.view_type = view_type

    def __setitem__(self, key, value):
        self.bm.insert(key, value, self.view_type)

    def __getitem__(self, item):
        return self.bm.get(item, self.view_type)
    
    def keys(self):
        return self.bm.keys(self.view_type)

    def values(self):
        return self.bm.values(self.view_type)


class bimap(object):
    def __init__(self):
        self.multi_index = MultiIndexContainer(HashedUnique('left'),
                                               HashedUnique('right'))

        self._left = View(self, 'left')
        self._right = View(self, 'right')

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def insert(self, key, value, view_type):
        if view_type == 'left':
            self.multi_index.modify('right', value, BiMapValue(key, value)) if self.multi_index.get('left', key) else self.multi_index.insert(BiMapValue(key, value))
#            self.multi_index.insert(BiMapValue(key, value), overwrite=True)
        else:
            self.multi_index.modify('right', key, BiMapValue(value, key)) if self.multi_index.get('right', value) else self.multi_index.insert(BiMapValue(value, key))
#            self.multi_index.insert(BiMapValue(value, key), overwrite=True)

    def get(self, item, view_type):
        if view_type == 'left':
            return getattr(self.multi_index.get('left', item), 'right')
        else:
            return getattr(self.multi_index.get('right', item), 'left')

    def keys(self, view_type):
        for index in self.multi_index.get_index(view_type):
            yield index[0]
    
    def values(self, view_type):
        if view_type == 'left':
            for index in self.multi_index.get_index('right'):
                yield index[0]
        else:
            for index in self.multi_index.get_index('left'):
                yield index[0]

 
class multi_bimap(object):
    def __init__(self):
        self.multi_index = MultiIndexContainer(HashedNonUnique('left'),
                                               HashedNonUnique('right'))

        self._left = View(self, 'left')
        self._right = View(self, 'right')

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def insert(self, key, value, view_type):
        if view_type == 'left':
            self.multi_index.insert(BiMapValue(key, value))
        else:
            self.multi_index.insert(BiMapValue(value, key))

    def get(self, item, view_type):
        if view_type == 'left':
            return [getattr(mi_ctr, 'right') for mi_ctr in self.multi_index.get('left', item)]
        else:
            return [getattr(mi_ctr, 'left') for mi_ctr in self.multi_index.get('right', item)]

    def keys(self, view_type):
        for index in self.multi_index.get_index(view_type):
            yield index[0]
    
    def values(self, view_type):
        if view_type == 'left':
            for index in self.multi_index.get_index('right'):
                yield index[0]
        else:
            for index in self.multi_index.get_index('left'):
                yield index[0]

       
bm = bimap()
bm.left[1] = 'a'
bm.left[2] = 'b'
bm.left[3] = 'c'
print(bm.left[2])
print(bm.right['c'])
import pdb;pdb.set_trace()
bm.left[2] = 'xyz'
bm.right['d'] = 4
print(bm.left[2])
print(bm.left[4])
print(list(bm.left.keys()))
print(list(bm.right.keys()))
print('**************')
print(list(bm.left.values()))
print(list(bm.right.values()))

print('=================')
bm = multi_bimap()
bm.left[1] = 'a'
bm.left[2] = 'b'
bm.left[3] = 'c'
print(bm.left[2])
print(bm.right['c'])

bm.left[2] = 'xyz'
bm.right['d'] = 4
print(bm.left[2])
print(bm.left[4])
print(list(bm.left.keys()))
print(list(bm.right.keys()))
print('**************')
print(list(bm.left.values()))
print(list(bm.right.values()))
