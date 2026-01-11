class DigitalTwin:
    def __init__(self, efficacy_model, toxicity_model, fusion_model):
        self.efficacy_model = efficacy_model
        self.toxicity_model = toxicity_model
        self.fusion_model = fusion_model

    def simulate(self, X):
        eff = self.efficacy_model.predict(X)
        tox = self.toxicity_model.predict(X)
        score = self.fusion_model.compute_score(eff, tox)

        return {
            "efficacy": eff,
            "toxicity": tox,
            "risk_benefit_score": score
        }

