rm -rf [1-9]* constant/polyMesh postProcessing
blockMesh
# surfaceFeatureExtract
snappyHexMesh -overwrite
topoSet
checkMesh
# setsToZones
touch DeflectorWithActuatorDisk.foam
paraview DeflectorWithActuatorDisk.foam