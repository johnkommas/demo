print(list(map(lambda a: a * 2, [1, 2, 3])))


def decorator(function):
    def wrap():
        print('Hello')
        function()
    return wrap


@decorator
def first():
    print("Komma")


first()
