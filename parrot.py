prompt = "\n Tell me something and i will repeat it back to you:"
prompt += "\nENter 'quit' to end the program"

active = True

message = ""

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)