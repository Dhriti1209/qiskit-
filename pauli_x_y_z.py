import sys
sys.stdout.reconfigure(encoding='utf-8')
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.x(0)

print("Pauli-X Gate Circuit:")
print(qc.draw(output='text', fold=-1))

state = Statevector.from_instruction(qc)
print("Final State:", state)

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.y(0)

print("Pauli-Y Gate Circuit:")
print(qc.draw(output='text', fold=-1))

state = Statevector.from_instruction(qc)
print("Final State:", state)

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.z(0)

print("Pauli-Z Gate Circuit:")
print(qc.draw(output='text', fold=-1))

state = Statevector.from_instruction(qc)
print("Final State:", state)