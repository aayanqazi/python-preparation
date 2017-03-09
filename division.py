print("Give me two numbers, and I'll divide them.")
print ("Enter 'q' to quit")

while True:
    first_Number = input("\n First Number: ")
    if first_Number == 'q':
        break
    second_number = input("\n Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_Number) / int(second_number)
    except ZeroDivisionError:
        print("SOrry")
    else:
        print(answer)