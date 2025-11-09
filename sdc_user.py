import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def parse_complex(s: str):
    """to deal w complex numbers"""
    s = s.strip().lower()
    if s == 'i':
        return 1j
    elif s == '-i':
        return -1j
    else:
        try:
            return complex(s)
        except ValueError:
            raise ValueError("Alpha/Beta must be 1, -1, i, or -i")

def superdense_general(bits: str, a1: int, a2: int, b1: int, b2: int, alpha: complex, beta: complex):
    """
    Superdense coding with a user input entangled state.
    """
    if bits not in ['00', '01', '10', '11']:
        raise ValueError("Bits must be one of: '00', '01', '10', '11'")
    for v in [a1, a2, b1, b2]:
        if v not in [0, 1]:
            raise ValueError("a1,a2,b1,b2 must each be 0 or 1")

    qc = QuantumCircuit(2, 2)

    # entalnge a and b state
    state = np.zeros(4, dtype=complex)
    idx1 = 2 * a1 + a2
    idx2 = 2 * b1 + b2
    state[idx1] = alpha / np.sqrt(2)
    state[idx2] = beta / np.sqrt(2)
    qc.initialize(state, [0, 1])

    # Alice message
    if bits == '00':
        pass
    elif bits == '01':
        qc.x(0)
    elif bits == '10':
        qc.z(0)
    elif bits == '11':
        qc.z(0)
        qc.x(0)

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    #simulate the amount of times that AerSimulator does
    simulator = AerSimulator()
    compiled = transpile(qc, simulator)
    result = simulator.run(compiled, shots=1024).result()
    counts = result.get_counts()

    print(f"\nAlice and Bob entangled state: (1/√2) * ({alpha}|{a1}{a2}> + {beta}|{b1}{b2}>)")
    print(f"Alice sent bits: {bits}\n")
    
    print("Bob's measurement results:")
    for outcome, count in counts.items():
        print(f"  Message {outcome} received {count} times ({(count/1024)*100:.1f}%)")

    most_probable = max(counts, key=counts.get)
    print(f"\nBob decodes the message as: {most_probable}")

if __name__ == "__main__":
    print("\nSuperdense Coding Simulator\n")
    bits = input("Enter Alice's 2-bit message (00, 01, 10, 11): ").strip()
    a1 = int(input("Enter a1 (0 or 1): "))
    a2 = int(input("Enter a2 (0 or 1): "))
    b1 = int(input("Enter b1 (0 or 1): "))
    b2 = int(input("Enter b2 (0 or 1): "))
    alpha = parse_complex(input("Enter alpha (1, -1, i, or -i): "))
    beta = parse_complex(input("Enter beta (1, -1, i, or -i): "))

    superdense_general(bits, a1, a2, b1, b2, alpha, beta)

