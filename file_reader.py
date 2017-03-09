filename = "pi_digits.txt"
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
 # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")