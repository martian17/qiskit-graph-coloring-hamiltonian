from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, BasicAer

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

    backend = BasicAer.get_backend('statevector_simulator')
    shots = 1024
    results = execute(circuit, backend=backend, shots=shots).result()
    answer = results.get_counts()
    plot_histogram(answer)
    r = plot_histogram(answer)
    r.show()
    input()

if __name__ == "__main__":
    m_gate_for_special_case()
