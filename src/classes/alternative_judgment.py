from classes.alternative import Alternative
from classes.criterion import Criterion
from classes.decision_maker import DecisionMaker


class AlternativeJudgment:

    def __init__(
        self,
        alternative: Alternative,
        decision_makers: list[DecisionMaker],
        criterion: Criterion,
        max_value: int,
        min_value: int
    ):
        self.alternative = alternative
        self. decision_makers = decision_makers,
        self.criterion = criterion,
        self.max_value = max_value,
        self.min_value = min_value
