import random

def draw(hand):
    card_values = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    new_card = random.choice(card_values)
    hand.append(new_card)

class Game:
    def __init__(self):
        self.user_hand = None
        self.computer_hand = None

    def reset(self):
        self.computer_hand = []
        self.user_hand = []

    def hit(self):
        continue_game = True
        while continue_game and not self.user_bust():
          next_move = input("Would you like to draw another card? Type 'Yes' or 'No'")
          if next_move == 'Yes':
              self.user_draws
          else:
              continue_game = False
    
    def user_draws(self):
        draw(self.user_hand)

        if self.user_aces and self.user_bust():
            self.switch_ace

    def user_aces(self):
      return 11 in self.user_hand
    
    def user_bust(self):
        if sum(self.user_hand > 21):
            print('Busted!!')

    def switch_ace(self):
          self.user_hand.remove(11)
          self.user_hand.append(1)
    
    def draw_opening(self):
      for i in range(2):
          draw(self.user_hand)
          draw(self.computer_hand)