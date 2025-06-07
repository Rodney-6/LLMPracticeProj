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
px.histogram(medical_df, x='smoker', color='sex', title='Smoker')


#haven't looked at age as it relates to charges yet and that could intuitievly be very interesting
fig = px.scatter(medical_df, 
                 x='age', 
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='Age vs. Charges')
fig.update_traces(marker_size=5)
fig.show()

#now check BMI against the charges
fig = px.scatter(medical_df, 
                 x='bmi',
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show()


years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)');

cherries = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1]
plt.plot(years, apples)
plt.plot(years, cherries)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Cherries']);