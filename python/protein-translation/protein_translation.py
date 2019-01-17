import re
from itertools import takewhile

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
    'UAA': 'Stop',
    'UAG': 'Stop',
    'UGA': 'Stop',
}


def proteins(strand):
    codons = re.findall(r'\w{3}', strand)
    polypeptides = [DNA_TABLE[codon] for codon in codons]
    return list(takewhile(lambda p: p != 'Stop', polypeptides))
