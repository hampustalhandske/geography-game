import networkx as nx
import itertools

def cartersian(A, B):
    return set(itertools.product(A, B))

def powerset(S):
    return {frozenset(subset) for n in range(len(S) + 1) for subset in itertools.combinations(S, n)}

def domain(R):
    return {x for x, _ in R}

def range(R):
    return {y for _, y in R}

def image_of(R, x):
    return {y for a, y in R if a == x}

def inverse(R):
    return {(y, x) for x, y in R}


def is_reflexive(R, A):
    for a in A:
        if (a, a) not in R:
            return False
    return True

def is_irreflexive(R, A):
    for a in A:
        if (a, a) in R:
            return False
    return True

def is_symmetric(R):
    for (a, b) in R:
        if (b, a) not in R:
            return False
    return True

def is_subset(A, B):
    for a in A:
        if a not in B:
            return False
    return True

def is_transitive(R):
    return all(image_of(R, b).issubset(image_of(R, a)) for a, b in R)

    
def remove_pair(x, y, R):
    return {(a, b) for a, b in R if (a, b) != (x, y) and (a, b) != (y, x)}



