if __name__ == "__main__":
    num = input("Enter the integer: ")
    product = 1
    sum = 0
    for i in num:
        product =  product * int(i)
        sum = sum + int(i)
    print("Difference = " + str(product-sum))