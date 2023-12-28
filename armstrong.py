if __name__ == "__main__":
    num = input("Enter a number: ")
    restriction = int(num)
    sum = 0
    power = 1
    while True:
        for i in num:
            sum = sum + pow(int(i),power)
        if(sum == restriction):
            print("It is an Armstrong number.")   
            break 
        elif(sum > restriction):
            print("It is not an Armstrong number for power " + str(power))
            break
        sum = 0
        power = power + 1