import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score
import joblib

# Load dataset
df = pd.read_csv(r'C:\Users\Raghu\Downloads\Flask_ML\archive\star_classification.csv')

# Encode target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['class'])

joblib.dump(label_encoder, r'C:\Users\Raghu\Downloads\Flask_ML\models\label_encoder.pkl')

# Prepare features
X = df.drop(columns=['class'], axis=1)

# Split the dataset
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Save the scaler
joblib.dump(scaler, r'C:\Users\Raghu\Downloads\Flask_ML\models\scaler.pkl')

# Define class weights
class_weights = {
    0: df.shape[0] / (3 * (y == 0).sum()),
    1: df.shape[0] / (3 * (y == 1).sum()),
    2: df.shape[0] / (3 * (y == 2).sum())
}

# Train model
model = RandomForestClassifier(class_weight=class_weights, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, r'C:\Users\Raghu\Downloads\Flask_ML\models\model.pkl')

print("Model, scaler, and label encoder saved.")
