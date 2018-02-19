import random
import string


board = []
result = []
for j in range(100): #ftiaxno ton pinaka 100*100 me random kefalaia grammata
    rows = []
    for i in range(100):
        letter = random.choice(string.letters)
        rows.append(letter.upper())
    board.append(rows)



with open("words.txt","r") as file:
    for line in file:
        grammi = ""

        check = False
        word = line
        word = word.upper() #tis kano kefalees afoy to 100*100 einai kefalaio
        word = list(word)
        word.remove('\n')
        word = "".join(word)
        for i in range(100):
            stili = []
            grammi = "".join(board[i])
            if grammi.find(word) != -1:
                #print "found: " + word
                if word not in result: result.append(word)
                break
            for j in range(100):
                stili.append(board[j][i])
            stili = "".join(stili)

            if stili.find(word) != -1:
                #print "found: " + word
                if word not in result: result.append(word)
                break
            stili = ''.join(reversed(stili))
            grammi = ''.join(reversed(grammi))
            if stili.find(word) != -1 or grammi.find(word) != -1:
                #print "found: " + word
                if word not in result: result.append(word)
                break
    print result