import numpy as np
import matplotlib.pyplot as plt

X_train=np.array([1,2,3,4])
y_train=np.array([2,4,6,8])

X_test=np.array([5])
y_test=np.array([10])

m = np.sum((X_train - X_train.mean()) * (y_train - y_train.mean())) / np.sum(
    (X_train - X_train.mean()) ** 2
)

b = y_train.mean() - m * X_train.mean()

# Make prediction
y_pred = m * X_test + b

# Calculate MSE
mse = np.mean((y_test - y_pred) ** 2)

print("Slope:", m)
print("Intercept:", b)
print("Actual value:", y_test[0])
print("Predicted value:", y_pred[0])
print("MSE:", mse)

# Create regression line
X_line = np.linspace(1, 5, 100)
y_line = m * X_line + b

# Plot training data
plt.scatter(X_train, y_train, label="Training data")

# Plot test data
plt.scatter(X_test, y_test, label="Test data")

# Plot regression line
plt.plot(X_line, y_line, label="Regression line")

plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show()

