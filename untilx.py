if __name__ == "__main__":
    sum = 0
    while True:
        l = input("Enter: ")
        if(l == 'x'):
            break
        sum = sum + int(l)

    print("Sum is "+ str(sum))