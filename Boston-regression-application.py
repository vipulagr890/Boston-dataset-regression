#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
regr = LinearRegression() 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, mean_squared_error, r2_score


# In[2]:


boston_dataset = load_boston()


# In[3]:


data = pd.DataFrame(data = boston_dataset.data, columns = boston_dataset.feature_names)


# In[4]:


data = data.drop(['INDUS','AGE'], axis = 1)


# In[5]:


price = np.log(boston_dataset.target)


# In[6]:


train_x, test_x, train_y,test_y = train_test_split(data, price, test_size = 0.3, random_state = 0)


# In[7]:


regr.fit(train_x, train_y)


# In[8]:


y_pred = regr.predict(test_x)


# In[9]:


log_mse = mean_squared_error(test_y,y_pred)


# In[10]:


log_rmse = np.sqrt(log_mse)


# In[11]:


log_score = r2_score(test_y,y_pred)


# In[12]:


input("Press Enter to start the program ")


# In[13]:


#CRIM	ZN	CHAS	NOX	RM	DIS	RAD	TAX	PTRATIO	B	LSTAT
def get_prediction_data(CHAS,RM,PTRATIO):
    x = data.mean()
    x[2] = CHAS
    x[4] = RM
    x[8] = PTRATIO
    print(x)
    return regr.predict([x])[0]


# In[14]:


while True:
    print("Enter 0 or 1 for Charles River value : ")
    CHAS = int(input())
    if ((CHAS < 0) or (CHAS > 1)):
        print('Please enter 0 or 1.')
        continue
    break
    
while True:
    print("Enter no. of rooms : ")
    print("('Values will be converted to Integer automatically)'")
    RM = int(input())
    if (RM <= 0):
        print('Number of Rooms should be more than 0.')
        continue
    break

while True:
    print("Enter no. of pupil-teacher ratio : ")
    print("('Values will be converted to Integer automatically)'")
    PTRATIO = int(input())
    if (PTRATIO < 0):
        print("pupil to teachers ratio should be more than 1.")
        continue
    break

house_price = get_prediction_data(CHAS,RM,PTRATIO)
print("log house price is : {0}".format(house_price *1000))


# In[15]:


type(PTRATIO)


# In[16]:


#bounds 
upper_bound =  np.log(28.529) + 2*log_rmse
print("upper_bound is for house price is : {0} ".format(upper_bound * 1000))


# In[17]:


lower_bound = np.log(28.529) - 2*log_rmse
lower_bound * 27.51
print("lower bound is for house price is: {0}".format(lower_bound * 1000))


# In[18]:


actual_price = np.e**house_price * 1000 
print("actual price is 1980's: {0} $".format(int(actual_price)))
print("actual price in 2020's : {0} $".format(int(actual_price * 27.51)))


# In[19]:


input("press enter to exit the program")


# In[ ]:





# In[ ]:




