from pycdhit import cd_hit, read_clstr


"""
i: input input filename in fasta format, required
o: output filename, required
c:  sequence identity threshold, default 0.9
n: word_length, default 5, n=5 for thresholds 0.7 ~ 1.0, n=4 for thresholds 0.6 ~ 0.7, n=3 for thresholds 0.5 ~ 0.6, n=2 for thresholds 0.4 ~ 0.5
d: length of description in .clstr file, default 20. if set to 0, it takes the fasta defline and stops at first space
"""
res = cd_hit(
    i="/Users/kianaseraj/desktop/github-kianaseraj/go_cd_hit/sequence.fasta",
    o="/Users/kianaseraj/desktop/github-kianaseraj/go_cd_hit/out_0.7",
    c=0.7,
    n=5,
    d=0,
    sc=1
)


