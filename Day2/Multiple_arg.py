
def Arg_fxn(*arg):
    for i in arg:
        print(i)

def Arg_fxn1(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


Arg_fxn('Hello', 30.5, 5, 'Saurabh')
Arg_fxn1("saurabh", college='NIT Srinagar', degree='BTech Final Yr', branch='IT')

