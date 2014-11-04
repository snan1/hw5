'''
Sidharth. S. Nandury
HW 5: Guess the Animal
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        i = 1
        for hint in (game_dict[self.name]):
            print ("\tHint "+str(i)+": "+hint)
            answer = input ("\tWho am I?\t")
            if answer.lower()== self.name:
                print ("\tYou're smart! I am a "+self.name)
                break
            else:
                print ("\tMaybe, the next hint should be helpful\n")
                i +=1
            if i > 3:
                print("\tOops, sorry I am out of hints")
                print ("\tThe answer was "+self.name)
            
game_dict = {"elephant": ["I have exceptional memory", "I am the largest land-living mammal in the world", "I have a trunk"],"tiger":["I am the biggest cat", "I come in black and white or orange and black", "I am a carnivore"],"bat":["I use echo-location", "I can fly", "I see well in dark"]}
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

print ("\tI will give you 3 hints, guess what animal I am")

print ("\n\nGuess the first Animal:")
e.guess_who_am_i()
print ("\n\nGuess the second Animal:")
t.guess_who_am_i()
print ("\n\nGuess the thrid Animal:")
b.guess_who_am_i()
