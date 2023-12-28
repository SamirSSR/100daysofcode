def hcf(a, b):
    if(a<b):
        c = a
        while(c>=1):
            if(a%c==0 and b%c==0):
                return c
            c=c-1
    else:
        c = b
        while(c>=1):
            if(a%c==0 and b%c==0):
                return c
            c=c-1

def lcm(a,b):
    if(a<b):
        c = b
        while(c<=(a*b)):
            if(c%a==0 and c%b==0):
                return c
            c= c+1
    else:
        c = a
        while(c<=(a*b)):
            if(c%a==0 and c%b==0):
                return c
            c=c+1

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print("HCF = " + str(hcf(a,b)))
    print("LCM = " + str(lcm(a,b)))