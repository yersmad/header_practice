numb, word = input().split()
i = int(numb) - 1
if len(word) > i:
    word = word[0: i:] + word[i + 1::]
print(word)
