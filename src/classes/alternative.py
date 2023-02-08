class Alternative:
    
    total_distance_positive = int;
    total_distance_negative = int;
    score = float;
    ranking_position = int;
    
    def __init__(self, name, weight):
      self.name = name
      self.weight = weight 

    def score_calculation(self):
       pass 