def tup(*args):
    sum = 0
    for a in args:
        sum = sum + a
    print(sum)

    

tup(1,2,)

#Named arg,  making to accept unlimited args
def welcome(**kwargs):
    print(kwargs)

welcome(name="Shisir", anotherName="Jagdish")