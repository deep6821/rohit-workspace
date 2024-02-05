"""
Blackjack is the most widely played casino game in the world. It falls under the category of comparing-card games
and is usually played between several players and a dealer.

Each player, in turn, competes against the dealer, but players do not play against each other. In Blackjack, all
players and the dealer try to build a hand that totals 21 points without going over. The hand closest to 21 wins.

System Requirements:
-------------------
Blackjack is played with one or more standard 52-card decks. The standard deck has 13 ranks in 4 suits.

Background:
- To start with, the players and the dealer are dealt separate hands. Each hand has two cards in it.
- The dealer has one card exposed (the up card) and one card concealed (the hole card), leaving the player with
incomplete information about the state of the game.
- The player’s objective is to make a hand that has more points than the dealer, but less than or equal to 21 points.
- The player is responsible for placing bets when they are offered, and taking additional cards to complete their hand.
- The dealer will draw additional cards according to a simple rule: when the dealer’s hand is 16 or less, they will
draw cards (called a hit), when it is 17 or more, they will not draw additional cards (or stand pat).

Points calculation:
Blackjack has different point values for each of the cards:
- The number cards (2-10) have the expected point values.
- The face cards (Jack, Queen, and King) all have a value of 10 points.
- The Ace can count as one point or eleven points. Because of this, an Ace and a 10 or face card totals 21.
This two-card winner is called "blackjack".
- When the points include an ace counting as 11, the total is called soft-total; when the ace counts as 1, the
total is called hard-total. For example, A+5 can be considered a soft 16 or a hard 6.

Gameplay:
1. The player places an initial bet.
2. The player and dealer are each dealt a pair of cards.
3. Both of the player’s cards are face up, the dealer has one card up and one card down.
4. If the dealer’s card is an ace, the player is offered insurance.

Initially, the player has a number of choices:
- If the two cards are the same rank, the player can elect to split into two hands.
- The player can double their bet and take just one more card.
- The more typical scenario is for the player to take additional cards (a hit ) until either their hand totals
more than 21 (they bust ), or their hand totals exactly 21, or they elect to stand.

If the player’s hand is over 21, their bet is resolved immediately as a loss. If the player’s hand is 21 or less,
it will be compared to the dealer’s hand for resolution.

Dealer has an Ace: If the dealer’s up card is an ace, the player is offered an insurance bet. This is an
additional proposition that pays 2:1 if the dealer’s hand is exactly 21. If this insurance bet wins, it will,
in effect, cancel the loss of the initial bet. After offering insurance to the player, the dealer will check
their hole card and resolve the insurance bets. If the hole card is a 10-point card, the dealer has blackjack,
the card is revealed, and insurance bets are paid. If the hole card is not a 10-point card, the insurance bets
are lost, but the card is not revealed.

Split Hands: When dealt two cards of the same rank, the player can split the cards to create two hands. This
requires an additional bet on the new hand. The dealer will deal an additional card to each new hand, and the
hands are played independently. Generally, the typical scenario described above applies to each of these hands.

Bets:
- Ante: This is the initial bet and is mandatory to play.
- Insurance: This bet is offered only when the dealer shows an ace. The amount must be half the ante.
- Split: This can be thought of as a bet that is offered only when the player’s hand has two cards of equal rank.
 The amount of the bet must match the original ante.
- Double: This can be thought of as a bet that is offered instead of taking an ordinary hit. The amount of the
bet must match the original ante.
"""

from abc import ABC
import datetime
from enum import Enum
import random


class SUIT(Enum):
    HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4


# Card: The following class encapsulates a playing card:
class Card:
    def __init__(self, suit, face_value):
        self.__suit = suit
        self.__face_value = face_value

    def get_suit(self):
        return self.__suit

    def get_face_value(self):
        return self.__face_value


# BlackjackCard: BlackjackCard extends from Card class to represent a blackjack card:
class BlackjackCard(Card):
    def __init__(self, suit, face_value):
        super().__init__(suit, face_value)
        self.__game_value = face_value
        if self.__game_value > 10:
            self.__game_value = 10

    def get_game_value(self):
        return self.__game_value


class Deck:
    def __init__(self):
        self.__cards = []
        self.__creation_date = datetime.date.today()
        for value in range(1, 14):
            for suit in SUIT:
                self.__cards.append(BlackjackCard(suit, value))

    def get_cards(self):
        return self.__cards


