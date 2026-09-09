import numpy as np

# Training data
X_train = np.array([1, 2, 3, 4])
y_train = np.array([2, 4, 6, 8])

# Test data
X_test = np.array([5])
y_test = np.array([10])

# Learn from training data
m = np.sum((X_train - X_train.mean()) * (y_train - y_train.mean())) / np.sum((X_train - X_train.mean()) ** 2)
b = y_train.mean() - m * X_train.mean()

# Make prediction on test data
y_pred = m * X_test + b

# Calculate MSE
mse = np.mean((y_test - y_pred) ** 2)

print("Slope:", m)
print("Intercept:", b)
print("Actual value:", y_test[0])
print("Predicted value:", y_pred[0])
print("MSE:", mse)
