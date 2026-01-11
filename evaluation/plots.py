import matplotlib.pyplot as plt

def plot_tradeoff(efficacy, toxicity):
    plt.scatter(toxicity, efficacy)
    plt.xlabel("Toxicity Risk")
    plt.ylabel("Treatment Benefit")
    plt.title("Risk–Benefit Trade-off")
    plt.show()

