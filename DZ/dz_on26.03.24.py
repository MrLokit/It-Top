def arif(x):
    def wrap(*args):
        return x(*args)/len(args)
    return wrap
@arif
def summ(*args):
    return sum(args)

print(summ(2,3,3,4))