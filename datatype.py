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
#     print("chutiya mat bana")
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
#     ripeness="gelchoda"

# print(ripeness)



# colour=input("what is the colour of your banana? \n")

# if colour=="green":
#    print("unripe")

# elif colour=="yellow":
#     print("ripe")
  

# elif colour=="brown":
#     print("overripe")

# else:
#     print("gelchoda")




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


day=["monday","tuesday","wednesday","thu","fri","sat","sun"]
meal=["breakfast","lunch","dinner"]


for a in day:
    print("today is",a) 
    for b in meal:
        if b=="dinner":
            break
        print ("i had ", b)
        print ("")






    












