import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate the slope and intercept
m = np.sum((X - X.mean()) * (y - y.mean())) / np.sum((X - X.mean()) ** 2)
b = y.mean() - m * X.mean()

# Make a prediction
x_new = 6
prediction = m * x_new + b

print("Slope:", m)
print("Intercept:", b)
print("Prediction for x =", x_new, ":", prediction)
