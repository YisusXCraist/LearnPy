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

json_file.close() # close the file

# read the json file
with open('NoobLvl2\my_file.json') as my_other_file: # a means append
    for line in my_other_file.readlines():
        print(line) # print the json file

json_dict = json.load(open('NoobLvl2\my_file.json')) # load the json file into a dictionary
print(json_dict) # print the dictionary
print(type(json_dict)) # print the type of the dictionary

# .csv file
# csv file is a file that contains data in a csv format

import csv

csv_file = open('NoobLvl2\my_file.csv', "w+", newline='') # w+ means write and read

csv_writer = csv.writer(csv_file) # create a csv writer

csv_writer.writerow(["Nombre", "Apellido", "Edad"]) # write a row in the csv file
csv_writer.writerow(["John", "Doe", 30]) # write a row in the csv file

csv_file.close() # close the file

with open('NoobLvl2\my_file.csv') as my_other_file: # a means append
    for line in my_other_file.readlines():
        print(line) # print the csv file


# .xlsx file
# xlsx file is a file that contains data in a xlsx format

# import xlrd #The module needs to be installed

# .xml file
# xml file is a file that contains data in a xml format

import xml 
