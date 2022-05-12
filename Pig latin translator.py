#the following is for specific vowel rules

# word = input("Write a word: ")

# word = word.split()

# for i in range(len(word)):
#     if word[i][0] in "aeiou":
#         word[i] += 'yay'
#     else:
#         word[i]=word[i][1:]+word[i][0]
#         word[i]+='ay'
# word = ' '.join(word)

# print(word)

#the following is for generic translation

word = input("Write a word: ")

new_word = word[1:] +'ay'

print(new_word)

#Note: man I was more happy than I needed to be when I was able to splice together line (19-23) yayy