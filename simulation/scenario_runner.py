import pandas as pd
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.efficacy_model import EfficacyModel
from models.toxicity_model import ToxicityModel
from models.fusion_model import RiskBenefitFusion
from simulation.digital_twin import DigitalTwin

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "sample_data.csv")
data = pd.read_csv(data_path)

features = data[[
    "tumor_growth_rate",
    "tumor_stage",
    "treatment_intensity",
    "patient_resilience"
]]

eff_model = EfficacyModel()
tox_model = ToxicityModel()

eff_model.train(features, data["response"])
tox_model.train(features, data["toxicity"])

fusion = RiskBenefitFusion(alpha=0.6, beta=0.4)
twin = DigitalTwin(eff_model, tox_model, fusion)

results = twin.simulate(features.head(10))
print(results)

