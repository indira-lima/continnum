from enumerations.criterion_type import CriterionType

class Criterion:
    """Representation of the Criteria used to judge Alternatives in the Model"""
    total_positive_distance = 0  # distance of this criterion to the positive ideal
    total_negative_distance = 0  # distance of this criterion to the negative ideal
    unnormalized_weight = 0      # unnormalized weight
    normalized_weight = 0        # weight (level of importance) of the criterion

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
