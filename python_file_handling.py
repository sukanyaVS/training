#Write a program to take a source file name and destination file name from the user and 
# copy the data from the source file to the destination file. Also handle FileNotFoundError,
# PermissionError using try...except

def copy_data(source_file,destination_file):
    f1 = open(source_file)
    f2 = open(destination_file,'w+')
    print("=====Source=========")
    print(f1.read())
    f1.seek(0)
    for data in f1:
        f2.write(data)
    print("File copied successfully.")    
    
    print("=====Destination=========")
    f2.seek(0)
    print(f2.read())  




source_file = input("Enter source file name : ")
destination_file = input("Enter destination file name : ")

try:
 copy_data(source_file,destination_file)
except FileNotFoundError:
 print("Error: File not found")
except PermissionError:
    print("Error: Permission denied.") 



#Write a program to display how many lines and words are present in a file called story.txt

try:
    f1 = open('story.txt')
    print("======================")
    print(f1.read())
    f1.seek(0)
    print("======================")
    lines = f1.readlines()
    print("Number of lines : ", len(lines))
    count_words = 0
    for line in lines:
        each_line = line.split()
        count_words += len(each_line)

    print("Numbe of words : ", count_words)
except FileNotFoundError:
    print("Error: File not found")    

#3.Write a Python program to ask the user for a word and display how many times it 
# appears in the file data.txt.

def search_word(word):
    f1 = open('data.txt')
    print("=======Full data==========")
    print(f1.read())
    print("===========================")
    
    f1.seek(0)
    lines = f1.readlines()
    word_count = 0

    for line in lines:
        each_line = line.split()
        for words in each_line:
            words = words.lower()
            if word == words:
                word_count += 1
    if word_count > 0:            
      print("Count of word",word,"is:",word_count)
    else:
      print("No similar word")  

user_word = input("Enter a word to search : ")
user_word = user_word.lower()
try:
    search_word(user_word)
except FileNotFoundError:
    print("Error: File not found")    
 