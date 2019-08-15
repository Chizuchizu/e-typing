import matplotlib.pyplot as plt
import numpy as np


def byoga(number):
    score = np.load("score_" + number + ".npy").astype(int)

    plt.rcParams["font.size"] = 25

    plt.figure(figsize=(15, 10))
    plt.hist(score.astype(int), bins=30)
    plt.xlabel("score")
    plt.ylabel("frequency")
    plt.title("No." + number + " e-typing ranking")
    plt.show()
