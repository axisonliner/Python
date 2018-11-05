import math
import maya.cmds as cmds
selectPop = cmds.ls(type=['PopulationToolLocator'])
if cmds.objExists(selectPop[0]) and cmds.attributeQuery(
                                    'numberParticlesPlaced', 
                                    node=selectPop[0], 
                                    exists=True):
    popCount = cmds.getAttr(selectPop[0] + '.numberParticlesPlaced')
tornadoPos = cmds.xform('Tornado', q=True, translation=True, worldSpace=True)
particlesPos = cmds.getParticleAttr(
        'particleShape1.pt[0:{num}]'.format(
            num=popCount), 
            attribute='position', 
            array=True)
sort = []
while len(particlesPos) > 3:
    one = tuple(particlesPos[:3])
    sort.append(one)
    particlesPos = particlesPos[3:]
sort.append(particlesPos)
del sort[-1]
particlesPos = sort
vectorF = []
for p, pos in enumerate(particlesPos):
    deltaX = tornadoPos[0] - pos[0]  
    deltaZ = tornadoPos[2] - pos[2]
    rotD = math.atan2(deltaX, deltaZ) #math.degrees(
    z = math.sin(rotD)
    x = math.cos(rotD)
    one = (x, 0.0, z)  
    vectorF.append(one)
//print 'vectorF =', vectorF    
for i in range(popCount):
    cmds.select('particleShape1.pt[{num}]'.format(num=i))
    cmds.setParticleAttr(vectorValue=vectorF[i], attribute='MyVectorForce')
