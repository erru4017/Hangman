'''
Erin Ruby
TA: Amber Womack
Python Project = Hangman
'''

import random #import libraries

class hangman:
    def __init__(self):
        self.fruitlist = [] #list for the fruit category
        self.citieslist = [] #list for the cities category
        self.animallist = [] #list for the animal category
        with open("animal.txt", 'r') as animals:
            for line in animals:
                self.animallist.append(line.strip()) #add words from the file into the animal list
        with open("fruits.txt", 'r') as fruits:
            for line in fruits:
                self.fruitlist.append(line.strip()) #add words from the file into the fruit list
        with open("cities.txt", 'r') as cities:
            for line in cities:
                self.citieslist.append(line.strip()) #add words from the file into the city list
        self.categoryDictionary = {"cities":self.citieslist, "animal":self.animallist, "fruit":self.fruitlist} #complex dictionary
    def buildbody(self, wrong, unknownword): #function to keep track on wrong guesses and print out the hangman
        if wrong == 1:
            print('''
            ---+--
            |  |
            |  O
            |
            |
            ________
            ''')
        if wrong == 2:
            print('''
            ---+--
            |  |
            |  O
            |  |
            |
            ________
            ''')

        if wrong == 3:
            print('''
            ---+--
            |  |
            |  O
            |  |
            |   \
            ________
            ''')
        if wrong == 4:
            print('''
            ---+--
            |  |
            |  O
            |  |
            | / \
            ________
            ''')
        if wrong == 5:
            print('''
            ---+--
            |  |
            |  O
            |  |-
            | / \
            ________
            ''')

        if wrong == 6:
            print('''
            ---+--
            |  |
            |  O
            | -|-
            | / \
            ________
            ''')
            print("You lost. The word was",unknownword,".")
            quit()

    def writewinningword(self, unknownword):
        winner = open('HiddenWord.txt', 'w')
        winner.write("The word was "+unknownword + ".")
        winner.close()

class player:
    def __init__(self, man):
        self.hangman = man

    def pickCategory(self):
        choice = str(input("Pick a category: cities, animal, fruit: "))
        categorylist = self.hangman.categoryDictionary[choice]
        random1 = random.randint(0,len(categorylist)-1) #use of the imported library random
        unknownword = categorylist[random1]
        return categorylist[random1]

    def blankspaces(self, unknownword):
        blanks = []
        for i in range(len(unknownword)):
            blanks.append('_')
            i+=1
        return blanks


    def guessing(self, unknownword, blanks):
        numguess = 0
        j = 0
        wrong = 0
        while '_' in blanks:
            guess = str(input("Guess a letter or entire word: "))
            if guess == unknownword:
                print("Nice work, you have guessed the correct word!!")
                quit()
            if guess in unknownword:
                for j in range(len(unknownword)):
                    if unknownword[j] == guess:
                        blanks[j] = guess
                        print(blanks)
                    j+=1
            else:
                wrong+=1
                self.hangman.buildbody(wrong, unknownword)

            numguess +=1
        if '_' not in blanks:

            print("Congrats! You have guessed the word!")
def main():
    try:
        with open("rules.txt", 'r') as rules:
            for line in rules:
                print(line.strip())
    except IOError:
        print("Could not find the rules... sorry")
        exit()
    p = player(hangman())
    h = hangman()
    playerchoice = p.pickCategory()
    spaces = p.blankspaces(playerchoice)
    print(spaces)
    playerguess = p.guessing(playerchoice, spaces)
    h.writewinningword(playerchoice)
    #print playerguess


main()
