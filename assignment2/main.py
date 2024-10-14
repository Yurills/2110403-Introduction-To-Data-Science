class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'{self.value} {self.suit}'
    def getScore(self):
        if not self.value.isnumeric():
            if self.value == 'A':
                return 1
            else:
                return 10
        else:
            return int(self.value)
    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    def __lt__(self, rhs):
        lvalue = self.getScore()
        rvalue = rhs.getScore()
        if (lvalue<3):
            lvalue += 10
        if (rvalue<3):
            rvalue += 10
        
        if (lvalue == rvalue):
            sValue = {
                "club": 1,
                "diamond": 2,
                "heart": 3,
                "spade": 4
            }
            return sValue[self.suit] < sValue[rhs.suit]
        else:
            return lvalue < rvalue
    
#**Copy and paste your class with modified functions when submitting to the grader.
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
    print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
    print("----------")
cards.sort()
for i in range(n):
    print(cards[i])