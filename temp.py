from Bio import SeqIO

adhesin_dataset = list(SeqIO.parse("adh.fasta", "fasta"))
not_adhesin_dataset = list(SeqIO.parse("not_adh.fasta", "fasta"))

print(len(adhesin_dataset))
print(len(not_adhesin_dataset))

lista_aminoacidi = []
for aa in adhesin_dataset[0]:
    if aa not in lista_aminoacidi:
        lista_aminoacidi.append(aa)
print(len(lista_aminoacidi))

print(adhesin_dataset[0].seq)
