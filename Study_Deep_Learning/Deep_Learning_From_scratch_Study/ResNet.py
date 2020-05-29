from keras.models import Sequential
from keras.layers.convolutional import Conv2D, ZeroPadding2D, AveragePooling2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers import BatchNormalization, concatenate, Input
from keras.models import Model
from keras.layers import Dropout
from keras import backend as K
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)


class ResNet:

    @staticmethod
    def residual_module(data, num_filter, stride, red=False, bnEps=2e-5, bnMom=0.9):
        # red: A boolean indicating whether or not we should apply an additional residual module to reduce the spatial dimensions of the volume
        #       (This downsampling is done in between stages.)
        # bnEps: The epsilon value of batch normalization used to prevent division by zero errors.
        # bnMon: The momentum of the batch normalization which serves as how much "rolling average" is kept.

        shortcut = data
        bn1 = BatchNormalization(epsilon=bnEps, momentum=bnMom)(shortcut)
        act1 = Activation("relu")(bn1)
        conv1 = Conv2D(int(num_filter * 0.25), kernel_size=(1, 1), strides=(1, 1), use_bias=False)(act1)

        bn2 = BatchNormalization(epsilon=bnEps, momentum=bnMom)(conv1)
        act2 = Activation("relu")(bn2)
        pad2 = ZeroPadding2D(padding=(1, 1))(act2)
        conv2 = Conv2D(int(num_filter * 0.25), kernel_size=(3, 3), strides=stride, use_bias=False)(pad2)

        bn3 = BatchNormalization(epsilon=bnEps, momentum=bnMom)(conv2)
        act3 = Activation("relu")(bn3)
        conv3 = Conv2D(num_filter, kernel_size=(1, 1), strides=(1, 1), use_bias=False)(act3)

        if red:
            shortcut = Conv2D(num_filter, kernel_size=(1, 1), strides=stride, use_bias=False)(conv1)

        add = conv3 + shortcut

        return add


    @staticmethod
    def build(width, height, depth, classes):

        inputShape = (height, width, depth)

        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        stages = (3, 4, 6 , 3)
        filters = (64, 256, 512, 1024, 2048)

        input = Input(shape=inputShape)
        bn1_1 = BatchNormalization(epsilon=2e-5, momentum=0.9)(input)
        pad1_1 = ZeroPadding2D(padding=(3, 3))(bn1_1)
        conv1_1 = Conv2D(kernel_size=(7, 7), strides=(2, 2), filters=filters[0], use_bias=False)(pad1_1)

        bn1_2 = BatchNormalization(epsilon=2e-5, momentum=0.9)(conv1_1)
        act1_2 = Activation('relu')(bn1_2)
        pad1_2 = ZeroPadding2D(padding=(1, 1))(act1_2)
        pool1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(pad1_2)
        body = pool1

        for i in range(0, len(stages)):
            stride = (1, 1) if i == 0 else (2, 2)
            body = ResNet.residual_module(body, filters[i + 1], stride, red=True)

            for j in range(0, stages[i] - 1):
                body = ResNet.residual_module(body, filters[i+1], (1, 1))

        print(body.shape)

        bn2_1 = BatchNormalization(epsilon=2e-5, momentum=0.9)(body)
        act2_1 = Activation('relu')(bn2_1)

        flatten = Flatten()(act2_1)
        dp = Dropout(0.5)(flatten)
        fc1 = Dense(classes)(dp)
        act = Activation('softmax')(fc1)

        resnet = Model(inputs=input, outputs=act)

        return resnet