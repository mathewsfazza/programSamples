#CS4349 - Advanced Algorithm Design
#This program was created by Mathews Fazza as the programming project for CS4349
#
#there are three ways to run the program:
#1 - No arguments: if the program is run without arguments the user will be prompted to enter a text to be justified
#2 - 1 argument: The argument needs to be a valid filename.  The file will be output justified.
#3 - 2 arguments: In this mode the user can specify both the file and the width of each line.  A negative width
#                 will change the extra spaces into plus signs
#
#The algorithm is described in the report.  Please, see the report for details on this implementation

import math
import sys

def Print_Neatly(words, n, M):
    extras = [[9999 for i in range(n + 1)] for j in range(n + 1)]
    lc = [[9999 for i in range(n + 1)] for j in range(n + 1)]
    c = [sys.maxsize] * (n + 1)
    p = [9999] * (n + 1)

    #find the values of extras
    for i in range(1, n+1):
        extras[i][i] = M - len(words[i])
        for j in range(i+1, n+1):
            extras[i][j] = extras[i][j-1] - len(words[j]) - 1

    #find the values of lc
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (extras[i][j] < 0 and extras[i][j]):
                lc[i][j] = sys.maxsize
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = math.pow((extras[i][j]), 3)

    #find c and p
    c[0] = 0
    for j in range(1, n+1):
        for i in range(1, j+1):
            if c[i-1] + lc[i][j] < c[j]:
                c[j] = c[i-1] + lc[i][j]
                p[j] = i

    return c, p

def Build_Line(text, j, P):

    i = P[j]
    line = 1
    if i != 1:
        line = Build_Line(text, i - 1, P) + 1

    #find the number of extra spaces needed for each line
    extra_spaces  = M - ( sum(map(len, text[i:(j+1)])) + len(text[i:(j+1)])) +1

    #this loop will print justified and add spaces as necessary
    for x in range(i, j+1):

        #first word of line
        if(x == i):
            print(text[x], end=' ')
        #last word of line
        elif(x == j+1):
            print(text[x], end='')
        #all other words have a chance of having an extra space attached to them
        else:
            if(extra_spaces>0):
                if(S==-1):
                    print(text[x], end='+ ')
                else:
                    print(text[x], end='  ')
                extra_spaces += -1

            else:
                print(text[x], end=' ')

    print()
    return line

def main(argv):
    text = ''
    global M
    global S #switch to turn spaces into plus signs
    S = 0
    if(len(argv)<1):
        text = input("Please enter the text to be justified.")
        M=80
    elif(len(argv)==1):
        try:
            textfile = open(sys.argv[1], 'r')
            text = textfile.read()
            M=80
        except FileNotFoundError:
            print("Please, try a valid file name next time.")
    elif(len(argv)==2):
        try:
            textfile = open(sys.argv[1], 'r')
            text = textfile.read()
        except FileNotFoundError:
            print("Please, try a valid file name next time.")
        try:
            M = int(sys.argv[2])
            if(M<0):
                M = abs(M)
                S = -1
        except ValueError:
            print("Please, enter a number as your second argument.")

    paragraphs = text.split('\n')
    paragraphs = list(filter(None, paragraphs))

    for words in paragraphs:
        words = ['BLANK'] + words.split(' ')
        n = len(words) - 1
        C, P = Print_Neatly(words, n, M)
        Build_Line(words, n, P)
        print()


if __name__ == '__main__':
    main(sys.argv[1:])