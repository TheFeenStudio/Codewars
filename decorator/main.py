def decorator(func):
    def wrapper():
        print('hello my dear world')
        type(func())
    return wrapper()


@decorator
def hello():
    print('hello world')
    