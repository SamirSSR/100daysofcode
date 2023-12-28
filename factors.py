if __name__ == "__main__":
    n = int(input("Enter the number: "))
    count = 1
    while(count <= n):
        if(n%count==0):
            print(count)
        count = count + 1