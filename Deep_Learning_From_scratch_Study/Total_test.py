from LeNet import LeNet
from GoogLeNet import GoogLeNet
from AlexNet import AlexNet
from minivggnet import MiniVGGNet
from keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

print("[INFO] accessing MNIST...")
dataset = datasets.fetch_openml("mnist_784", version=1)
data = dataset.data

if K.image_data_format() == "channels_first":
    data = data.reshape(data.shape[0], 1, 28, 28)

else:
    data = data.reshape(data.shape[0], 28, 28, 1)

(trainX, testX, trainY, testY) = train_test_split(data / 255.0,
                                                  dataset.target.astype("int"), test_size = 0.25, random_state = 42)
le = LabelBinarizer()
trainY = le.fit_transform(trainY)
testY = le.transform(testY)

print("[INFO] compiling model...")
opt = SGD(lr=0.01)

model = LeNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
print("[INFO] training network...")
LeNet_H = model.fit(trainX, trainY, validation_data=(testX, testY),batch_size=128, epochs=20, verbose=1)
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=128)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=[str(x) for x in le.classes_]))

model = AlexNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
print("[INFO] training network...")
AlexNet_H = model.fit(trainX, trainY, validation_data=(testX, testY),batch_size=128, epochs=20, verbose=1)
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=128)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=[str(x) for x in le.classes_]))

model = GoogLeNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
print("[INFO] training network...")
GoogLeNet_H = model.fit(trainX, trainY, validation_data=(testX, testY),batch_size=128, epochs=20, verbose=1)
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=128)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=[str(x) for x in le.classes_]))

model = MiniVGGNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
print("[INFO] training network...")
MiniVGGNet_H = model.fit(trainX, trainY, validation_data=(testX, testY),batch_size=128, epochs=20, verbose=1)
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=128)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=[str(x) for x in le.classes_]))



plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 20), LeNet_H.history["val_acc"], label="LeNet_acc")
plt.plot(np.arange(0, 20), AlexNet_H.history["val_acc"], label="AlexNet_acc")
plt.plot(np.arange(0, 20), GoogLeNet_H.history["val_acc"], label="GoogleNet_acc")
plt.plot(np.arange(0, 20), MiniVGGNet_H.history["val_acc"], label="VGGNet_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()