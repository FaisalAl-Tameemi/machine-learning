import numpy as np
import pandas as pd

# RMS Titanic data visualization code
from titanic_visualizations import survival_stats
from IPython.display import display
# %matplotlib inline
def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

    else:
        return "Number of predictions does not match number of outcomes!"

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

# Print the first few entries of the RMS Titanic data
display(data.head())
# survival_stats(data, outcomes, 'Sex')
