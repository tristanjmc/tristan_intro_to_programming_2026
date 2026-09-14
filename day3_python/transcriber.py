with open('my_seq.fa','r')as file:
    dna = file.read()
print(dna)
rna=[]
with open('my_rna_seq.fa','w') as file:
    for value in dna:
        if value=='T':
            rna.append("U")
        elif value in ['A','G','C']:
            rna.append(value)
        else:
            print("not a base :(")
            raise SystemExit
    rna_joined=''.join(rna)
    file.write(rna_joined)
    print(rna_joined)
