from data_processing import *
from Expanded_SPAAN_Model import *

from Bio import SeqIO
import numpy as np
import tensorflow

# load the datasets (it requires about 1 minute)
x, y = process(list(SeqIO.parse("./data/original_adh_dataset.fasta", "fasta")), list(SeqIO.parse("./data/original_negative_dataset.fasta", "fasta")))
x_train, y_train, x_val, y_val, x_test, y_test = split_ds(np.array(x), np.array(y), np.random.permutation(len(x)))

# method for fitting in the multi-input neural network
def fit_in_nn(x):
    x_1, x_2, x_3, x_4, x_5, x_6, x_7 = [[] for _ in range(7)]
    for el in x:
        x_1.append(el[0])
        x_2.append(el[1])
        x_3.append(el[2])
        x_4.append(el[3])
        x_5.append(el[4])
        x_6.append(el[5])
        x_7.append(el[6])
    return np.array(x_1), np.array(x_2), np.array(x_3), np.array(x_4), np.array(x_5), np.array(x_6), np.array(x_7)

# model instantiation
espaan_model = Expanded_SPAAN_Model()
max_epochs = 300

my_callbacks = [
    tensorflow.keras.callbacks.EarlyStopping(patience=10)
]

history = espaan_model.get_model().fit(
                                        x=fit_in_nn(x_train),
                                        y=y_train,
                                        batch_size=32, # default
                                        epochs=max_epochs, # the original paper has 10k epochs!
                                        verbose=1, # 1 or 2 to watch the evolution
                                        validation_data=(fit_in_nn(x_val), y_val),
                                        callbacks=my_callbacks,
                                        shuffle=True    
                                        )

import matplotlib.pyplot as plt

plt.title('Loss during training')
plt.plot(range(len(history.history['loss'])), history.history['loss'], label='loss', ls='-', linewidth=.8, color='green')
plt.plot(range(len(history.history['loss'])), history.history['val_loss'], label='validation loss', ls='-', linewidth=.8, color='red')
plt.grid(color='grey', linewidth=.4)

plt1 = plt.figure('training loss')
plt.legend(loc="upper right")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.xlim(0, len(history.history['loss'])+1)
plt.show()

plt2 = plt.figure('training accuracy')
plt.title('Accuracy during training')
plt.plot(range(len(history.history['loss'])), history.history['accuracy'], label='accuracy', ls='-', linewidth=.8, color='green')
plt.plot(range(len(history.history['loss'])), history.history['val_accuracy'], label='val_accuracy loss', ls='-', linewidth=.8, color='red')
plt.grid(color='grey', linewidth=.4)

plt.legend(loc="lower right")
plt.xlabel("Accuracy")
plt.ylabel("loss")
plt.xlim(0, len(history.history['loss'])+1)
plt.savefig('acc.png')
plt.show()

print("Test accuracy: " + str(espaan_model.get_model().evaluate(
    x=fit_in_nn(x_test),
    y=y_test   
    )[1]))

espaan_model.get_model().save('model.h5')