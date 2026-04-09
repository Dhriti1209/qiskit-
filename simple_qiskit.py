import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

qc.h(0)

qc.measure(0, 0)

print(qc.draw(output='text', fold=-1))

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

counts = result.get_counts()
print("Measurement Results:", counts)