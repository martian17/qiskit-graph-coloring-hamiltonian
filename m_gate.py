from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

from qiskit.visualization import plot_histogram


def multi_toffoli_q(qc, q_controls, q_target, q_ancillas=None):
    """
    N = number of qubits
    controls = control qubits
    target = target qubit
    ancillas = ancilla qubits, len(ancillas) = len(controls) - 2
    """
    # q_controls = register_to_list(q_controls)
    # q_ancillas = register_to_list(q_ancillas)
    if len(q_controls) == 1:
        qc.cx(q_controls[0], q_target)
    elif len(q_controls) == 2:
        qc.ccx(q_controls[0], q_controls[1], q_target)
    elif len(q_controls) > 2 and (q_ancillas is None or len(q_ancillas) < len(q_controls) - 2):
        raise Exception('ERROR: need more ancillas for multi_toffoli!')
    else:
        multi_toffoli_q(qc, q_controls[:-1], q_ancillas[-1], q_ancillas[:-1])
        qc.ccx(q_controls[-1], q_ancillas[-1], q_target)
        multi_toffoli_q(qc, q_controls[:-1], q_ancillas[-1], q_ancillas[:-1])

def m_gate_for_special_case():
    qr = QuantumRegister(7)
    cr = ClassicalRegister(7)
    circuit = QuantumCircuit(qr, cr)

    circuit.x(0)
    multi_toffoli_q(circuit, [0,1], 6)
    circuit.x(0)
    circuit.barrier()

    circuit.x(1)
    multi_toffoli_q(circuit, [0,1], 6)
    circuit.barrier()

    multi_toffoli_q(circuit, [0,1], 3)
    circuit.barrier()

    circuit.x([0,1])
    multi_toffoli_q(circuit, [0,1], 2)
    circuit.x(0)
    circuit.barrier()

    circuit.measure(qr, cr)
    print(circuit)

    execute_circuit((circuit))


def exists_one_in_column(m, column):
    for i in range(len(m)):
        if m[i][column] > 0:
            return True

    return False

def int_to_bin(num, digit):
    num_bin = bin(num)[2:]
    if len(num_bin) < digit:
        num_bin = '0'* (digit - len(num_bin)) + num_bin
    return num_bin

def one_bits_list(num_bin):
    ret = []
    for iter, b in enumerate(num_bin):
        if b == '0':
            ret.append(iter)
    return ret


def m_gate_for_general_case(q1, q2, q3, hamiltonian):
    n = len(q1)
    c1 = ClassicalRegister(n)
    c2 = ClassicalRegister(n)
    c3 = ClassicalRegister(n)
    m_circuit = QuantumCircuit(q1,q2,q3, c1,c2,c3)

    for i in range(2**n):
        if exists_one_in_column(hamiltonian, i):
            num_bin = int_to_bin(i, n)
            ones_idx = one_bits_list(num_bin)
            print(ones_idx)
            for idx in ones_idx:
                m_circuit.x(idx)
            multi_toffoli_q(m_circuit, [i for i in range(n)], 2*n)
            for idx in ones_idx:
                m_circuit.x(idx)
            m_circuit.barrier()

    m_circuit.measure(q1, c1)
    m_circuit.measure(q2, c2)
    m_circuit.measure(q3, c3)

    print(m_circuit)

    # execute_circuit(m_circuit)


def execute_circuit(circuit):
    backend = Aer.get_backend('qasm_simulator')
    shots = 1024
    results = execute(circuit, backend=backend, shots=shots).results()
    answer = results.get_counts()
    r = plot_histogram(answer)
    r.show()



if __name__ == "__main__":
    hamil = [[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]
    n = 2
    q1 = QuantumRegister(n)
    q2 = QuantumRegister(n)
    q4 = QuantumRegister(n)
    m_gate_for_general_case(q1,q2,q4,hamil)
