"""This script is contains a simple use case of the QFAST synthesis method."""
from __future__ import annotations

import logging

from bqskit.compiler import CompilationTask
from bqskit.compiler import Compiler
from bqskit.compiler.passes.synthesis.qpredict import QPredictDecompositionPass
from bqskit.ir import Circuit
from bqskit.qis.unitary.unitarymatrix import UnitaryMatrix

# Enable logging
logging.getLogger('bqskit').setLevel(logging.DEBUG)

# Let's create a random 3-qubit unitary to synthesize and add it to a circuit.
circuit = Circuit.from_unitary(UnitaryMatrix.random(3))


# We will now define the CompilationTask we want to run.
task = CompilationTask(circuit, [QPredictDecompositionPass()])

# Finally let's create create the compiler and execute the CompilationTask.
compiler = Compiler()
compiled_circuit = compiler.compile(task)
for op in compiled_circuit:
    print(op)

# Close our connection to the compiler backend
del compiler