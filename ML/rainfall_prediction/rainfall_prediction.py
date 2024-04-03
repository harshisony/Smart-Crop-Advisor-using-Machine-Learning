import pandas as pd
import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the dataset into a dataframe
csv_file = os.path.join(script_dir, 'rainfall_in_india_1901-2015.csv')
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print("Error: CSV file not found at", csv_file)
    sys.exit(1)

# Define a function to predict rainfall for a given district and month
def predict_rainfall(state, month):
    # Filter the dataframe to only include rows with the given district
    state_data = df[df['SUBDIVISION'] == state]

    # Calculate the average rainfall for the given month across all the years
    avg_rainfall = state_data[month].mean()
    
    # Return the predicted rainfall for the given month
    return avg_rainfall

# Get the input parameters as command line arguments
Jregion = sys.argv[1]
Jmonth = sys.argv[2]

#predicted_rainfall = predict_rainfall('ANDAMAN & NICOBAR ISLANDS', 'JAN')

predicted_rainfall = predict_rainfall(Jregion, Jmonth)
print(predicted_rainfall)
