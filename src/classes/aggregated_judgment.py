from classes.criterion import Criterion
from classes.alternative import Alternative

class AggregatedJudgment:

    sp = int;
    sq = int;
    positive_distance = float;
    negative_distance = float;
    
    def __init__(self, alternative: Alternative, criterion: Criterion):
      self.alternative = alternative
      self.criterion = criterion
