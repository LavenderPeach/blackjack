import random

def draw(hand):
    card_values = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    new_card = random.choice(card_values)
    hand.append(new_card)

class Game:
    def __init__(self):
        self.user_hand = None
        self.computer_hand = None

    def draw_opening(self):
      for i in range(2):
          draw(self.user_hand)
          draw(self.computer_hand)