cars = ['audi', 'bmw', 'subaru', 'toyota']
for value in cars:
    if value == 'bmw':
        print (value.upper())
    else:
        print (value.title())

#Checking Information in list

requested_toppings =['mashroom','onions','pineapple']
print ('mashroom' in requested_toppings)

#CHecked #Banned #Users

banned_users = ['andrew','carolina','arsalan']
user = "marie"

if user not in banned_users:
    print(user.title()+" you can post a response if you wish")

#Voting

age = 18

if age >= 18:
    print ("You are eligible to vote")

#Multiple Conditions
age = 14
if(age < 4):
    print("Admission is Free !")
elif (age <18):
    print("Your Fee is 8$")
else:
    print("Your admission cost is 10$")

