username = "rishabkumar03"

def fun():
    # username = "raz"
    print(username)

print(username)
fun()

x = 96

# def fun2(y):
#     z = x + y
#     return z

# result = fun2(3)
# print (result)

# def fun3():
#     global x
#     x = 9

# fun3()
# print(x)

def f1():
    x = 10
    def f2():
        print(x)
    return f2
my_res = f1()
my_res() 

def me(r):
    def actual(x):
        return x ** r
    return actual

i = me(2)
s = me(4)

print(i(6))
print(s(6))