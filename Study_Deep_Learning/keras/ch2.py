import tensorflow as tf
import keras
import numpy as np


(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
train_images = train_images.reshape((60000,28*28))/ 255
train_labels = train_labels.astype("float32")
test_images = test_images.reshape((10000,28*28))/ 255
test_labels = test_labels.astype("float32")

model = keras.Sequential([
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam",
              loss = keras.losses.sparse_categorical_crossentropy,
              metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=100, batch_size=128)

predicts = model(test_images)
predicts = predicts.numpy()
predicts_labels = np.argmax(predicts, axis=1)
print(predicts_labels.shape)
matches = predicts_labels == test_labels
print(f"Acc : {matches.mean():.2f}")
