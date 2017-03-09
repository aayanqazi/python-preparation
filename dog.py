class Dog():
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        """Initialize name and age attritbues"""
        self.name = name
        self.age = age

    def sit(self):
        """Sitimulate a dog sitting in response to a command"""
        print(self.name.title()+"is now sitting")

    def roll_over(self):
        """Sitimulare rolling over in response to a command """
        print(self.name.title()+"rolled over!")


my_dog = Dog("Willie",6)

print("My Dog name is " + my_dog.name.title())
print("My Dog is " + str(my_dog.age)+" Years Old")

my_dog.sit()