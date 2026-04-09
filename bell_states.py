import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

simulator = AerSimulator()

# Function to run and print results
def run_circuit(qc, name):
    qc.measure([0,1], [0,1])
    print(f"\n{name} Circuit:")
    print(qc.draw(output='text', fold=-1))
    
    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=1000)
    result = job.result()
    
    print(f"{name} Output:", result.get_counts())

# 1. Phi+
qc1 = QuantumCircuit(2,2)
qc1.h(0)
qc1.cx(0,1)
run_circuit(qc1, "Phi+")

# 2. Phi-
qc2 = QuantumCircuit(2,2)
qc2.h(0)
qc2.cx(0,1)
qc2.z(0)
run_circuit(qc2, "Phi-")

# 3. Psi+
qc3 = QuantumCircuit(2,2)
qc3.h(0)
qc3.cx(0,1)
qc3.x(1)
run_circuit(qc3, "Psi+")

# 4. Psi-
qc4 = QuantumCircuit(2,2)
qc4.h(0)
qc4.cx(0,1)
qc4.x(1)
qc4.z(0)
run_circuit(qc4, "Psi-")