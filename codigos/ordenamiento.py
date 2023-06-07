def selection(A):
    for i in range(0, len(A)-1  ):
        menor = float("inf")
        pos = 0
        for j in range(i, len(A)):
            if A[j] < menor:
                menor = A[j]
                pos = j
        aux = A[i]
        A[i] = menor
        A[pos] = aux
        print(A) # Puede borrarse

def bubble(A):
    for i in range(0, len(A)-1):
        for j in range (0, len(A)-1-i):
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux 
            print(A) # Puede borrarse

def insertion(A):
    for i in range (1, len(A)):
        insertar = A[i]
        j = i-1
        while j >= 0 and A[j] > insertar:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = insertar
        print(A) # Puede borrarse

def merge(S, S1, S2):
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(A):
    if len(A) > 1:
        S1 = A[0:len(A)//2]
        S2 = A[len(A)//2:len(A)]
        merge_sort(S1)
        merge_sort(S2)
        merge(A,S1,S2)
        print (A) # Puede borrarse
    else:
        print(A) # Puede borrarse

def quick_sort(A):
    if len(A) > 1:
        pivot = A[-1]
        menores = []
        mayores = []
        iguales = []
        while len(A) > 0:
            if A[0] > pivot:
                mayores.append(A[0])
            elif A[0] < pivot:
                menores.append(A[0])
            else:
                iguales.append(A[0])
            A.pop(0)
        
        quick_sort(menores)
        quick_sort(mayores)
        while len(menores) > 0:
            menor = menores.pop(0)
            A.append(menor)
        while len(iguales) > 0:
            igual = iguales.pop(0)
            A.append(igual)
        while len(mayores) > 0:
            mayor = mayores.pop(0)
            A.append(mayor)
    print(A) # Puede borrarse
