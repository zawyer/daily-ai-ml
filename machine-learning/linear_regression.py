import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate slope (m)
m = np.sum((X - X.mean()) * (y - y.mean())) / np.sum((X - X.mean()) ** 2)

# Calculate intercept (b)
b = y.mean() - m * X.mean()

# Predictions
y_pred = m * X + b

# Mean Squared Error
mse = np.mean((y - y_pred) ** 2)

# Predict a new value
x_new = 6
prediction = m * x_new + b

print("Slope:", m)
print("Intercept:", b)
print("MSE:", mse)
print("Prediction for x =", x_new, ":", prediction)

