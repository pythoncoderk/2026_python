def obj():
    print("オブジェクト")

def free(word):
    return word

def py(func):
    def wrapper(*args, **kwargs):
        print("Pythonは" + func(*args, **kwargs))
    return wrapper

pyobj = py(obj)
pyfree = py(free)
print(pyobj)
print(pyfree("楽しい"))