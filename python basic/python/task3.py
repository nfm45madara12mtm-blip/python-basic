# get user's exam marks
# if the mark is greater than 100 and less than 0, print a statment
# if the mark is greater than 90 and less then 100, print a statment("Excekllent")
# if the mark is greater than 80 and less than 90 , print a statement
# if the mark is greater than 70 and less than 80 , print a statement
# if the mark is greater than 60 and less than 70 , print a statement
# if the mark is greater than 50 and less than 60 , print a statement
# if the mark is greater than 40 and less than 50 , print a statement
# if the mark is less than 40, print a statment


marks=float(input("enter marks:"))
if marks>=100 and marks<=0:
    print("pass")
elif marks>=90 and marks<=100:
    print("excellent")
elif marks>=80 and marks<=90:
    print("very good")
elif marks>=70 and marks<=80:
    print("good")
elif marks>=60 and marks<=70:
    print("Average")
elif marks>=50 and marks<60:
    print("below average")
elif marks<=40:
    print("meh")