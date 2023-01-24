from classes.criterion import Criterion
from classes.decision_maker import DecisionMaker


class CriterionJudgement:
    """Representation of the DM's judgement about the weight of the Criterion"""

    positive_distance = float
    negative_distance = float

    def __init__(
            self,
            criterion: Criterion,
            decision_maker: DecisionMaker,
            max_value: int,
            min_value: int
        ) -> None:
        self.criterion = criterion              # criterion being judged by the DecisionMaker
        self.decision_maker = decision_maker    # DecisionMaker making the judgement
        self.max_value = max_value              # higher value of the fuzzy judgement
        self.min_value = min_value              # lower value of the fuzzy judgement
