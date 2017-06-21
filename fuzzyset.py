#Simple fuzzyset implementation
#Author: Lucas V. Oliveira

class FuzzySet(dict):
    def __init__(self, iterable=[]):
        for item in iterable:
            this = self
            this[item] = 1
    
    def __setitem__(self, key, value):
        assert value >= 0 and value <= 1
        return super(FuzzySet, self).__setitem__(key, value)
        
    def union(self, targetset):
        assert isinstance(targetset, FuzzySet)
        newset = FuzzySet()
        elements_set = set(list(self.keys()) + list(targetset.keys()))
        for elem in elements_set:
            newset[elem] = max(self.get(elem, 0), targetset.get(elem, 0))
        return newset
    
    def intersection(self, targetset):
        assert isinstance(targetset, FuzzySet)
        newset = FuzzySet()
        elements_set = set(list(self.keys()) + list(targetset.keys()))
        for elem in elements_set:
            newset[elem] = min(self.get(elem, 1), targetset.get(elem, 1))
        return newset