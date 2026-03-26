import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


data = pd.read_csv("data.csv")

X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = LogisticRegression()
model.fit(X_train, y_train)


with open("loan_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained!")