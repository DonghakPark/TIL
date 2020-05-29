from keras.models import Sequential
from keras.layers.convolutional import Conv2D, ZeroPadding2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers import BatchNormalization
from keras.layers import Dropout
from keras import backend as K
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)


class AlexNet:

    @staticmethod
    def build(width, height, depth, classes):

        model = Sequential()
        inputShape = (height, width, depth)

        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        # Conv 1-1
        model.add(Conv2D(filters=32, kernel_size=(11, 11), input_shape=inputShape, padding="same"))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        # Conv 2-1
        model.add(Conv2D(filters=64, kernel_size=(5, 5), padding="same"))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        # Conv 3-1
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding="same"))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))


        # Conv 3-2
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding="same"))
        model.add(BatchNormalization())
        model.add(Activation("relu"))


        # Conv 3-3
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding="same"))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        # Fully-Connected
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(Dropout(0.5))

        model.add(Dense(512))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(Dropout(0.5))

        model.add(Dense(classes))
        model.add(BatchNormalization())
        model.add(Activation("softmax"))

        return model