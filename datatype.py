# userscore = input("give a value: ")
# print(userscore)
# print(type(userscore))
# a= int(userscore)
# print(a)
# print(type(a))
# b=a*(2)
# print(b)



# tea_cup = int(input("kiti cup? \n"))
# cost = int (input("cost?: \n"))
# total = int(tea_cup*cost)
# print("total value",total)
# if total > 300:
#         a= total-((total*0.10))
#         print(a)




# age=int(input("what is your age?:\n"))
# if age<13:
#     print("BACCHA")
# # print("ghada")

# elif age<20:
#     print("teen")

# elif age<60:
#     print("adult")

# else:
#     print("buddhe")
# print("hmmmm")


# print("hi")
# age=int(input("what is your age? :\n"))
# day=input("what is the day today?\n").lower()

# if age<18:
#     price=int(8)
# else:
#     price=int(12)

# if day == "Wednesday":
#     price-=2
# else:
#     price

# print("Ticket price for you is $",price)



# grade=int(input("what is your grade:\n"))
# if grade>101:
#     print("na mat bana")
#     exit()

# if grade>=90:
#     print("A : YOU ARE A SMARTYYYYYYY")

# elif grade>=80:
#     print("B")

# elif grade>=70:
#     print("C")

# elif grade>=60:
#     print("D")

# else:
#     print("you are a dumbass")


# colour=input("what is the colour of your banana? \n")

# if colour=="green":
#     ripeness="unripe"
#     # print(ripeness)

# elif colour=="yellow":
#     ripeness="ripe" 
#     # print(ripeness)

# elif colour=="brown":
#     ripeness="overripe"
#     # print(ripeness)

# else:
#     ripeness="NA"

# print(ripeness)



# colour=input("what is the colour of your banana? \n")

# if colour=="green":
#    print("unripe")

# elif colour=="yellow":
#     print("ripe")
  

# elif colour=="brown":
#     print("overripe")

# else:
#     print("na")




# weather=input("what is the weather? \n").lower()

# if weather=="sunny":
#     activity="walk"
# elif weather=="rainy":
#     activity="chai"
# elif weather=="windy":
#     activity="read"
# elif weather=="snow":
#     activity="snowman"

# print(activity)


# dist=int(input("distance:\n"))

# if dist<3:
#     transport="walk"
# elif dist<15:
#     transport="bike"
# else:
#     transport="car"

# print ("mode of transport:", transport)




# size=input("size???")
# extra_shot=input("extra shot?????").lower()

# if extra_shot=="yes":
#     order = size + " coffee with extra coffee"

# else:
#     order= size +" coffee"

# print("order:",order)



# password=input("enter password : \n")

# if len(password)<6:
#     print("WEAK")
# elif len(password)<=10:
#     print("MEDIUM")
# else:
#     print("STRONG")




# year=int(input("Year:\n"))

# if (year %  400==0) or (year % 4== 0 and year % 100 != 0):
#     print(year,"is a LEAP YEAR")

# else:
#     print(year,"is a NOT A LEAP YEAR")



# a = input("do you have a pet???").lower()
# if a== "no" :
#     exit()
# else:
#     pet=input("what is your pet:\n").lower()
#     if (pet == "cat")or (pet=="dog"):
#          age=int(input("what is your pet's age:\n"))
#          if pet=="dog":
#             if age<3:
#                 food="puppy food"
#             else:
#                 food="dog food"
#          else:
#             if age>4:
#                 food="senior cat food"
#             else:
#                 food="kitten food"
#     else:
#         print("no data avaliable")
#         exit()

# print(food)





# nos=(input("please give list of numbers \n"))
# numbers=(nos.split())
# converted = [int(s) for s in numbers]
# positive_number_count=0
# for n in converted:
#     if n > 0:
#         print(n)
#         positive_number_count +=1

# print("total positive number count is: ",positive_number_count)





# numbers=[0,1,-2,3,-4,5,-6,7,-8,9,10]
# print(type(numbers))
# positive_number_count=0
# for n in numbers:
#     if n>0:
#         print(n)
#         positive_number_count+=1

# print("total positive number count is: ",positive_number_count)


# day=["monday","tuesday","wednesday","thu","fri","sat","sun"]
# meal=["breakfast","lunch","dinner"]


# for a in day:
#     print("today is",a) 
#     for b in meal:
#         if b=="dinner":
#             break
#         print ("i had ", b)
#         print ("")




# n=int(input("give a number:"))
# sum_even=0

# for i in range(1, n+1):
#     if i%2==0:
#         sum_even+=1
# print("sum of even no is:",sum_even)



# given_number=2
# for i in range(1,11):
#     if i==5:
#         continue
#     print(given_number, "x", i, "=", (given_number*i))
    

# i=(input("give your numbers:\n"))
# j=(i.split())
# k=[int(s) for s in j]

#hardcode
# k=[3,204,6,55,109,10,21,5]

# for n in k:
#     if (n<1)or(n>100):
#         continue    
#     else: 
#         if n%2!=0:
#             print(n,":Weird")
#         elif (n%2==0)and(range(2,6)):
#             print(n,":Not Weird")
#         elif (n%2==0)and(range(6,21)):
#             print(n,":Weird")
#         else:
#             print(n,":Not Weird")


# input="hello"
# reverse=""

# for i in input:
#     reverse=i+reverse
# print(reverse)


# word="aabcbdcc"
# for i in word:
#     print(i)
#     if word.count(i) == 1:
#         print("it is",i)
#         break



# number=5
# factorial=1

# while number>0:
#     factorial*=number
#     number-=1
# print(factorial)





# //break in if : here the program will terminate if you give something in between 1 and 100
# //continue in if : the program will keep running
# //break in else : here the program will terminate if you give something in outside 1 and 100
# //continue in if : the program will keep running

# while True:
#     i=int(input("give a number:"))
#     if 1<=i<=100:
#         print("thankyou")
#         # continue
#         # break
#     else:
#         print("please try again")
        # break
        # continue
        









   








    












