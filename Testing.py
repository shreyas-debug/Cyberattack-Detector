# Step 1 Load Data
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dataset = pd.read_csv('encryption.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,1].values

# Step 2: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, 
                                                    random_state=0)
# Step 3: Fit Simple Linear Regression to Training Data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 4: Make Prediction
y_pred = regressor.predict(X_test)

# Step 5 - Visualize training and testing set results
fig = plt.figure()
ax = fig.subplots()
# plot the regression line
ax.plot(X_train, regressor.predict(X_train),color = 'g', alpha = 0.9)
# plot the actual data points of training set
ax.scatter(X_train,y_train,s = 10, color = 'b', label = 'Training Set')
# plot the actual data points of test set
ax.scatter(X_test,y_test,s = 10, color = 'r', label = 'Test Set')
ax.set_title('Data Vs Encryption')
ax.legend()
plt.xlabel('Data Units')
plt.ylabel('Encryption Level')
plt.show()

# Step 6 - Make new prediction
Encryption_level_pred = regressor.predict([[5]])
print('The predicted encryption level for certain units is: ',
      Encryption_level_pred)
if(Encryption_level_pred > 0.4):
    {print("Error not detected system is safe")}
else:
    print("Error has been detected")