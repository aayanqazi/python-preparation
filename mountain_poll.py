responses = {}

active = True

while active:
    name = input("\n What is your name??")
    response = input("Which mountain would you like to climb someday?")
    responses[name]=response

    repeat = input("\n Would you like to another response? (Y / N")
    if(repeat == "n"):
        active = False

print ("n --- Poll Result ----")
for name,response in responses.items():
    print(name + " would like to climb " + response+".")