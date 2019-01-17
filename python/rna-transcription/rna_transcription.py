def to_rna(dna_strand):
    DNA_RNA_TABLE = str.maketrans("ACGT" , "UGCA")
    return dna_strand.translate(DNA_RNA_TABLE)
