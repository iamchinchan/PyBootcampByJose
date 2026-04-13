import one
print("outer in two file")


def two_func():
    print("i am inside two func")


one.one_func()
if __name__ == "__main__":
    print(f"two.py runned directly because __name__= {__name__}")
else:
    print(f"two.py imported, and __name__ = {__name__}")
