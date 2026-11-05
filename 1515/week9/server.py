# TODO: Try to Write a file
file = open("bcit.txt", "w")
file.write("hello")
# file.close()

# TODO: Try to Read a file
file = open("bcit.txt", "r")
data = file.read()
file.close()

print(data)
print(type(data))
