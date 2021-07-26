def to_rna(dna_strand):
    rna_strand = []
    for n in dna_strand:
        if n == 'G':
            rna_strand.append('C')
        elif n == 'C':
            rna_strand.append('G')
        elif n == 'T':
            rna_strand.append('A')
        elif n == 'A':
            rna_strand.append('U')
    return ''.join(rna_strand)