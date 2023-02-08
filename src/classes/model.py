from criterion import Criterion
from criterion_judgment import CriterionJudgment
from decision_maker import DecisionMaker

# from enumerations.five_linguistic_terms import FiveLinguisticTerms
# from enumerations.seven_linguistic_terms import SevenLinguisticTerms

class Model:
    def __init__(
        self,
        number_of_terms: int,
        criteria: list[Criterion],
        criterion_judgement: list[CriterionJudgment],
        decision_maker: list[DecisionMaker]
    ) -> None:
        self.number_of_terms = number_of_terms
        self.criteria = criteria
        self.criterion_judgement = criterion_judgement
        self.decision_maker = decision_maker

    def sum_positive_criterion_distance(self):
        pass

    def sum_negative_criterion_distance(self):
        pass

    def calculate_normalized_weight(self):
        pass

    def sum_positive_alternative_distance(self):
        pass

    def sum_negative_alternative_distance(self):
        pass

    def define_alternative_ranking(self):
        pass
