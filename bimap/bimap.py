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
            self.multi_index.replace('left', key, BiMapValue(key, value)) if self.multi_index.get('left', key) else self.multi_index.insert(BiMapValue(key, value))
            #self.multi_index.modify('left', key, BiMapValue(key, value)) if self.multi_index.get('left', key) else self.multi_index.insert(BiMapValue(key, value))
            #self.multi_index.insert(BiMapValue(key, value), overwrite=True) if self.multi_index.get('left', key) else self.multi_index.insert(BiMapValue(key, value))
        else:
            self.multi_index.replace('right', key, BiMapValue(value, key)) if self.multi_index.get('right', key) else self.multi_index.insert(BiMapValue(value, key))
            #self.multi_index.modify('right', key, BiMapValue(value, key)) if self.multi_index.get('right', key) else self.multi_index.insert(BiMapValue(value, key))
            #self.multi_index.insert(BiMapValue(value, key), overwrite=True) if self.multi_index.get('right', key) else self.multi_index.insert(BiMapValue(value, key))
            

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

       
