words = open("word.txt", "r").read().split()
long_word = ""
lm = 0
for x in words:
    l = len(x)
    if l > lm:
       long_word = x
       lm = l
print(long_word)