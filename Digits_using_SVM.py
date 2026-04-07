# Import required libraries
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load handwritten digits dataset
digits = load_digits()

# Features and target
X = digits.data
y = digits.target

# Optional: View dataset information
print("Dataset Shape:", X.shape)
print("Number of Classes:", len(set(y)))
print("Classes:", set(y))

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Different kernels to test
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

# Store results
results = []

# Train and evaluate SVM with different kernels
for kernel in kernels:
    print("\n" + "="*50)
    print(f"SVM with {kernel} kernel")
    print("="*50)

    # Create model
    model = SVC(kernel=kernel)

    # Train model
    model.fit(X_train, y_train)

    # Make