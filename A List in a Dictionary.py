#List Of Dictionary

pizza = {
    'crust':'thick',
    'toppings': ['mashrooms', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for toppings in pizza['toppings']:
    print ("\t"+toppings)


#Examples 2

favourite_languages= {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    ' edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favourite_languages.items():
    print("\n"+name.title()+"'s favourite languages are :")
    for language in languages:
        print ("\t"+language.title())