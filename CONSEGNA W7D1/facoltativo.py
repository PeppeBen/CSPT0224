def word_length(A):
    B = []
    for word in A:
        B.append(len(word))
    return B

A = [input("Inserisci una parola e otterrai la sua lunghezza: \n")]
B = word_length(A)
print(B)