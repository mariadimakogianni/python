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
        temp = ""

        check = False
        word = line
        word = word.upper() #tis kano kefalees afoy to 100*100 einai kefalaio
        word = list(word)
        word.remove('\n')
        word = "".join(word)
        #print word
        for i in range(100):
            templist = []
            temp = "".join(board[i])
            if temp.find(word) != -1:
                print "found: "+word
                break
            for j in range(100):
                templist.append(board[j][i])
            templist = "".join(templist)

            if templist.find(word) != -1:
                print "found: "+ word
                break
            templist = ''.join(reversed(templist)) #koitao mipos yparxei h leksi anapoda h apo kato pros ta pano
            temp = ''.join(reversed(temp))
            if templist.find(word) != -1 or temp.find(word) != -1:
                print "found: "+ word
                break