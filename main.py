fileName = input("Enter the file name: ")
file = open(fileName, "r")

contents = file.read()
words = contents.split()
# numWords = len(words)
# print("your content is: " + contents, "[- And the number of words in the file is]:", len(words))
print(f"The file \"{fileName}\" contains {len(words)} words.")