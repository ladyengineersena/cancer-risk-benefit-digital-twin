class RiskBenefitFusion:
    def __init__(self, alpha=0.7, beta=0.3):
        self.alpha = alpha
        self.beta = beta

    def compute_score(self, efficacy, toxicity):
        return self.alpha * efficacy - self.beta * toxicity

