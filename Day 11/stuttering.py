from random import randint
import numpy as np
import matplotlib.pyplot as plt

# function to roll a specified die
def dice_roller(numDie):
    return randint(1,numDie)

# generate data for rolling a d20
def generate_data():
    data = []
    for i in range(100):
        data.append(dice_roller(20))
    return data

def histogram(data):
    plt.hist(data,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],rwidth=0.9)
    plt.show()

def expected_value(outcomes, weights):
    values = np.asarray(outcomes)
    weights = np.asarray(weights)
    return (values * weights).sum() / weights.sum()


def probability():
    probs = [.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05]
    values = []
    for i in range(1,21):
        values.append(i)
    return expected_value(values,probs)


if __name__ == "__main__":
    histogram(generate_data())
    print(probability())