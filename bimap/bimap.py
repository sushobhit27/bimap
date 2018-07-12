from multiindex import MultiIndexContainer, HashedUnique, HashedNonUnique


class ViewEnum(object):
    LEFT_VIEW = 'left' 
    RIGHT_VIEW = 'right' 


VIEW_MAPPING = {
        ViewEnum.LEFT_VIEW: ViewEnum.RIGHT_VIEW,
        ViewEnum.RIGHT_VIEW: ViewEnum.LEFT_VIEW,
}


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
        self.multi_index = MultiIndexContainer(HashedUnique(ViewEnum.LEFT_VIEW),
                                               HashedUnique(ViewEnum.RIGHT_VIEW))

        self._left = View(self, ViewEnum.LEFT_VIEW)
        self._right = View(self, ViewEnum.RIGHT_VIEW)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def insert(self, key, value, view_type):
        if view_type == ViewEnum.LEFT_VIEW:
            self.multi_index.replace(ViewEnum.LEFT_VIEW, key, BiMapValue(key, value)) if self.multi_index.get(ViewEnum.LEFT_VIEW, key) else self.multi_index.insert(BiMapValue(key, value))
        else:
            self.multi_index.replace(ViewEnum.RIGHT_VIEW, key, BiMapValue(value, key)) if self.multi_index.get(ViewEnum.RIGHT_VIEW, key) else self.multi_index.insert(BiMapValue(value, key))

    def get(self, item, view_type):
        if view_type == ViewEnum.LEFT_VIEW:
            return getattr(self.multi_index.get(ViewEnum.LEFT_VIEW, item), ViewEnum.RIGHT_VIEW)
        else:
            return getattr(self.multi_index.get(ViewEnum.RIGHT_VIEW, item), ViewEnum.LEFT_VIEW)

    def keys(self, view_type):
        for index in self.multi_index.get_index(view_type):
            yield index[0]
    
    def values(self, view_type):
        if view_type == ViewEnum.LEFT_VIEW:
            for index in self.multi_index.get_index(ViewEnum.RIGHT_VIEW):
                yield index[0]
        else:
            for index in self.multi_index.get_index(ViewEnum.LEFT_VIEW):
                yield index[0]

 
class multi_bimap(object):
    def __init__(self):
        self.multi_index = MultiIndexContainer(HashedNonUnique(ViewEnum.LEFT_VIEW),
                                               HashedNonUnique(ViewEnum.RIGHT_VIEW))

        self._left = View(self, ViewEnum.LEFT_VIEW)
        self._right = View(self, ViewEnum.RIGHT_VIEW)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def insert(self, key, value, view_type):
        if view_type == ViewEnum.LEFT_VIEW:
            self.multi_index.insert(BiMapValue(key, value))
        else:
            self.multi_index.insert(BiMapValue(value, key))

    def get(self, item, view_type):
        return [getattr(mi_ctr, VIEW_MAPPING[view_type]) for mi_ctr in self.multi_index.get(view_type, item)]

    def keys(self, view_type):
        for index in self.multi_index.get_index(view_type):
            yield index[0]
    
    def values(self, view_type):
        for index in self.multi_index.get_index(VIEW_MAPPING[view_type]):
            yield index[0]

