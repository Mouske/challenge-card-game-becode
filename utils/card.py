class Symbol:
    def __init__(self,color,icon):
        self.color = color
        self.icon = icon

color = ["red","black"]
icon = [♥, ♦, ♣, ♠]


class Card(Symbol):
    def __init__(self,color,icon,value):
        self.color = color
        self.icon = icon 
        self.value = value

value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']

