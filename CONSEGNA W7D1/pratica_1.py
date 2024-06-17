def word_length(A):
    B = []
    for word in A:
        B.append(len(word))
    return B

A = ["pippo","pluto","paperino","paperina","topolino"]
B = word_length(A)
print(B)