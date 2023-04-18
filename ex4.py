word_length = int(input())
word = input()

slices = []
for i in range(word_length):
    chopped_word = word[i:]+word[:i]
    if chopped_word == chopped_word[::-1]:
        slices.append(i)

if 0 in slices:
    slices.remove(0)
    slices.append(word_length)
print(len(slices))
print(*slices, sep="\n")
