import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Create entanglement
qc.h(0)       # Hadamard on qubit 0
qc.cx(0, 1)   # CNOT: control=0, target=1

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Print circuit
print(qc.draw(output='text', fold=-1))

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
job = simulator.run(compiled, shots=1000)
result = job.result()

# Output
counts = result.get_counts()
print("Measurement Results:", counts)