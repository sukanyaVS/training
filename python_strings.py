#Write a program to create a new string made of an input string’s first, middle, and last character.?
my_word = str(input("Enter any word : "))
x = len(my_word) / 2
y = int(x)
new_word = print("New word : " ,my_word[0] + my_word[y] + my_word[-1])


#write a program to count occurrences of all characters within a string?'
word = "malayalam"

def count_letters(word):
    unique_val = set(word)
    for i in unique_val:
      count = word.count(i)
      print("Count of",i,":",count)

count_letters(word)

#Given string contains a combination of the lower and upper case letters. Write a program 
# to arrange the characters of a string so that all lowercase letters should come first?

word = "MaLbYclLdm"

def my_func(word):
    x = ''
    y = ''
    for i in word:
       if(i.islower()):
          x += i
       else:
          y += i   

    print(x+y)    
    

my_func(word)