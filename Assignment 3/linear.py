import numpy as np
import matplotlib.pyplot as plt
filename = "noisy_18.txt"
data = np.loadtxt(filename)
x = data[:, 0]
y = data[:, 1]
print("Total number of samples:", len(x))
np.random.seed(42)
indices = np.random.permutation(len(x))
x = x[indices]
y = y[indices]
n = len(x)
train_end = int(0.60 * n)
test_end = int(0.80 * n)
x_train = x[:train_end]
y_train = y[:train_end]
x_test = x[train_end:test_end]
y_test = y[train_end:test_end]
x_val = x[test_end:]
y_val = y[test_end:]
print("\nData split:")
print("Training samples   :", len(x_train))
print("Testing samples    :", len(x_test))
print("Validation samples :", len(x_val))
def polynomial_features(x, degree):
    X = np.ones((len(x), degree + 1))
    for j in range(1, degree + 1):
        X[:, j] = X[:, j - 1] * x
    return X
def mse(y_true, y_pred):
    error = y_true - y_pred
    return np.mean(error ** 2)
def pseudo_inverse(X):
    X_T = X.T
    XTX = X_T @ X
    XTX_inverse = np.linalg.inv(XTX)
    X_pseudo = XTX_inverse @ X_T
    return X_pseudo
def train(x, y, degree):
    X = polynomial_features(x,degree)
    X_pseudo = pseudo_inverse(X)
    w = X_pseudo @ y
    return w
def predict(x, w):
    degree = len(w) - 1
    X = polynomial_features(x,degree)
    return X @ w
best_degree = 1
best_test_mse = float("inf")
best_w = None
degrees = []
train_errors = []
test_errors = []
print("\n")
print("POLYNOMIAL DEGREE RESULTS:")
print("{:<10} {:<15} {:<15}".format("Degree","Train MSE","Test MSE"))
print("-" * 60)
for degree in range(1, 10):
    w = train(x_train,y_train,degree)
    X_train = polynomial_features(x_train,degree)
    X_test = polynomial_features(x_test,degree)
    train_pred = X_train @ w
    test_pred = X_test @ w
    train_mse = mse(y_train,train_pred)
    test_mse = mse(y_test,test_pred)
    degrees.append(degree)
    train_errors.append(train_mse)
    test_errors.append(test_mse)
    print("{:<10} {:<15.6f} {:<15.6f}".format(degree,train_mse,test_mse))
    if test_mse < best_test_mse:
        best_test_mse = test_mse
        best_degree = degree
        best_w = w.copy()
print("\n")
print("BEST POLYNOMIAL MODEL")
print("Best degree   :",best_degree)
print("Best test MSE :",best_test_mse)
X_val = polynomial_features(x_val,best_degree)
val_pred = X_val @ best_w
val_mse = mse(y_val,val_pred)
print("\n")
print("VALIDATION RESULTS:")
print("Validation MSE  :",val_mse)
print("\n")
print("LEARNED PARAMETERS:")
for i in range(len(best_w)):
    print("w[{}] = {:.10f}".format(i,best_w[i]))
x_plot = np.linspace(np.min(x),np.max(x),500)
X_plot = polynomial_features(x_plot,best_degree)
y_plot = X_plot @ best_w
plt.figure(figsize=(10, 6))
plt.scatter(x_train,y_train,label="Training data",alpha=0.6)
plt.scatter(x_test,y_test,label="Test data",alpha=0.6)
plt.scatter(x_val,y_val,label="Validation data",alpha=0.6)
plt.plot(x_plot,y_plot,linewidth=2,label="Polynomial fit")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Regression - Degree {}".format(best_degree))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
plt.plot(degrees,train_errors,marker="o",label="Training MSE")
plt.plot(degrees,test_errors,marker="o",label="Test MSE")
plt.xlabel("Polynomial Degree")
plt.ylabel("MSE")
plt.title("MSE vs Polynomial Degree")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()