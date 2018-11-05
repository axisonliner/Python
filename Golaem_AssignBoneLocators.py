from glm.devkit import *
print
simulationData = createAndReadSimulationData('C:/Temp/Golaem/test.crowdField1.gscs')
if (simulationData is not None):
    print('Success while opening Simulation Data file')

frameData = createFrameData(simulationData)
print frameData
if (readFrameData(frameData , simulationData, 'C:/Temp/Golaem/test.crowdField1.2.gscf') == GSC_SUCCESS):
    print('Success while opening Frame Data file')
else:
    print('Error while opening Frame Data file')
    destroyFrameData(frameData, simulationData)
    destroySimulationData(simulationData)
    # return
bonePos = []
# get bone position array
bonePos.append(floatArray_frompointer(getBonePositions(frameData)))
# bonePos = floatArray_frompointer(getBonePositions(frameData))
for i in bonePos:
	print i
# # set root bone height (Y) to 0
# entityCount = simulationData._entityCount
# for iEntity in xrange(0, entityCount ):
#     # root bone is the first bone
#     iBone = getEntityBoneOffsetIndex(iEntity, simulationData)
#     # each position is made of 3 float (*3), and we access the Y (+1)
#     bonePos[iBone * 3 + 1] = 0

# # write frame data
# if (writeFrameData('cacheFilePath/cacheFileName.gscf', frameData, simulationData) == GSC_SUCCESS):
#     print('Success while writing Frame Data file')
 
# # clean memory
# destroyFrameData(frameData, simulationData)
# destroySimulationData(simulationData)   
print 'Done'    