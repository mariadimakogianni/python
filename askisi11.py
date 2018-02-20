import random
import string


board = []
result = []
for j in range(100):
    rows = []
    for i in range(100):
        letter = random.choice(string.letters)
        rows.append(letter.upper())
    board.append(rows)


arxeio = raw_input("dose onoma arxeiou ")
with open(arxeio,"r") as file:
    for line in file:
        grammi = ""

        check = False
        word = line
        word = word.upper()
        word = list(word)
        word.remove('\n')
        word = "".join(word)
        for i in range(100):
            stili = []
            grammi = "".join(board[i])
            if grammi.find(word) != -1:
                if word not in result: result.append(word)
                break
            for j in range(100):
                stili.append(board[j][i])
            stili = "".join(stili)

            if stili.find(word) != -1:
                if word not in result: result.append(word)
                break
            stili = ''.join(reversed(stili))
            grammi = ''.join(reversed(grammi))
            if stili.find(word) != -1 or grammi.find(word) != -1:
                if word not in result: result.append(word)
                break
    print result