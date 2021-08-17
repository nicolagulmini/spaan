from Bio import SeqIO

adhesin_dataset = list(SeqIO.parse("adh.fasta", "fasta"))
not_adhesin_dataset = list(SeqIO.parse("not_adh.fasta", "fasta"))

test_protein = adhesin_dataset[0].seq
