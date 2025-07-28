from sklearn.linear_model import LinearRegression

# Simple example: Predict y from x
# sklearn - scikit-learn which requires 2 D to work so x input is 2D
x = [[1], [2], [3]]
y = [2, 4, 6]

model = LinearRegression()
model.fit(x, y)

print(model.predict([[4]]))  # y = 2 × x model predict give data



