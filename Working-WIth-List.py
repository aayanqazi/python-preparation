magicians =  ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")


#Range IN Number

for value in range(1,5):
    print(value)

#Range List
numbers = list(range(1,6))
print(numbers)

#Even Number
even_number =list(range(0,100,2))
print (even_number)

#Square OF 10 Numbers
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

#MAximum And Minimum

digits = [2,4,6,8,234,32,579,100]

print(min(digits))
print(max(digits))
print(sum(digits))


#List Comprehension

squating = [value ** 2 for value in range(1,6)]
print(squating)


#Task
for value in range(1,10):
    print(value)

#Odd Numbers
for value in range(1,21,2):
    print (value)

#3 Table
table = [value*3 for value in range(1,31)]
print(table)

