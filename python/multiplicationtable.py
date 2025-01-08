#create  a multiplication table
a = int(input("ENTER THE NUMBER  :"))
b = int(input("upto which table :"))
for x in range(1,b+1) :
    c = a*x
    print(str(a)+"*"+str(x)+"="+str(c))