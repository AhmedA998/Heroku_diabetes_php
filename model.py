#Import Libraries
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import pickle

warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"

#----------------------------------------------------


# drawing confusion matrix
sns.heatmap(CM, center = True)
plt.show()



pickle.dump(GaussianNBModel, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))



