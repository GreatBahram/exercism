from itertools import islice


DNA_TABLE = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
}


def codons(words):
    stops = ('UAA', 'UAG', 'UGA')
    length = len(words) // 3
    iterator = iter(words)
    for _ in range(length):
        codon = ''.join(islice(iterator, 3))
        if codon in stops:
            break
        yield codon


def proteins(strand):
    return [DNA_TABLE[codon] for codon in codons(strand)]
