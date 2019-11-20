from edge_coloring import GCL



# b = [
#     [2,1,0,1],
#     [1,0,1,0],
#     [0,1,0,3],
#     [1,0,3,0]
# ]


def main():
    hamiltonian = input()
    decomposed = GCL(hamiltonian)

    simulating_circuits = [create_circuit(h_j) for h_j in decomposed]

    return simulating_circuits

if __name__ == "__main__":
    ret = main()
    print(ret)