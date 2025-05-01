simpleFoam -postProcess -dict system/controlDict
# postProcess -dict system/controlDict -funcs '(actuatorThrust pAbove pBelow)' -fields '(U p)'
# postProcess -dict system/postProcessDict -funcs '(fieldAveraging)' -fields '(U p)'
