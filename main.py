from edge_coloring import GCL
from quantum_part import entire_circuit


b = [
    [2,1,0,1],
    [1,0,1,0],
    [0,1,0,3],
    [1,0,3,0]
]


def main():
    # hamiltonian = input()
    hamiltonian = b

    decomposed = GCL(hamiltonian)

    simulating_circuits = [entire_circuit(h_j) for h_j in decomposed]

    return simulating_circuits

if __name__ == "__main__":
    ret = main()
    for c in ret:
        print(c)
        input()
    print(len(ret))