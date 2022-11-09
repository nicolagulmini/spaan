# LSTM layer

To enhance the performance of SPAAN we added an LSTM layer with a naive fixed length padding. 
Still testing it, but for now it reaches the same accuracy in about 30 epochs (which is an order of magnitude less than SPAAN).
On the other hand, time is spent in processing and training to consider sequential data.

This is a test with a fixed number of epochs and learning rate = 0.001, 

![acc](https://user-images.githubusercontent.com/62892813/200834845-515aa142-4e48-406e-b408-67ba818d6b87.png)

you can find the code in [this notebook](./LSTM_spaan.ipynb).
