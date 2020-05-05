#myself
from random import shuffle
SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    def __init__ (self):
        print('Creating a new ordered Deck...')
        self.allcards=[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('Shuffling cards...')
        shuffle(self.allcards)

    def split_the_deck(self):
        self.half1=self.allcards[:26]
        self.half2=self.allcards[26:]
        return self.half1,self.half2

class Player:
    def __init__ (self,cards,name):
        self.cards=cards
        self.name=name
    def still_has_cards(self):
        return len(self.cards)!=0

    def play_cards(self):
        drawn_card=self.cards.pop()
        print('{} has placed {}'.format(self.name,drawn_card))
        return drawn_card

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_war_cards(self):
        war_cards=[]
        if len(self.cards)<3:
                return self.cards
        else:
            for x in range(3):
                war_cards.append(self.cards.pop())
            return war_cards


print('Welcome to war! Lets begin...')
d=Deck()
d.shuffle()
half1,half2=d.split_the_deck()

computer=Player(half1,'computer')
name=input('What is ur name?')
human=Player(half2,name)

total_rounds=0
war_counts=0

while(human.still_has_cards() and computer.still_has_cards()):
    total_rounds+=1
    print('Time for a new round')
    print("Here are the current standings")
    print(human.name+' has count '+str(len(human.cards)))
    print(computer.name + ' has count ' + str(len(computer.cards)))
    print('play a card')
    print('\n')

    c_card=computer.play_cards()
    h_card=human.play_cards()

    table_cards=[]
    table_cards.append(c_card)
    table_cards.append(h_card)

    if(c_card[1]==h_card[1]):
        war_counts+=1
        print('war !')

        table_cards.extend(human.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

    else:
        if(RANKS.index(h_card[1])>RANKS.index(c_card[1])):
            human.add(table_cards)
        else:
            computer.add(table_cards)

print('game completed in {} rounds'.format(str(total_rounds)))
print('No. of war occured ={} '.format(str(war_counts)))

if human.still_has_cards():
    print('YOU WIN !!!')
else:
    print("- You Lose -")
    print('press shift+F10 to play again')

# print('comp='+str(len(computer.cards)))
# print('human='+str(len(human.cards)))










