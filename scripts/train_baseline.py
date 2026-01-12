import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


# Load dataset
df = pd.read_csv("data/raw/sessions.csv")

# Separate features and label
X = df.drop(columns=["label"])
y = df["label"]

# Train test split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42,stratify=y)

# Train baseline model
model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)
# Evaluation
print("Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report: ")
print(classification_report(y_test,y_pred))