from keras import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping


'''
In this first section we create a Deep neural net like we did
earlier then we will tune the learning rate hyper-parameter.
'''

def new_model():
	'''
	Since we will be fitting a model each time, let's factor code in a function.
	This function create a deep learning model.
	'''
	# Get number of features
	n_cols = X.shape[1]

	# model instance
	model = Sequential()

	# Input layer, hidden layers and output layer creation
	model.add(Dense(20, input_shape=(n_cols, )))
	model.add(Dense(20, activation='relu'))
	model.add(Dense(20, activation='relu'))
	model.add(Dense(2, activation='softmax'))

# Early stopping.
early_stopping = EarlyStopping(patience=2)

################ Tuning ##################

# Create list of learning rates.
lr_values = [.0001, .001, .01, .1, 1]

# Loop over learning rates
for lr in lr_values:
	print('\nTesting model with learning rate: %f\n'%lr )

	# Build new model to test, unaffected by previous models
	model = new_model()

	# Create SGD optimizer with specified learning rate.
	my_optimizer = SGD(lr=lr)

	# Compile the model
	model.compile(optimizer=my_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

	# Fit the model
	model.fit(X, y, validation_split=.25, epochs=20, callbacks=[early_stopping])