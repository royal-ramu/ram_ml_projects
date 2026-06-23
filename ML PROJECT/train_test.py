
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
from sklearn.metrics import accuracy_score

# Paths
data_path = r"D:\ML PROJECT\data\fertilizer_recommendation_dataset.csv"
save_path = "model/fertilizer_recom.pkl"
os.makedirs("model", exist_ok=True)

# Load data
df = pd.read_csv(data_path)

# Encode categorical columns
soil_encoder = LabelEncoder()
crop_encoder = LabelEncoder()
fertilizer_encoder = LabelEncoder()

df["Soil"] = soil_encoder.fit_transform(df["Soil"])
df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["Fertilizer"] = fertilizer_encoder.fit_transform(df["Fertilizer"])

# Remove unused column
df.drop("Remark",axis=1,inplace=True)

# Split X and y
X = df.drop("Fertilizer",axis=1)
y = df["Fertilizer"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale numeric features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Training Accuracy:", model.score(X_train, y_train) * 100)
print("Test Accuracy:", model.score(X_test, y_test) * 100)

# Save model + scaler + encoders
with open(save_path, "wb") as f:
    pickle.dump({
        "model": model,
        "scaler": scaler,
        "soil_encoder": soil_encoder,
        "crop_encoder": crop_encoder,
        "fertilizer_encoder": fertilizer_encoder
    }, f)

print("Model saved successfully!")
