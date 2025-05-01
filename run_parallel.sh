#!/bin/bash

# Detect available CPU cores
#NP=$(nproc)
NP=12

echo "📦 Decomposing domain..."
decomposePar -force > log.decomposePar

echo "🚀 Running simpleFoam in parallel with $NP processors..."
mpirun -np $NP simpleFoam -parallel > log.simpleFoam

echo "🔧 Reconstructing solution..."
reconstructPar > log.reconstructPar

echo "🧹 Cleaning up processor directories..."
rm -rf processor*

echo "✅ Done!"
