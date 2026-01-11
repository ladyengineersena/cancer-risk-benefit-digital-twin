import numpy as np

def risk_benefit_summary(scores):
    return {
        "mean": np.mean(scores),
        "max": np.max(scores),
        "min": np.min(scores)
    }

