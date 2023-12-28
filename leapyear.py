year = int(input("Entr a year: "))
if(year%4==0):
    print("Leapyear!")
else:
    if(year%400==0):
        print("Leapyear!")
    else:
        print("Not a leapyear!")