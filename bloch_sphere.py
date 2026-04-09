import sys
sys.stdout.reconfigure(encoding='utf-8')

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)

qc.h(0)

print("Hadamard Gate Circuit:")
print(qc.draw(output='text', fold=-1))

state = Statevector.from_instruction(qc)
print("Final Statevector:", state)

plot_bloch_multivector(state)
plt.show()