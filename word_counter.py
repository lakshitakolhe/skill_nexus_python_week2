file = open("sample.txt.txt", "r")

text = file.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("Number of words:", len(words))
print("Number of lines:", len(lines))
print("Number of characters:", characters)

file.close()