# TODO: Try to Write a file
with open("bcit.txt", "w") as file:
    file.write("hello")

# TODO: Try to Read a file
with open("bcit.txt", "r") as file:
    data = file.read()

print(data)
print(type(data))
