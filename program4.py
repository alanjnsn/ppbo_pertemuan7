def say_hi(cls):
    def hi(self):
        print('hai')
    cls.hi= hi
    return cls

@say_hi
class Sapa:
    pass
print()
menyapa= Sapa()
menyapa.hi()
print()
print()