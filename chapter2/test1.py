# 关于_str__和__str__方法
# 非集合对象的重写
class Card:
    insure = False
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit =suit
        self.hard,self.soft = self._point()

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r},rank = {rank!r})".format(__class__=self.__class__ ,**self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)


class NumberCard(Card):
    def _point(self):
        return int(self.rank),int(self.suit)

x = NumberCard('2','100')

print(str(x),repr(x))


# 集合对象的重写
class Hand:
    def __init__(self,dealer_card,*cards):
        self.dealer_card = dealer_card
        # 集合对象
        self.cards = list(cards)

    def __str__(self):
        return ",".join(map(str,self.cards))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r},{_cards_str})".format(__class__=self.__class__,_cards_str=",".join(map(repr,self.cards)),**self.__dict__)