# Deck and Shoe: Shoe contains cards from multiple decks:
class Shoe:
    def __init__(self, number_of_decks):
        print("number_of_decks --->>>", number_of_decks)
        self.__cards = []
        self.__number_of_decks = number_of_decks
        self.create_shoe()
        self.shuffle()

    def create_shoe(self):
        for decks in range(0, self.__number_of_decks):
                self.__cards.append(Deck().get_cards())

    import random

    def shuffle(self):
        card_count = len(self.__cards)
        for i in range(0, card_count):
            j = random.randrange(0, card_count - i - 1, 1)
            print("\n j---->>", j)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

    # Get the next card from the shoe
    def deal_card(self):
        if len(self.__cards) == 0:
            self.create_shoe()
        return self.__cards.remove(0)


# Hand: Hand class encapsulates a blackjack hand which can contain multiple cards
class Hand:
    def __init__(self, blackjack_card1, blackjack_card2):
        self.__cards = [blackjack_card1, blackjack_card2]

    def get_scores(self):
        totals = [0]

        for card in self.__cards:
            new_totals = []
            for score in totals:
                new_totals.append(card.face_value() + score)
                if card.face_value() == 1:
                    new_totals.append(11 + score)

            totals = new_totals

        return totals

    def add_card(self, card):
        self.__cards.append(card)

    # get highest score which is less than or equal to 21

    def resolve_score(self):
        scores = self.get_scores()
        best_score = 0
        for score in scores:
            if 21 >= score > best_score:  # score <= 21 and score > best_score
                best_score = score

        return best_score


# Player: Player class extends from BasePlayer:
class BasePlayer(ABC):
    # def __init__(self, id, password, balance, status, person):
    #     self.__id = id
    #     self.__password = password
    #     self.__balance = balance
    #     self.__status = status
    #     self.__person = person
    #     self.__hands = []

    def __init__(self):
        self.__hands = []

    def reset_password(self):
        None

    def get_hands(self):
        return self.__hands

    def add_hand(self, hand):
        return self.__hands.append(hand)

    def remove_hand(self, hand):
        self.__hands.remove(hand)


class Player(BasePlayer):
    # def __init__(self, id, password, balance, status, person):
    #     super.__init__(id, password, balance, status, person)

    def __init__(self):
        super(Player, self).__init__()
        self.__bet = 0
        self.__total_cash = 0


class Dealer(BasePlayer):
    # def __init__(self, id, password, balance, status, person):
    #     super.__init__(id, password, balance, status, person)

    def __init__(self):
        super(Dealer, self).__init__()


# Game: This class encapsulates a blackjack game:
class Game:
    def __init__(self, player, dealer):
        self.__player = player
        self.__dealer = dealer
        self.__MAX_NUM_OF_DECKS = 3
        self.__shoe = Shoe(self.__MAX_NUM_OF_DECKS)

    def play_action(self, action, hand):
        switcher = {
            "hit": self.hit(hand),
            "split": self.split(hand),
            "stand pat": None,  # do nothing
            "stand": self.stand()
        }
        switcher.get(action, 'Invalid move')

    def hit(self, hand):
        self.__hand.add_card(self.__shoe.deal_card())

    def stand(self):
        dealer_score = self.__dealer.get_total_score()
        player_score = self.__player.get_total_score()
        hands = self.__player.get_hands()
        for hand in hands:
            best_score = hand.resolve_score()
            if player_score == 21:
                # blackjack, pay 3: 2 of the bet
                None
            elif player_score > dealer_score:
                # pay player equal to the bet
                None
            elif player_score < dealer_score:
                # collect the bet from the player
                None
            else:  # tie
                # bet goes back to player
                None

    def split(self, hand):
        cards = hand.get_cards()
        self.__player.add_hand(Hand(cards[0], self.__shoe.deal_card()))
        self.__player.add_hand(Hand(cards[1], self.__shoe.deal_card()))
        self.__player.remove_hand(hand)

    def start(self):
        # self.__player.place_bet(get_bet_from_UI())

        player_hand = Hand(self.__shoe.deal_card(),
                           self.__shoe.deal_card())
        self.__player.add_to_hand(player_hand)

        dealer_hand = Hand(self.__shoe.deal_card(),
                           self.__shoe.deal_card())
        self.__dealer.add_to_hand(dealer_hand)

        while True:
            hands = self.__player.get_hands()
            print("hands --->>>", hands)
            for hand in hands:
                action = get_user_action(hand)
                self.play_action(action, hand)
                if action.equals("stand"):
                    break


def main():
    player = Player()
    dealer = Dealer()
    print(player, type(player), dealer, type(dealer))
    game = Game(player, dealer)
    game.start()


if __name__ == "__main__":
    main()