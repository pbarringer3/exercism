CODON_DICT = {
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
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
    }


def proteins(strand):
    if len(strand) % 3 != 0:
        raise ValueError("The strand must consist of 3 neucleotide codons")

    codons = [strand[i: i+3] for i in range(0, len(strand), 3)]
    prot = [CODON_DICT[codon] for codon in codons]

    if 'STOP' in prot:
        prot = prot[0: prot.index('STOP')]

    return prot
