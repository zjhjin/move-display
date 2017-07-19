"""test"""


def inside():
    a = 'cool'

    def init():
        print(a)
    return init


def decor(func):
    a = 'cool'
    def wrapper(*args, **kwargs):
        return func(a, *args, **kwargs)
    return wrapper


@decor
def beinside(a):
    print(a)


if __name__ == '__main__':
    # init = inside()
    # init()
    beinside()

