x = 'Hello i am Sukanya A'

#Define a generator that will extract vowels from a given string and print them one by one.
def get_vowels(word):
    for i in word:
     i.lower()
     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
      yield i


def print_vowels(word):
    for i in get_vowels(word):
        print(i)

print_vowels(x)
print("--------------------------------------------------")

#Using an iterator, display only the vowels from a given string.
class IteratVowels:
    def __init__(self, word):
     self.word = word
     self.index = 0

    def __iter__(self):
     return self

    def __next__(self):
        while self.index < len(self.word):
            ltr = self.word[self.index]
            self.index += 1
            if ltr.lower() in 'aeiou':
                return ltr
        raise StopIteration

for i in IteratVowels(x):
    print(i)


#Define a generator that will print all the words of a sentence one by one.

my_word = "Define a generator that will print all the words of a sentence one by one."

def print_word(word):
   new_sent = word.split()
   for i in new_sent:
    yield i


def split_words(sentance):
   for i in print_word(sentance):
     print(i)

split_words(my_word)