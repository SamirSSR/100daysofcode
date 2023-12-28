if __name__ == "__main__":
    num = input("Enter the number: ")
    l = len(num)
    count = 0
    flag = True
    while(count<(l/2)):
        if(num[count]!=num[l-1-count]):
            flag = False
            print("Not a pallindrome")
            break
        count = count + 1
    if(flag):
        print(str(num) + " is a pallindrome")