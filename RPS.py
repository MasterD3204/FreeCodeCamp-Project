# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.
import random
R, P, S = 'R', 'P', 'S'
MOVES = [R, P, S]

class MarkovBot():
    def __init__(self, order=2):
        self.order = order
        self.counter = {P: S, R: P, S: R} 
        self.history = []      
        self.transitions = {}     

    def predict_opponent_move(self):

        if len(self.history) < self.order:
            return None 
        
        last_sequence = "".join(self.history[-self.order:])

        if last_sequence not in self.transitions:
            return None 

        # Tìm nước đi có khả năng xảy ra cao nhất
        prediction_counts = self.transitions[last_sequence]
        prediction = max(prediction_counts, key=prediction_counts.get)
        return prediction

    def playy(self, last_opponent_move=""):
        if last_opponent_move != "" and last_opponent_move in MOVES:
            if len(self.history) >= self.order:
                last_sequence = "".join(self.history[-self.order:])
                if last_sequence not in self.transitions:
                    self.transitions[last_sequence] = {R: 0, P: 0, S: 0}
                # Ghi nhận nước đi của đối thủ
                self.transitions[last_sequence][last_opponent_move] += 1
            self.history.append(last_opponent_move)

        opponent_prediction = self.predict_opponent_move()
        my_move = ""
        if opponent_prediction is not None:
            my_move = self.counter[opponent_prediction]
        else:
            my_move = random.choice(MOVES) 
        return my_move