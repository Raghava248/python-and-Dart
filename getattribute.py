#__getattribute__

class Dummy(object):
    def __getattribute__(self, attr):
        __dict__ = super(Dummy, self).__getattribute__('__dict__')
        if attr in __dict__:
            return super(Dummy, self).__getattribute__(attr)
        return attr.upper()
d = Dummy()
d.value = "Python"
print(d.value)  # "Python"
print(d.does_not_exist)  # "DOES_NOT_EXIST"
