def boyHeight(f:int,m:int):
    boyH = (f+m)*1.08/2
    print(boyH)

def girlHeight(f:int,m:int):
    girlH = (f*0.923+m)/2
    print(girlH)

print("boy or girl?")
sex = input()
f=int(input("父亲身高："))
m=int(input("母亲身高："))

if(sex in 'boy' ):
    boyHeight(f,m)
elif(sex in 'girl'):
    girlHeight(f,m)
else:
    print("error")
