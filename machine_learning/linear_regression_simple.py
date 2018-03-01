from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

reg = linear_model.LinearRegression()
#Parameters:training data and expected values
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# Make predictions using the testing set
y_pred = reg.predict([[5, 5], [7, 7]])

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error([5,7], y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score([5,7], y_pred))