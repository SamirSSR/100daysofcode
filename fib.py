def fib(n):
    sum = 0
    count = 1
    a = 0
    b = 1
    while(count <= n):
        print(a)
        sum = a+b
        a = b
        b = sum
        count = count + 1

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    fib(n)