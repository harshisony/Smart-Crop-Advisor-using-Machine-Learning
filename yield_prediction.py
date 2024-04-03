import pandas as pd
import numpy as np
import json
import os
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the dataset into a dataframe
csv_file = os.path.join(script_dir, 'crop_production_karnataka.csv')
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print("Error: CSV file not found at", csv_file)
    sys.exit(1)
# Drop the Crop_Year column
df = df.drop(['Crop_Year'], axis=1)

# Separate the features and target variables
X = df.drop(['Production'], axis=1)
y = df['Production']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Categorical columns for one-hot encoding
categorical_cols = ['State_Name', 'District_Name', 'Season', 'Crop']

# One-hot encode the categorical columns
ohe = OneHotEncoder(handle_unknown='ignore')
ohe.fit(X_train[categorical_cols])

# Convert categorical columns to one-hot encoding
X_train_categorical = ohe.transform(X_train[categorical_cols])
X_test_categorical = ohe.transform(X_test[categorical_cols])

# Combine the one-hot encoded categorical columns and numerical columns
X_train_final = np.hstack((X_train_categorical.toarray(), X_train.drop(categorical_cols, axis=1)))
X_test_final = np.hstack((X_test_categorical.toarray(), X_test.drop(categorical_cols, axis=1)))

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_final, y_train)

# Get the input parameters as command line arguments
Jstate = sys.argv[1]
Jdistrict = sys.argv[2]
Jseason = sys.argv[3]
Jcrops = sys.argv[4]
Jarea = sys.argv[5]

# Get the user inputs and store them in a numpy array
user_input = np.array([[Jstate, Jdistrict, Jseason, Jcrops, Jarea]])

# Convert the categorical columns to one-hot encoding
user_input_categorical = ohe.transform(user_input[:, :4])

# Combine the one-hot encoded categorical columns and numerical columns
user_input_final = np.hstack((user_input_categorical.toarray(), user_input[:, 4:].astype(float)))

# Make the prediction
prediction = model.predict(user_input_final)

# Evaluate the model on the test set
y_pred_test = model.predict(X_test_final)

# Calculate accuracy using a threshold
threshold = 0.1  # You can adjust this threshold as needed
correct_predictions = np.sum(np.abs(y_pred_test - y_test) < threshold)
total_samples = len(y_test)
accuracy = correct_predictions / total_samples

# Print accuracy
#print(f'Accuracy: {accuracy * 100:.2f}')

# Return the prediction as a string
print(f'{prediction[0]}')
