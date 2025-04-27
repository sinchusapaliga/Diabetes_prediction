from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)


df = pd.read_csv("Data.csv")
x = df.drop(columns="Outcome", axis=1)
y = df["Outcome"]

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x_scaled, y, test_size=0.25, stratify=y, random_state=42
)


classifier = svm.SVC(kernel="linear", C=1.0)
classifier.fit(x_train, y_train)


train_predictions = classifier.predict(x_train)
train_accuracy = accuracy_score(y_train, train_predictions)
print("Training Data Accuracy:", train_accuracy)

test_predictions = classifier.predict(x_test)
test_accuracy = accuracy_score(y_test, test_predictions)
print("Test Data Accuracy:", test_accuracy)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = [
            float(request.form["Pregnancies"]),
            float(request.form["Glucose"]),
            float(request.form["BloodPressure"]),
            float(request.form["SkinThickness"]),
            float(request.form["Insulin"]),
            float(request.form["BMI"]),
            float(request.form["DiabetesPedigreeFunction"]),
            float(request.form["Age"]),
        ]

        input_data_np = np.array(input_data).reshape(1, -1)
        normalized_data = scaler.transform(input_data_np)
        prediction = classifier.predict(normalized_data)

        if prediction[0] == 0:
            return "The person is not diabetic"
        else:
            return "The person is diabetic"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
