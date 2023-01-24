from criterion import Criterion
from criterion_judgement import CriterionJudgement
from decision_maker import DecisionMaker

from enumerations.five_linguistic_terms import FiveLinguisticTerms
from enumerations.seven_linguistic_terms import SevenLinguisticTerms

class Model:
    def __init__(
        self,
        linguistic_terms: FiveLinguisticTerms,
        criteria: list[Criterion],
        criterion_judgement: list[CriterionJudgement],
        decision_maker: list[DecisionMaker]
    ) -> None:
        self.linguistic_terms = linguistic_terms
        self.criteria = criteria
        self.criterion_judgement = criterion_judgement
        self.decision_maker = decision_maker
