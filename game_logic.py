import random

class MemoryGame:
    def __init__(self):
        self.cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
        self.card_states = ['down'] * len(self.cards)  # All cards initially face down
        self.last_flipped = None  # Keep track of the last flipped card index

    def shuffle_cards(self):
        random.shuffle(self.cards)
        self.card_states = ['down'] * len(self.cards)  # Reset card states
        self.last_flipped = None

    def get_card_states(self):
        return self.card_states

    def flip_card(self, index):
        if 0 <= index < len(self.cards) and self.card_states[index] == 'down':
            self.card_states[index] = 'up'
            if self.last_flipped is None:
                self.last_flipped = index
                return {'match': False, 'completed': False}
            else:
                if self.cards[index] == self.cards[self.last_flipped]:
                    self.last_flipped = None
                    return {'match': True, 'completed': all(state == 'up' for state in self.card_states)}
                else:
                    self.card_states[index] = 'down'
                    self.card_states[self.last_flipped] = 'down'
                    self.last_flipped = None
                    return {'match': False, 'completed': False}
        return {'error': 'Invalid operation'}
