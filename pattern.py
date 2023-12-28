def rectangle(h,b):
    count = 1
    while(count <= h):
        print("*"*b)
        count = count + 1

def righttriangle(h):
    count = 1
    while(count <= h):
        print("*"*count)
        count = count + 1

def reverserighttringle(h):
    while(h>=1):
        print("*"*h)
        h = h-1

def numbered_righttriangle(h):
    count = 1
    arr = []
    while(count<=h):
        arr.append(count)
        for i in arr:
            print(i, end=" ")
        print("")
        count = count+1 

def rotated_triangle(h):
    count = 1
    flag = True
    while (count <=h and count>=1):
        print("*"*count)
        if(count == h):
            flag = False
        if(flag):
            count = count + 1
        else: 
            count = count - 1
def rectangle_withspacing(h,b):
    count = 1
    while(count<=h):
        num_space = b-count
        num_star = count
        print(" "*num_space + "*"*num_star)
        count = count + 1
        
def reverse_reactanglewithspacing(h):
    tem = 0
    while(h>=1):
        print(" "*tem+ "*"*h)
        tem = tem+1
        h = h-1

def pyramid(h,b):
    count = 1
    while(count<=h):
        num_space = b-count
        num_star = count-1
        print(" "*num_space+"*"*num_star+"*"+ "*"*num_star+" "*num_space)
        count = count + 1

def reverse_pyramid(h,b):
    tem = 0
    while(h>=1):
        print(" "*tem+"*"*(b-1)+"*"+"*"*(b-1)+" "*tem)
        b= b-1
        tem = tem + 1
        h = h-1
def spaced_triange(h):
    tem = 1
    while(h>=1):
        print(" "*(h-1)+"* "*tem)
        h=h-1
        tem = tem + 1

def reverse_spaced_triangle(h):
    tem = 0
    while(h>=1):
        print(" "*tem+"* "*h)
        h=h-1
        tem=tem+1

def mirrortriangle(h):
    limit = h
    tem = 0
    flag = True
    while(h>=1 and h<=limit):
        if(flag):
            print(" "*tem+"* "*h)
            h=h-1
            tem=tem+1
        else:
            print(" "*tem+"* "*h)
            h=h+1
            tem=tem-1
        if(h==1):
            flag = False    

def hollow_triangle(h):
    count = 1
    while(count<=h):
        num_space = h-count
        num_star = count
        if(count == h):
            print("*"*(2*h-1))
        elif(count == 1):
            print(" "*num_space+"*")
        else:
            print(" "*num_space+"*"+" "*(2*count-3)+"*")
        count = count+1

def hollow_triangle_reverse(h):
    print("*"*(2*h-1))
    tem = h
    while(h>=1):
        if(h>2):
            print(" "*(tem-(h-1))+"*"+" "*(2*h-5)+"*")
        else:
            print(" "*(tem-1)+ "*")
            break
        h = h-1

def hollw_diamond(h):
    count = 1
    flag = True
    while(count<=h and count>=1):
        num_space = h-count
        num_star = count
        if(count == h):
            flag = False
        if(count == 1):
            print(" "*num_space+"*")
        else:
            print(" "*num_space+"*"+" "*(2*count-3)+"*")
        if(flag):
            count= count + 1
        else:
            count = count - 1

if __name__ == "__main__":
    
    # hollw_diamond(5)
    # hollow_triangle_reverse(5)
    # hollow_triangle(5)
    # rectangle_withspacing(5,5)
    # reverse_reactanglewithspacing(5);
    # rotated_triangle(5)
    # rectangle(5, 5)
    # reverserighttringle(5)
    # reverse_pyramid(5,5)
    # reverse_spaced_triangle(5)
    # mirrortriangle(10)

