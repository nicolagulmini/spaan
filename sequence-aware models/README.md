# Sequence-aware models

This section is an attempt to obtain an adhesin classifier using sequences.

## Transformer

We tried a transformer on sequences to classify adhesins and we reached about 90% accuracy in not so many epochs. The drawback is that the training is slower than the model based on features.

![acc](https://user-images.githubusercontent.com/62892813/203839526-b5fdb6cf-3edc-4ba8-8754-2452b16b2557.png)

You can find the code in [this notebook](./Transformer_based_adhesin_classification.ipynb).

## LSTM

We used a model which exploits both the extracted features from protein sequences and protein sequences themselves, to reach better results. The model is obtained simply adding an LSTM layer. It is just a test, and here there are the results:

![acc](https://user-images.githubusercontent.com/62892813/202906147-cf212540-53a5-46e3-94dd-2b417e737729.png)

You can find the code and follow every step in [this notebook](./SAAC.ipynb).
