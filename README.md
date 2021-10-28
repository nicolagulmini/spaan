# spaan 

SPAAN (*Software Program for prediction of Adhesins and Adhesin-like proteins using Neural network*) is originally described in 
[this paper](https://pubmed.ncbi.nlm.nih.gov/15374866/). This directory contains its Python implementation with expanded features (higher dimensional data are considered, but the features are the same as the original work). To distinguish the Python model, it is called ESPAAN.

If you want to train you own model, you can follow the tutorial on the notebook `ESPAAN Training.ipynb`. 
If you want to test a model, you can load an `.h5` file with keras and use it.

## Dataset description

- `data/adh.fasta` contains 443 proteins sequences, taken from [uniprot](https://www.uniprot.org/) searching for `adhesin AND reviewed:yes`
- `data/not_adh.fasta` contains 500 proteins sequences, taken from the first 2 pages of [uniprot](https://www.uniprot.org/) searching for `NOT adhesin AND reviewed:yes`
- `data/original_adh_dataset.fasta` and `data/original_negative_dataset.fasta` are the original datasets, used in the [paper](https://pubmed.ncbi.nlm.nih.gov/15374866/), courtesy of [S. Ramachandran](https://sites.google.com/view/ramuigib/home) (one of the authors).

## Performance comparison

A comparison between the original SPAAN and the `model_trained_on_original_dataset.h5` was performed on the `data/adh.fasta` and `data/not_adh.fasta` datasets. The spaan results are in the `data/results` file. These test proteins were not used to train the models. 

```
true positive 33.87 % / 50%
true negative 47.12 % / 50%
false positive 12.64 %
false negative 6.38 %
ESPAAN accuracy 80.99 %

spaan_true positive 34.23 % / 50%
spaan_true negative 48.83 % / 50%
spaan_false positive 12.27 %
spaan_false negative 4.66 %
SPAAN accuracy 83.06 %
```

## Brief discussion

Despite I used higher dimensional features than the original spaan model (but less epochs), the results are still comparable. This proofs that the choices of the original authors are thoughtful and reasoned. Further changes and additions can be made.

## Unknown symbols

I decided not to handle the unknown symbols because this program can be used by biologists in reverse vaccinology pipelines in which the probability of a protein to be an adhesine could change significantly the result, and if a protein has an unknown symbol it is already a bad candidate for vaccines production: how can you produce a vaccine with a protein without knowing it?

## TODO
- [ ] add dropout to the model
- [ ] substitute the feature computation with the iFeature system
