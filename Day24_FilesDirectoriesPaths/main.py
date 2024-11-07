# file = open("Day24_FilesDirectoriesPaths\my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("Day24_FilesDirectoriesPaths\my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("Day24_FilesDirectoriesPaths\my_file.txt",mode='w') as file:
#     file.write("New text")

# with open("Day24_FilesDirectoriesPaths\my_file.txt",mode='a') as file:
#     file.write("\nNew Text")

# with open(r"Day24_FilesDirectoriesPaths\new_file.txt",mode='w') as file:
#     file.write("New File")