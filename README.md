# Adhesin classifier 

This model is inspired by 
SPAAN (*Software Program for prediction of Adhesins and Adhesin-like proteins using Neural network*), which is originally described in 
[this paper](https://pubmed.ncbi.nlm.nih.gov/15374866/). 

## Dataset

Bacterial adhesins were obtained performing [jackhmmer](https://www.ebi.ac.uk/Tools/hmmer/search/jackhmmer) search among reference proteomes of eubacteria with default patrameters and the domains listed in [this file](./new_data/Adhesive_domains_info.xlsx) as query.
Non adhesin proteins were obtained using the following query in uniprot:
```
(taxonomy_id:2) AND (reviewed:true) NOT (keyword:KW-1217) NOT (keyword:KW-1233) NOT (keyword:KW-0130) NOT (cc_function:adhesion) NOT (cc_function:"cell adhesion")
```
a subset of non adhesin proteins was randomly selected to match the size of adhesin dataset.
Reduntant sequences (60% and 25% identity trasholds) were removed using [CD-HIT](https://sites.google.com/view/cd-hit).


## Feature computation

Features are computed with [iFeature](https://github.com/Superzchen/iFeature) so a parser of the iFeature output files, to obtain the vectors to feed the model, is used. They are:
- AAC: amino acids composition
- DPC: dipeptide composition
- CTDC: composition
- CTDT: transition
- CTDD: distribution

([here](https://github.com/Superzchen/iFeature/blob/master/iFeatureManual.pdf) if you want more information about what they are and how to compute them).

... and here a brief tutorial on how to compute them:
```
!rm -r iFeature
!git clone https://github.com/Superzchen/iFeature
!python iFeature/iFeature.py --file ./input.fasta --type AAC --out aac.out    # amino acids composition
!python iFeature/iFeature.py --file ./input.fasta --type DPC --out dpc.out    # dipeptide composition
!python iFeature/iFeature.py --file ./input.fasta --type CTDC --out ctdc.out  # composition
!python iFeature/iFeature.py --file ./input.fasta --type CTDT --out ctdt.out  # transition
!python iFeature/iFeature.py --file ./input.fasta --type CTDD --out ctdd.out  # distribution
```

## PCA

Since every sequence has a (20+400+39+39+195=693)-dimensional feature vector, we performed Principal Component Analysis to reduce the dimensionality.
Here the results: 

![Explained variance (1)](https://user-images.githubusercontent.com/62892813/202872432-dd78ccca-f779-4dd1-8bc3-59c328ff0ead.png)

so we can take just the first 350 components, reducing the dimensionality of about the 50%.

## Model

We decided to use the smallest model possible, and with just a 10-units Dense layer and a K=400 from PCA, we are able to get the best results so far.

```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_11 (InputLayer)       [(None, 400)]             0         
                                                                 
 dense_21 (Dense)            (None, 10)                4010      
                                                                 
 dense_22 (Dense)            (None, 1)                 11        
                                                                 
=================================================================
Total params: 4,021
Trainable params: 4,021
Non-trainable params: 0
_________________________________________________________________
```

## Results

![loss](https://user-images.githubusercontent.com/62892813/202910944-e2a0a3ee-271b-448f-b3ad-5be80b661abd.png)

![acc](https://user-images.githubusercontent.com/62892813/202910949-4e4e74b4-ed3a-4f3a-b6d4-9c12b12dcbbf.png)

```
test_loss = 0.214177668094635
test_accuracy = 0.9396551847457886
```

Notice that removing regularizers and increasing neurons in the Dense layer it is possible to obtain roughly the same results (a little bit more overfitted) but in about 20 epochs.

<!---


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

![loss](https://user-images.githubusercontent.com/62892813/200617266-4cc80054-f90b-49da-bb04-77a23cbefac9.png)
![acc](https://user-images.githubusercontent.com/62892813/200617271-75c65bff-f439-469d-bdce-72e6115e2984.png)

reaching a test accuracy of 88%.

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

---> 
