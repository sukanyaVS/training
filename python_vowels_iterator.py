x = 'Hello i am Sukanya A'

def get_vowels(word):
    for i in word:
     i.lower()
     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
      yield i


def print_vowels(word):
    for i in get_vowels(word):
        print(i)

print_vowels(x)