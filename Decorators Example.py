def logger(func):
    def wrapper(*args):
        print("Executing...")
        return func(*args)
    return wrapper
@logger
def say_hello():print("Hello!")
say_hello()

