def to_rna(dna_strand):
    mapping = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([mapping[i] for i in dna_strand])
