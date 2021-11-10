#2 Leap year
x=int(input("Enter current year="))
y=int(input("Enter future year="))

while (x<=y):
    if x%100==0 and x%400==0:
        print(x)
    elif x%4==0:
        print(x)
    x+=1
