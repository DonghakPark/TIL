"""
This Contents is about MNIST from Tensorflow Official Tutorial
url : https://www.tensorflow.org/tutorials/quickstart/beginner
All of the codes are from the url above.
"""

import tensorflow as tf  # Import Tensorflow Library

# Load MNIST Dataset
MNIST = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = MNIST.load_data()

# Normalize the data
# MNIST is Image Data, so it is 0~255
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),  # Flatten the data
        tf.keras.layers.Dense(128, activation="relu"),  # Dense Layer
        tf.keras.layers.Dropout(0.2),  # Dropout Layer
        tf.keras.layers.Dense(10, activation="softmax"),  # Output Layer
    ]
)

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
# epochs : How many times the model will be trained
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
# verbose : 0, 1, 2
# verbose mean how much information will be shown
model.evaluate(x_test, y_test, verbose=2)
