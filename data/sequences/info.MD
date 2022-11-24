Bacterial adhesins were obtained performing jackhammer search among reference proteomes of eubacteria using https://www.ebi.ac.uk/Tools/hmmer/search/jackhmmer with default patrameters and the domains listed in Adhesive_domain_info.xlsx as query.
Non adhesin proteins were obtained using the following query in uniprot:
(taxonomy_id:2) AND (reviewed:true) NOT (keyword:KW-1217) NOT (keyword:KW-1233) NOT (keyword:KW-0130) NOT (cc_function:adhesion) NOT (cc_function:"cell adhesion")
a subset of non adhesin proteins was randomly selected to match the size of adhesin dataset.
Reduntant sequences (60% and 25% identity trasholds) were removed using CD-HIT (https://sites.google.com/view/cd-hit).

raw_sequences contains adhesins and non_adhesin sequences before redundancy removal and random picking (in the case of non_adhesins).

processed_sequences contains sequences of (non-)adhesins after redundancy removal and, in the case of non_adhesins, after random picking.

