#Mean Square Error Calculation
weights = np.random.normal(scale=1/n_features**.5, size=n_features)

#NumPy provides a function that calculates the dot product of two arrays, which conveniently calculates h for us. The dot product multiplies two arrays element-wise, the first element in array 1 is multiplied by the first element in array 2, and so on. Then, each product is summed.

# input to the output layer
output_in = np.dot(weights, inputs)

#update weights by
weights += ...


