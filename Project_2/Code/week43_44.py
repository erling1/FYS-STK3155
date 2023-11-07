
import numpy as np
import jax.numpy as jnp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from NN import FFNN
from scheduler import Constant, Adam
from funcs import CostCrossEntropy, sigmoid, CostLogReg
from copy import copy
from sklearn.model_selection import train_test_split
# from sklearn.neural_network import MLPClassifier
# import tensorflow as tf

eta = 0.1
rho = 0.9
rho2 = 0.999
scheduler = Constant(eta)
scheduler = Adam(eta, rho, rho2)

X = np.array([[0,0,1,1],[0,1,0,1]]).T

t_XOR = np.array([0,1,1,0], dtype=float)
t_AND = np.array([0,0,0,1], dtype=float)
t_OR = np.array([0,1,1,1], dtype=float)
t_XOR = np.c_[t_XOR]
t_AND = np.c_[t_AND]
t_OR = np.c_[t_OR]

X_train, X_val, t_train, t_val = train_test_split(X, t_XOR, test_size=0.2)

dim = (2, 5, 1)
Neural = FFNN(dim, hidden_act=sigmoid, output_act=sigmoid, cost_func=CostLogReg, seed=100, classification=True)

scores = Neural.train(X_train, t_train, scheduler, epochs=100, X_val=X_val, t_val=t_val)

output = Neural.predict(X)
print("After backpropagation")
print(output)

# print("Scores")
df = pd.DataFrame(scores)
print(scores)
# epochs = np.arange(len(scores["train_errors"]))
# plt.plot(epochs, scores["train_errors"])
# plt.show()

# err0 = scores["train_errors"][0]
# err1 = scores["train_errors"][-1]
# costf = CostCrossEntropy(t_XOR)
# cost = costf(output)
# print(f"cost = {cost}")
# print(f"err0 = {err0} ; err1 = {err1}")

# # With scikit-learn
# t_XOR = np.array([0,1,1,0], dtype=float)
# clf = MLPClassifier(solver="sgd", alpha=0, hidden_layer_sizes=(2), random_state=1)
# clf.fit(X, t_XOR)
# output = clf.predict_proba(X)
# print("Scikit-learn")
# print(output)

# # With tensorflow
# model = tf.keras.Sequential()
# model.add(tf.keras.Input(shape=(2,)))
# model.add(tf.keras.layers.Dense(2))
# model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# model.compile(optimizer="adam", loss=tf.keras.losses.BinaryCrossentropy())
# model.fit(X, t_XOR, epochs=100)
# pred = model.predict(X)

# print("Tensorflow")
# print(pred)