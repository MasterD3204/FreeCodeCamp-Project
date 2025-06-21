# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter

# beat quincy

class QuincySlayer():
    def __init__(self):
        self.turn_counter = 0
        self.quincy_patterns = ["R", "R", "P", "P", "S"]
        self.counter_quincy = {"P":"S","R":"P","S":"R"}
    
    def make_move(self, prev_play, opponent_history=[]):
        predict_move = self.quincy_patterns[self.turn_counter % len(self.quincy_patterns)]
        self.turn_counter += 1
        my_move = self.counter_quincy[predict_move]
        return my_move


class KrisSlayer():
    def __init__(self):
        self.last_move = None
        self.counter = {"P":"S","R":"P","S":"R"}

    def make_move(self, prev_play, opponent_history=[]):
        my_move = ''
        if self.last_move is None:
            my_move = 'R'
        else:
            kris_move = self.counter[self.last_move]
            my_move = self.counter[kris_move]
        self.last_move = my_move
        return my_move

class MrugeshSlayer():
    def __init__(self):
        self.history = []
        self.counter = {"P":"S","R":"P","S":"R"}
        self.move = ['R','P','S']

    def make_move(self, prev_play, opponent_history=[]):
        my_move = ''
        if not self.history:
            my_move = 'S'
        else:
            bait_move = self.move[len(self.history)%3]
            current_history = (self.history + [bait_move])[-10:]

            counts = Counter(current_history)

            
            most_frequent = counts.most_common(1)[0][0]
    
            predict_mru_move = self.counter[most_frequent]
            my_move = self.counter[predict_mru_move]
        self.history.append(my_move)
        return my_move





