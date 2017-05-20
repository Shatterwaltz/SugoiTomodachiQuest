'''
A simple mixin that can be extended by a class to allow it's properties 
to be iterable.
'''

class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value
