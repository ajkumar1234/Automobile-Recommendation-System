import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# Load data
df = pd.read_csv("C:\Users\PC\Downloads\Automobile_data.csv")  # try to retrieve the data by using the path address

# Encode fuel type (feature)
fuel_encoder = LabelEncoder()
df["fuel_type"] = fuel_encoder.fit_transform(df["fuel_type"])

# Combine brand & model as single target
df["target"] = df["brand"] + "_" + df["model"]

target_encoder = LabelEncoder()
df["target"] = target_encoder.fit_transform(df["target"])

# Features & target
X = df[["price", "fuel_type"]]
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Prediction function
def predict_car(price, fuel):
    fuel_encoded = fuel_encoder.transform([fuel])[0]
    prediction = model.predict([[price, fuel_encoded]])
    result = target_encoder.inverse_transform(prediction)[0]
    brand, model_name = result.split("_")
    return brand, model_name
