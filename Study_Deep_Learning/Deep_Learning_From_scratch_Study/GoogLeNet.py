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


class GoogLeNet:


    @staticmethod
    def conv_module(data, num_filter, kernel_size, pad="same", stride=(1, 1)):
        conv = Conv2D(filters=num_filter, kernel_size=kernel_size, padding=pad, strides=stride)(data)
        bn = BatchNormalization()(conv)
        act = Activation('relu')(bn)

        return act

    @staticmethod
    def inception_module(data, num1x1, num3x3reduce, num3x3, num5x5reduce, num5x5, num1x1Proj):
        conv_1x1 = GoogLeNet.conv_module(data, num1x1, (1, 1))
        conv_r3x3 = GoogLeNet.conv_module(data, num3x3reduce, (1, 1))
        conv_3x3 = GoogLeNet.conv_module(conv_r3x3, num3x3, (3, 3))
        conv_r5x5 = GoogLeNet.conv_module(data, num5x5reduce, (1, 1))
        conv_5x5 = GoogLeNet.conv_module(conv_r5x5, num5x5, (5, 5))
        pool = MaxPooling2D(padding="same", pool_size=(3, 3), strides=(1, 1))(data)
        conv_proj = GoogLeNet.conv_module(pool, num1x1Proj, (1, 1))
        concat = concatenate([conv_1x1, conv_3x3, conv_5x5, conv_proj])

        return concat


    @staticmethod
    def build(width, height, depth, classes):

        inputShape = (height, width, depth)

        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        input = Input(shape=inputShape)

        input_pad = ZeroPadding2D(padding=(3, 3))(input)
        conv1_1 = GoogLeNet.conv_module(input_pad, 64, (7, 7), stride=(2, 2))
        pad1_1 = ZeroPadding2D(padding=(1, 1))(conv1_1)
        pool1 = MaxPooling2D(padding="same", pool_size=(3, 3), strides=(2, 2))(pad1_1)

        conv1_2 = GoogLeNet.conv_module(pool1, 64, (1, 1))
        pad1_2 = ZeroPadding2D(padding=(1, 1))(conv1_2)

        conv1_3 = GoogLeNet.conv_module(pad1_2, 192, (3, 3))
        pad1_3 = ZeroPadding2D(padding=(1, 1))(conv1_3)
        pool2 = MaxPooling2D(padding="same", pool_size=(3, 3), strides=(2, 2))(pad1_3)

        in2a = GoogLeNet.inception_module(pool2, 64, 96, 128, 16, 32, 32)
        in2b = GoogLeNet.inception_module(in2a, 128, 128, 192, 32, 96, 64)
        pad2_1 = ZeroPadding2D(padding=(1, 1))(in2b)
        pool3 = MaxPooling2D(padding="same", pool_size=(3, 3), strides=(2, 2))(pad2_1)

        in3a = GoogLeNet.inception_module(pool3, 192, 96, 208, 16, 48, 64)
        in3b = GoogLeNet.inception_module(in3a, 160, 112, 224, 24, 64, 64)
        in3c = GoogLeNet.inception_module(in3b, 128, 128, 256, 24, 64, 64)
        in3d = GoogLeNet.inception_module(in3c, 112, 144, 288, 32, 64, 64)
        in3e = GoogLeNet.inception_module(in3d, 256, 160, 320, 32, 128, 128)
        pad3_1 = ZeroPadding2D(padding=(1, 1))(in3e)
        pool4 = MaxPooling2D(padding="same", pool_size=(3, 3), strides=(2, 2))(pad3_1)

        in4a = GoogLeNet.inception_module(pool4, 256, 160, 320, 32, 128, 128)
        in4b = GoogLeNet.inception_module(in4a, 384, 192, 384, 48, 128, 128)
        pool5 = AveragePooling2D(pool_size=(2, 2), strides=(1, 1))(in4b)

        flatten = Flatten()(pool5)
        dp = Dropout(0.5)(flatten)
        fc1 = Dense(classes)(dp)
        act = Activation('softmax')(fc1)

        googlenet = Model(inputs=input, outputs=act)

        return googlenet