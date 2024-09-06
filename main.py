from countries import *
from functions import *
import random

class Game:

    def __init__(self) -> None:
        self.current_pos = None
        self.steps = 0
        self.relation = R
        self.start = None
        self.goal = None
        self.options = None
        self.length = None


    def generate_start_and_end_country(self, difficulty):
        is_found = False
        difficulty = difficulty.lower()
        while not is_found:
            c1 = random.choice(countries)
            c2 = random.choice(countries)
            if is_reachable(c1, c2, self.relation):
                length = len(shortest_way(c1, c2, R))
                if difficulty == "easy" and length  < 7:
                    is_found = True
                    return (c1, c2)
                elif difficulty == "medium" and length < 12 and length >= 7:
                    is_found = True
                    return (c1, c2)
                elif difficulty == "hard" and length < 15 and length >= 12:
                    is_found = True
                    return (c1, c2)
        # return ("", "")
                
    def reset(self):
        self.steps = 0
        self.relation = R

    def move(self, destination):
        self.steps += 1
        self.relation = remove_pair(self.current_pos, destination, self.relation)
        self.current_pos = destination
        self.options = self.image_of(self.current_pos)

    def is_game_over(self):
        if self.current_pos == self.goal:
            return True
        elif is_reachable(self.current_pos, self.goal, self.relation):
            return False
        return True
    
    def has_won(self):
        return self.current_pos == self.goal
    
    def start_game(self, difficulty):
        c1, c2 = self.generate_start_and_end_country(difficulty)
        self.length = len(shortest_way(c1, c2, R)) - 1
        self.start = c1
        self.goal = c2
        self.current_pos = c1
        self.options = self.image_of(self.current_pos)
    
    def get_info(self):
        dict = {}
        dict["current"] = self.current_pos
        dict["goal"] = self.goal
        dict["options"] = self.options
        dict["steps"] = self.steps
        dict["length"] = self.length
        return dict
        
    def game(self, difficulty):
        while not is_done:
            print("You are here: " + self.current_pos)
            print("Destination: " + self.goal)
            print(image_of(self.relation, self.current_pos))
            
            choice = int(input("Enter number: "))
            xs = list(image_of(self.relation, self.current_pos))
            self.move(self.current_pos, xs[choice])
            is_done = self.is_game_over()
        if self.current_pos == self.goal:
            return True
        else:
            return False
        
    def image_of(self, c):
        return image_of(self.relation, c)
    
    def shortest_way(self):
        return shortest_way(self.start, self.goal, R)



