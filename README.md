# Adhesin classifier 

SPAAN (*Software Program for prediction of Adhesins and Adhesin-like proteins using Neural network*) is originally described in 
[this paper](https://pubmed.ncbi.nlm.nih.gov/15374866/). This directory contains its Python implementation with expanded features (higher dimensional data are considered, but the features are the same as the original work). To distinguish the Python model, it is called ESPAAN.

If you want to train you own model, you can follow the tutorial on the notebook `Adhesin classifier (training).ipynb`. 
If you want to test a model, you can load an `.h5` file with keras and use it.

## Dataset description

- `data/adh.fasta` contains 443 proteins sequences, taken from [uniprot](https://www.uniprot.org/) searching for `adhesin AND reviewed:yes`
- `data/not_adh.fasta` contains 500 proteins sequences, taken from the first 2 pages of [uniprot](https://www.uniprot.org/) searching for `NOT adhesin AND reviewed:yes`
- `data/original_adh_dataset.fasta` and `data/original_negative_dataset.fasta` are the original datasets, used in the [paper](https://pubmed.ncbi.nlm.nih.gov/15374866/), courtesy of [S. Ramachandran](https://sites.google.com/view/ramuigib/home) (one of the authors).

## Performance

The training performances of the `trained_model.h5` are shown in these two plots:

![loss](https://user-images.githubusercontent.com/62892813/165765620-95d96b09-e6e4-4417-9256-7634e41af7b2.png)
![acc](https://user-images.githubusercontent.com/62892813/165765632-be1d09fe-f713-4492-b10c-4720bf186ef2.png)

A comparison between the original SPAAN and the first trained model was performed on the `data/adh.fasta` and `data/not_adh.fasta` datasets. The spaan results are in the `data/results` file. These test proteins were not used to train the models. 

```
true positive 30.55 % / 50 %
true negative 48.83 % / 50 %
false positive 15.95 %
false negative 4.66 %
adhesin classifier accuracy 79.38 %

spaan_true positive 34.23 % / 50%
spaan_true negative 48.83 % / 50%
spaan_false positive 12.27 %
spaan_false negative 4.66 %
SPAAN accuracy 83.06 %
```

## Unknown symbols

I decided not to handle the unknown symbols because this program can be used by biologists in reverse vaccinology pipelines in which the probability of a protein to be an adhesine could change significantly the result, and if a protein has an unknown symbol it is already a bad candidate for vaccines production: how can you produce a vaccine with a protein without knowing it?
