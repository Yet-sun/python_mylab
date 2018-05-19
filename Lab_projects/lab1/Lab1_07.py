def calculate(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "方程根为全体实数"
            else:
                return "无根"
        else:
            return "该方程为一元一次方程"
    else:
        if b**2-4*a*c==0:
            x1=x2=-b
            print("x1="+str(x1),", x2="+str(x2))
        elif b**2-4*a*c>0:
             x1=-b+(b**2-4*a*c)**0.5/(2*a)
             x2=-b-(b**2-4*a*c)**0.5/(2*a)
             print("x1="+str(x1),", x2="+str(x2))
        elif b**2-4*a*c<0:
            print("无实根")

print(calculate(int(input()),int(input()),int(input())))
