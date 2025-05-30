import pandas as pd
from urllib.request import urlretrieve
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

#Retrieve Data
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url, 'medical.csv')
medical_df = pd.read_csv('medical.csv')

#gather information
print(medical_df)
medical_df.info()
data_descipription = medical_df.describe()
print(data_descipription)


# seaborn plot stylizers
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] ="#B9B1B100"

#generically plot distributions
# for i in medical_df:
#         fig = px.histogram(medical_df,
#                            x=i,
#                            marginal='box',
#                            title=f'Distribution of {i}')
#         fig.update_layout(bargap=0.1)
#         fig.show()
        

# Plot age data
fig = px.histogram(medical_df, 
                   x='age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()

# plot BMI data
fig = px.histogram(medical_df, 
                   x='bmi',
                   marginal='box',
                   color_discrete_sequence=['red'],
                   title='Distribution of BMI (Body Mass Index)')
fig.update_layout(bargap=0.1)
fig.show()

# plot the charges to evaluate if there are any correltaions
fig = px.histogram(medical_df,
                   x='charges',
                   marginal= 'box',
                   color='smoker',
                   color_discrete_sequence=['green', 'grey'],
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()

#We are itnerested in charges and there seems to be a correlation
#let's loook at smoker data:
medical_df.smoker.value_counts()