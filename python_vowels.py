word = str(input("Enter a word : "))
print(word)

isVowel = False

for i in word:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        isVowel = True
        break

if isVowel:
    print("There is vowel")
else:
    print("There is no vowel")    