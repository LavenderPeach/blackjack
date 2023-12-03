import random

def draw(hand):
    card_values = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    new_card = random.choice(card_values)
    hand.append(new_card)

class Game:
    def __init__(self):
        self.user_hand = None
        self.computer_hand = None
        self.new_user_hand = None

    def blackjack(self):
        self.reset()
        self.draw_opening()
        self.print_hands()
        self.hit()
        self.computer_limit()
        self.outcome()
        self.final_score()

    def reset(self):
        self.computer_hand = []
        self.user_hand = []

    def hit(self):
        for i in range(1):
             self.split()
             self.first_double()
             self.split_double()
             if len(self.user_hand) == 3:
                return
             self.first_hand_hit()
             if len(self.new_user_hand) == 3 and self.new_user_hand is not None:
                 return
             self.second_hand_hit()

    def first_hand_hit(self):
        if self.user_bust():
            return
        next_move = input("Would you like to draw another card? Type 'Yes' or 'No'")
        if next_move == 'Yes':
            self.user_draws()
            print(self.user_hand, self.new_user_hand)
            self.first_hand_hit()
        elif next_move == 'No':
            return
        
    def second_hand_hit(self):
        if self.second_bust():
            return
        next_move = input("Would you like to draw another card? Type 'Yes' or 'No'")
        if next_move == 'Yes':
            self.split_draw()
            print(self.user_hand, self.new_user_hand)
            self.second_hand_hit()
        elif next_move == 'No':
            return
    def split(self):
        if self.user_hand[0] == self.user_hand[1] and len(self.user_hand) == 2:
            split_choice = input("Would you like to split your hand? Type 'Yes' or 'No'")
            if split_choice == 'Yes':
                temp = self.user_hand[1] 
                self.new_user_hand = []
                self.new_user_hand.append(temp)
                self.user_hand.pop()
                for i in range(1):
                    draw(self.user_hand)
                    draw(self.new_user_hand)
                print(self.user_hand, self.new_user_hand)
                return
                
            elif split_choice == 'No':
                return
        else:
            return
        
    def first_double(self):
        if len(self.user_hand) == 2:
            double_choice = input('Would you like to double down on this hand?')
            if double_choice == 'Yes':
                for i in range(1):
                    self.user_draws()
                    return
            elif double_choice == 'No':
                return
        return
    
    def split_double(self):
        if self.new_user_hand is not None:
            if len(self.new_user_hand) == 2:
                double_choice = input('Would you like to double down on this hand?')
                if double_choice == 'Yes':
                    for i in range(1):
                        self.split_draw()
                        return            
                elif double_choice == 'No':
                    return
            else:
                return
        return

    def user_draws(self):
        draw(self.user_hand)
        if self.user_aces() and self.user_bust():
            self.switch_ace()
        print(self.user_hand)

    def split_draw(self):
        draw(self.new_user_hand)
        if self.user_aces() and self.user_bust():
            self.switch_ace()
        print(self.new_user_hand)

    def user_aces(self):
      return 11 in self.user_hand
    
    def user_bust(self):
        return sum(self.user_hand) > 21

    def second_bust(self):
        if self.new_user_hand is not None:
            return sum(self.new_user_hand) > 21 

    def switch_ace(self):
          self.user_hand.remove(11)
          self.user_hand.append(1)
    
    def computer_limit(self):
        if not self.user_bust():
            while sum(self.computer_hand) < 17:
                draw(self.computer_hand)
        return self.computer_hand

    def outcome(self):
        if sum (self.user_hand) == 21 and len(self.user_hand) == 2 and sum(self.computer_hand) != 21:
            print("Blackjack!")
        if sum(self.user_hand) != 21 and sum(self.computer_hand) == 21 and len(self.computer_hand) == 2:
            print("Dealer has blackjack!")
        elif self.user_bust():
            print("Bust!!!")
        elif sum(self.user_hand) == sum(self.computer_hand):
            print("Draw!")
        elif sum(self.user_hand) < sum(self.computer_hand) <= 21:
            print("Dealer wins!")
        else:
            print("You win!")
    
    def print_hands(self):
        print(f'User Hand: {self.user_hand}')
        print(f'Computer Hand {self.computer_hand[0]}')


    def final_score(self):
        print(f'Your final score is {sum(self.user_hand)} ({self.user_hand})')
        if self.new_user_hand is not None:
            print(f'{sum(self.new_user_hand)} ({self.new_user_hand})')
        print(f'CPU final score is {sum(self.computer_hand)} ({self.computer_hand})')


    
    def draw_opening(self):
      for i in range(2):
          draw(self.user_hand)
          draw(self.computer_hand)


game_instance = Game()
game_instance.blackjack()