import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("This is an error!")
except ValueError:
    print("Caught a ValueError!")
except TypeError:
    print("Caught a TypeError!")
except Exception as ex:
    print("exception is {}:".format(ex.__class__.__name__))
else:
    print("This code is no exception!")
finally:
    print("This cleanup code is always called!")
