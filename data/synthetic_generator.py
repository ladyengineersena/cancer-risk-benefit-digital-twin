import numpy as np
import pandas as pd
import os

def generate_synthetic_data(n=500):
    np.random.seed(42)

    data = pd.DataFrame({
        "tumor_growth_rate": np.random.uniform(0.1, 1.0, n),
        "tumor_stage": np.random.randint(1, 5, n),
        "treatment_intensity": np.random.uniform(0.2, 1.0, n),
        "patient_resilience": np.random.uniform(0.3, 1.0, n),
    })

    data["response"] = (
        data["treatment_intensity"] * data["patient_resilience"]
        - data["tumor_growth_rate"] * 0.4
        + np.random.normal(0, 0.05, n)
    ).clip(0, 1)

    data["toxicity"] = (
        data["treatment_intensity"] * (1 - data["patient_resilience"])
        + np.random.normal(0, 0.05, n)
    ).clip(0, 1)

    return data

if __name__ == "__main__":
    df = generate_synthetic_data()
    # Write to the data directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "sample_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Generated sample data with {len(df)} samples: {output_path}")

