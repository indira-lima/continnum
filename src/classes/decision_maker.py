from classes.criterion_judgement import CriterionJudgement


class DecisionMaker:
    """Representation of a Decision Maker (DM) person who apply judgements into the Model"""
    criterion_judgements = list[CriterionJudgement] # list of criterion judgements made by this DM
  
    positive_ideal_solution_max = int               # higher value of the positive ideal solution according to this DM
    positive_ideal_solution_min = int               # lower value of the positive ideal solution according to this DM
 
    negative_ideal_solution_max = int               # higher value of the negative ideal solution according to this DM
    negative_ideal_solution_min = int               # lower value of the negative ideal solution according to this DM

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        
