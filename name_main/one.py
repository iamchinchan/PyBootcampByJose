print("outer in one file")


def one_func():
    print("i am inside one func")


if __name__ == "__main__":
    print("one.py runned directly")
else:
    print(f"one.py imported, and __name__ = {__name__}")
