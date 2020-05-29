from LeNet import LeNet
#from GoogLeNet import GoogLeNet
# from ResNet import ResNet

from time import time
import numpy as np
import matplotlib.pyplot as plt

from keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from keras import backend as K

def main():

    print("[INFO] Accessing MNIST dataset.")
    dataset = datasets.fetch_openml("mnist_784", version=1)
    data = dataset.data

    if K.image_data_format() == "channels_first":
        data = data.reshape(data.shape[0], 1, 28, 28)
    else:
        data = data.reshape(data.shape[0], 28, 28, 1)

    print("[INFO] Number of data : {}".format(data.shape[0]))

    (X_train, X_test, Y_train, Y_test) = train_test_split(data/255.0, dataset.target.astype("int"), test_size=0.25, random_state=42)

    le = LabelBinarizer()
    Y_train = le.fit_transform(Y_train)
    Y_test = le.fit_transform(Y_test)

    print("[INFO] Compiling model.")
    start_time = time()
    opt = SGD(lr=0.01, momentum=0.9, decay=0.0005)
    model = LeNet.build(width=28, height=28, depth=1, classes=10)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

    print("[INFO] Training network.")
    H = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=128, epochs=10, verbose=1)

    print("[INFO] Evaluating network.")
    pred = model.predict(X_test, batch_size=128)
    print(classification_report(Y_test.argmax(axis=1), pred.argmax(axis=1), target_names=[str(x) for x in le.classes_]))

    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, 10), H.history['loss'], label="Train_loss")
    plt.plot(np.arange(0, 10), H.history['val_loss'], label="Val_loss")
    plt.plot(np.arange(0, 10), H.history['acc'], label="Train_acc")
    plt.plot(np.arange(0, 10), H.history['val_acc'], label="Val_acc")

    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()

    plt.show()

    plt.savefig("GoogLeNet.png")
    print("time : ", time() - start_time)

if __name__ == '__main__':
    main()