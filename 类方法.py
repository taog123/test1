class BaseA(object):

    @classmethod
    def func_a(cls):# 直接使用类名，而不使用cls
        print(BaseA)
        print(type(cls), cls)


class BaseB(object):
    pass


class ClassA(BaseA, BaseB):
    pass


if __name__ == '__main__':

    ClassA.func_a()