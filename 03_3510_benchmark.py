from AulasPraticas import AP_03_ordenacao as ap3
#import AulasPraticas.AP_03_ordenacao as ap3
import random
import time
import sys

sys.setrecursionlimit(10**6)


def caso_medio(n):
    conj = {}
    lista = []
    while len(lista) != n:
        elem = random.randint(1, n)
        if elem not in conj:
            lista.append(elem)
            conj[elem] = True
    return lista

def pior_quick(n):
    return [x for x in range(n)][::-1]

def perf_select(n, k):
    times =[]
    for _ in range(k):
        lista = caso_medio(n)
        tempo_inicial = time.perf_counter()
        ap3.selection_sort(lista)
        tempo_final = time.perf_counter()
        times.append(tempo_final - tempo_inicial)
    return sum(times)/k

def perf_select(n, k):
    times =[]
    for _ in range(k):
        lista = caso_medio(n)
        tempo_inicial = time.perf_counter()
        ap3.selection_sort(lista)
        tempo_final = time.perf_counter()
        times.append(tempo_final - tempo_inicial)
    return sum(times)/k

def perf_merge(n, k):
    times =[]
    for _ in range(k):
        lista = caso_medio(n)
        tempo_inicial = time.perf_counter()
        ap3.divide_and_conquer_sort(lista)
        tempo_final = time.perf_counter()
        times.append(tempo_final - tempo_inicial)
    return sum(times)/k

def perf_quick(n, k, pior = None):
    times = []
    for _ in range(k):
        lista = pior_quick(n) if pior else caso_medio(n)
        tempo_inicial = time.perf_counter()
        ap3.quick_sort(lista)
        tempo_final = time.perf_counter()
        times.append(tempo_final - tempo_inicial)
    return sum(times)/k

print("-" * 64)
print(f"{'Select Sort':^64}")
print("-" * 64)
print(f"N=100: {perf_select(100,50)} ms")
print(f"N=500: {perf_select(500,50)} ms")
print(f"N=1000: {perf_select(1000,50)} ms")
print(f"N=5000: {perf_select(5000,50)} ms")
print("-" * 64)
print(f"{'Merge Sort':^64}")
print("-" * 64)
print(f"N=100: {perf_merge(100,50)} ms")
print(f"N=500: {perf_merge(500,50)} ms")
print(f"N=1000: {perf_merge(1000,50)} ms")
print(f"N=5000: {perf_merge(5000,50)} ms")
print("-" * 64)
print(f"{'Quick Sort Caso Médio':^64}")
print("-" * 64)
print(f"N=100: {perf_quick(100,50)} ms")
print(f"N=500: {perf_quick(500,50)} ms")
print(f"N=1000: {perf_quick(1000,50)} ms")
print(f"N=5000: {perf_quick(5000,50)} ms")
print("-" * 64)
print(f"{'Quick Sort Pior Caso':^64}")
print("-" * 64)
print(f"N=100: {perf_quick(100,50,pior_quick)} ms")
print(f"N=500: {perf_quick(500,50,pior_quick)} ms")
print(f"N=1000: {perf_quick(1000,50,pior_quick)} ms")
print(f"N=5000: {perf_quick(5000,50,pior_quick)} ms")
print("-" * 64)
