from random import choice,shuffle
import time
import random
from time import sleep
import os



def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)



##Level 1
words = open("words.txt").read().splitlines()
words = [ w for w in words if "'" not in w ]
words = [ w for w in words if w[0] == w[0].lower() ]
words = [ w for w in words if len(w) > 2 ]
words = [ w for w in words if len(w) == 4 ]

print "Level 1"
time.sleep(1)


lives = 5
correct = 0
skip=6


while lives > 0 :
    x = choice(words)


    xs = [ c for c in x ]
    shuffle(xs)

    guess=raw_input(str("Make a word out of these letters: %s : " % " ".join(xs)))


    time.sleep(1)

    ##level 1
    if is_anagram(guess, x) and guess in words  :
        time.sleep(0.5)
        print "Correct! "
        correct = correct + 1
        time.sleep(1)
        clear = lambda: os.system('clear')
        clear()


    elif guess=="s" and skip>0:
        skip=skip-1
        print "you have" , skip ,  "skip(s) left"
        clear = lambda: os.system('clear')
        time.sleep(1)
        clear()

    elif guess=="" or len(guess)<4 :
       print "invalid Input try again"
       clear = lambda: os.system('clear')
       time.sleep(1)
       clear()



    else :
        print "Incorrect, the correct answer is", x
        time.sleep(1)
        lives=lives-1
        print "you have " ,lives ,"live left"
        clear = lambda: os.system('clear')
        time.sleep(1)
        clear()






    ##level 2
    if correct==5:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 2 "
        time.sleep(2)
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 5 ]
        x = choice(words)




    ##Level 3
    if correct==10:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 3 "
        time.sleep(2)
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 6 ]
        x = choice(words)

    ##level 4
    if correct==15:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 4 "
        time.sleep(2)
        clear = lambda: os.system('clear')
        clear()
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 7 ]
        x = choice(words)

    ##level 5
    if correct==20:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 5 "
        time.sleep(2)
        clear = lambda: os.system('clear')
        clear()
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 8 ]
        x = choice(words)

    ##Level 6
    if correct==25:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 7 "
        time.sleep(2)
        clear = lambda: os.system('clear')
        clear()
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 9 ]
        x = choice(words)

    ##Level 7
    if correct==30:
        time.sleep(0.5)
        clear = lambda: os.system('clear')
        clear()
        print "level 7 "
        time.sleep(2)
        clear = lambda: os.system('clear')
        clear()
        words = open("words.txt").read().splitlines()
        words = [ w for w in words if "'" not in w ]
        words = [ w for w in words if w[0] == w[0].lower() ]
        words = [ w for w in words if len(w) > 2 ]
        words = [ w for w in words if len(w) == 10 ]
        x = choice(words)














print "Game Over! You score was ", correct

print raw_input("Press enter to exit")



