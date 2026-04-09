import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Number of input qubits
n = 2

# Create circuit with n input qubits + 1 ancilla + n classical bits
qc = QuantumCircuit(n + 1, n)

# Step 1: Initialize ancilla qubit to |1>
qc.x(n)

# Step 2: Apply Hadamard to all qubits
for i in range(n + 1):
    qc.h(i)

# -------------------------
# ORACLE (Balanced Example)
# f(x) = x1 XOR x2
# -------------------------
qc.cx(0, n)
qc.cx(1, n)

# Step 3: Apply Hadamard to input qubits again
for i in range(n):
    qc.h(i)

# Step 4: Measure input qubits
for i in range(n):
    qc.measure(i, i)

# Print circuit
print("Deutsch-Jozsa Circuit:")
print(qc.draw(output='text', fold=-1))

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
job = simulator.run(compiled, shots=1000)
result = job.result()

# Output
counts = result.get_counts()
print("Measurement Results:", counts)