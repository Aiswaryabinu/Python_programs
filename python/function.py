#sum of two numbers using fn
#without arguments
a =8
b= 9
def sum1():
    c = a + b
    print(c)
sum1()    


#with arguments
def sum2(a,b):
    c= a + b
    print(c)
sum2(8,7)

#return type
def sum3(a,b):
    c = a+b
    return c
result=sum3(6,7)
print(result)