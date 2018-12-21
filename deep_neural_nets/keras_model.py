from keras import Sequential
from keras.layers import Dense


# Get number of features
n_cols = X.shape[1]

# model instance
model = Sequential()

# Input layer, hidden layers and output layer creation
model.add(Dense(20, input_shape=(n_cols, )))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='softmax'))


''' What we will need now is to compile and fit the model '''
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y)