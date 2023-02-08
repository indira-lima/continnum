from classes.alternative_judgment import AlternativeJudgment
from classes.aggregated_judgment import AggregatedJudgment
from enumerations.criterion_type import CriterionType

class Criterion:
    """Representation of the Criteria used to judge Alternatives in the Model"""
    total_positive_distance = 0  # distance of this criterion to the positive ideal
    total_negative_distance = 0  # distance of this criterion to the negative ideal
    unnormalized_weight = 0      # unnormalized weight
    normalized_weight = 0        # weight (level of importance) of the criterion

    unnormalized_distance = 0    
    normalized_distance = 0      
    
    alternative_judgments: list[AlternativeJudgment]
    aggregated_judgments: list[AggregatedJudgment]

    positive_ideal_solution_max = int               # higher value of the positive ideal solution
    positive_ideal_solution_min = int               # lower value of the positive ideal solution
 
    negative_ideal_solution_max = int               # higher value of the negative ideal solution
    negative_ideal_solution_min = int               # lower value of the negative ideal solution

    def __init__(
        self,
        description: str,
        criterion_type: CriterionType
    ) -> None:
        """Initializes a Criterion with it's type and description"""
        self.description = description
        self.criterion_type = criterion_type

    def calculate_unnormalized_weight(self):
        """Calculates the unnormalized weight by dividing the negative distance by the sum of the distances"""
        self.unnormalized_weight = self.total_negative_distance / (self.total_negative_distance + self.total_positive_distance) 

    def find_sp_by_alternative(self):
        pass

    def find_sq_by_alternative(self):
        pass

    def generate_aggregated_judgment_table(self):
        pass

    def find_positive_solution(self):
        pass

    def find_negative_solution(self):
        pass
