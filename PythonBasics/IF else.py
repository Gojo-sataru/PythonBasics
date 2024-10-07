# a=int(input("Enter a number="))
# if(a%3==0 or a%5==0) :
#      print ("the given number is divisible by 3 and 5")
# else:
#      print("the given number is  not divisible by 3 and 5")
#
# # #Example 3
# c=int(input("enter a number"))
# if (c%2==0):
#     print("even")
# else:
#     print("odd")

#example 4

# score=int(input("enter a number="))
# if (score<35):
#     print("poor student")
# elif (score>35 and score<70):
#     print("avg student")
# elif (score>70 and score<=100):
#     print("good student")
# else :
#     print("invalid")
#
# mini Calculator

a=int (input("enter a number="))

b=int (input("enter a number="))

opr=input("add/sub/mul/div:")

if (opr=="add"):
    print(a+b)
elif (opr=="sub"):
    print(a-b)
elif (opr=="mul"):
    print(a*b)
elif (opr=="div"):
    print(a/b)
else:
    print("invalid")

#example 6
#
# scr=int(input("enter your score="))
# if (scr>=70):
#     name=input("enter your name")
#     age=int(input("enter your age"))
#     print("your are eligible")
# else:
#     print("your not eligible")