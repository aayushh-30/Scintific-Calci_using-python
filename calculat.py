#CALCULATOR
def add(a,b):
    print("SUM IS",a+b)
def sqrt(a,b):
    print("{} RAISED TO POWER {} IS".format(a,b),a**b)
def sub(a,b):
    print("DIFFERENCE IS ",a-b)
def prd(a,b):
    print("PRODUCT IS",a*b)
def div(a,b):
    print("QUOTIENT IS",a//b)
def rem(a,b):
    print("REMAINDER",a%b) 
while True:
    print("'+' for addition","'-' for subtraction","'*' for multiply","'//' for division",'"**" for exponential','"%" for remainder','"sin" for sine of an angle in degree','"cos" for cosine of a angle in degree','"tan" for tangent of a angle in degree',"'tanh' for tangent-hyperbola","'sinh' for sine-hyperbola","'cosh' for cosine-hyperbola","'deg' to convert angle from radian to degree","'rad' to convert degree to radian","'.' for exit",sep=" || ")
    fun=input("ENTER OPERATION : ")
    if fun=="+":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        add(a,b)
    elif fun=="-":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        sub(a,b)
    elif fun=="*":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        prd(a,b)
    elif fun=="//":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        div(a,b)
    elif fun=="%":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        rem(a,b)
    elif fun=="**":
        a=eval(input("ENTER FIRST NUMBER : "))
        b=eval(input("ENTER SECOND NUMBER : "))
        sqrt(a,b)
    elif fun=="sin":
        import math
        num1=eval(input("ENTER VALUE : "))
        num=math.radians(num1)
        print("sin",num1,"is %.2f"%math.sin(num))
    elif fun=="cos":
        import math
        num1=eval(input('ENTER VALUE : '))
        num=math.radians(num1)
        print("cos",num1,"is %.2f"%math.cos(num))
    elif fun=="tan":
        import math
        num1=eval(input("ENTER VALUE : "))
        num=math.radians(num1)
        print("tan",num1,"is %.2f"%math.tan(num))
    elif fun=="tanh":
        import math
        num1=eval(input("ENTER VALUE : "))
        num=math.radians(num1)
        print("tanh",num1,"is %.2f"%math.tanh(num))
    elif fun=="sinh":
        import math
        num1=eval(input("ENTER VALUE : "))
        num=math.radians(num1)
        print("sinh",num1," is %.2f"%math.sinh(num))
    elif fun=="cosh":
        import math
        num1=eval(input("ENTER VALUE : "))
        num=math.radians(num1)
        print("cosh",num1,"is %.2f"%math.cosh(num))
    elif fun=="log":
        import math
        num=eval(input("ENTER NUMBER : "))
        base=eval(input("ENTER BASE"))
        print("Log of {} to base {} is".format(num,base),math.log(num,base))
    elif fun=="rad":
        import math
        num=eval(input("ENTER ANGLE IN DEGREE : "))
        ang=math.radians(num)
        print("ANGLE IN RADIANS :",ang)
    elif fun=="deg":
        import math
        num=eval(input("ENTER ANGLE IN RADIAN : "))
        ang=math.degrees(num)
        print("ANGLE IN DEGREES :",ang)
    elif fun==".":
        print("THANK YOU")
        break
            
else:
    print("INVALID INPUT")





