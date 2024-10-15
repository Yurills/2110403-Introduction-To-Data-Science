class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'({self.value} {self.suit})'
    def next1(self):
        suits = ['club', 'diamond', 'heart', 'spade']
        values = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suit = self.suit
        value = self.value
    
        if suit != 'spade':
            suit = suits[suits.index(suit)+1]
        else:
            suit = 'club'
            if value != '2':
                value = values[values.index(value)+1]
            else: value = '3'
        return Card(value, suit)
            

    def next2(self):
        suits = ['club', 'diamond', 'heart', 'spade']
        values = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suit = self.suit
        value = self.value
    
        if suit != 'spade':
            self.suit = suits[suits.index(suit)+1]
        else:
            self.suit = 'club'
            if value != '2':
                self.value = values[values.index(value)+1]
            else: self.value = '3'
            
#**Copy and paste your class with modified functions when submitting to the grader.

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i]) 