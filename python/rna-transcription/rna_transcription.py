def to_rna(dna_strand):
    DNA = "ACGT"
    RNA = "UGCA"
    rna_dict = str.maketrans(DNA, RNA)
    return dna_strand.translate(rna_dict)
