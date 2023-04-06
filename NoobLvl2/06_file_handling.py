### File Handling ###

# .txt file
# txt file is a plain text file

txt_file = open('NoobLvl2\my_file.txt', "r+") # r+ means read and write
#print(txt_file.read()) # read the file
#print(txt_file.read(5)) # read the first 5 characters, but this will not print the first 5 characters, it will print the next 5 characters, after the first read
#print(txt_file.readline()) # read the first line, but this will not print the first line, it will print the next line, after the first read

for line in txt_file.readlines(): # read all the lines and print them
    print(line)

txt_file.write("\nThis is a new line") # write a new line in the file
print(txt_file.read()) # read the file

txt_file.close() # close the file

with open('NoobLvl2\my_file.txt', "a") as my_other_file: # a means append
    my_other_file.write("\nThis is a new line :D")

# .json file
# json file is a file that contains data in a json format

import json

json_file = open('NoobLvl2\my_file.json', "w+") # w+ means write and read

json_test = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json.dump(json_test, json_file, indent = 2) # dump the json_test data into the json_file