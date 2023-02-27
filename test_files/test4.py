import sim


sim.simxFinish(-1)
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)

print ('Program started')

if clientID!=-1:
    print("Connected to remote API server")

    r, target = sim.simxGetObjectHandle( clientID , "IRB4600_IkTarget", sim.simx_opmode_blocking)
    r, cube = sim.simxGetObjectHandle(clientID, "Cuboid", sim.simx_opmode_blocking)
    r, cube0 = sim.simxGetObjectHandle(clientID, "Cuboid0", sim.simx_opmode_blocking)
    r, cube1 = sim.simxGetObjectHandle(clientID, "Cuboid1", sim.simx_opmode_blocking)
    r, cube2 = sim.simxGetObjectHandle(clientID, "Cuboid2", sim.simx_opmode_blocking)
    r, cube3 = sim.simxGetObjectHandle(clientID, "Cuboid3", sim.simx_opmode_blocking)
    r, cube4 = sim.simxGetObjectHandle(clientID, "Cuboid4", sim.simx_opmode_blocking)
    r, cube5 = sim.simxGetObjectHandle(clientID, "Cuboid5", sim.simx_opmode_blocking)
    r, cube6 = sim.simxGetObjectHandle(clientID, "Cuboid6", sim.simx_opmode_blocking)
    r, cube7 = sim.simxGetObjectHandle(clientID, "Cuboid7", sim.simx_opmode_blocking)
    r, cube8 = sim.simxGetObjectHandle(clientID, "Cuboid8", sim.simx_opmode_blocking)
    r, link1 = sim.simxGetObjectHandle(clientID, "IRB4600_link6", sim.simx_opmode_blocking)

    cubeList = [cube, cube0, cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8]
    cubeVector = []
    positionVector = []


    for i in range(1000):
        r, target_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
        r, target_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)
    target_vec = target_pos + target_or


    for x in range(len(cubeList)) :
        for i in range(2000):
            r, cubePos = sim.simxGetObjectPosition(clientID, cubeList[x], -1, sim.simx_opmode_streaming)
            r, cubeOri = sim.simxGetObjectOrientation(clientID, cubeList[x], -1, sim.simx_opmode_streaming)
        print(cubeOri)
        RcubeOri = [ (cubeOri[0]-3.1415927410125732) , cubeOri[1] , cubeOri[2] ]
        cubeVector.append( cubePos + RcubeOri )


    a = 0
    b = 0
    for x in range(len(cubeList)) :
        if x == 4 :
            a = 1
            b = 0
        elif x == 8 :
            a = 2
            b = 0
        positionVector.append([ (0.5-(0.1*a)), (0.5-(0.1*b)), 0.05, -3.1415927410125732, 0.0, 0.0])
        b = b + 1
        # print(i , positionVector , \n)


    position1 = [0, 0, 0.05, - 3.1415, 0.0, 0.0]
    position2 = [0, -0.1 ,0.05, - 3.1415, 0.0, 0.0]
    position3 = [0, -0.2 ,0.05, - 3.1415, 0.0, 0.0]
    position4 = [0, -0.3 ,0.05, - 3.1415, 0.0, 0.0]



# moving function -----------------------------
    def move(arm, cube, currentVec, desVec):
        if desVec == target_vec :
            desVec[3] = 0.0
            desVec[4] = 1.570451021194458
            desVec[5] = 0.0

        piece = []
        for x in range(6):
            piece.append( (desVec[x] - currentVec[x])/50 )

        for i in range(50):
            newVec = []
            for x in range(6):
                newVec.append( currentVec[x] + piece[x] )

            currentVec = newVec
            for i in range(1000):
                sim.simxSetObjectPosition(clientID, arm, -1, newVec[0:3], sim.simx_opmode_oneshot)
            for i in range(1000):
                sim.simxSetObjectOrientation(clientID, arm, -1, newVec[3:6], sim.simx_opmode_oneshot)


        for i in range(1000):
            sim.simxSetObjectPosition(clientID, arm, -1, desVec[0:3], sim.simx_opmode_oneshot)
            sim.simxSetObjectOrientation(clientID, arm, -1, desVec[3:6], sim.simx_opmode_oneshot)
#--------------------------------------



# method calling function ---------------------------
    def start(arm, cube, armVec, cubeVec, positionVec):
        move(arm, cube, armVec, cubeVec)
        sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
        move(arm, cube, cubeVec, armVec)
        move(arm, cube, armVec, positionVec)
        sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
        move(arm, cube, positionVec, armVec)
#------------------------------------------------






    start(target, cubeList[0], target_vec, cubeVector[0], positionVector[0])
    start(target, cubeList[1], target_vec, cubeVector[1], positionVector[1])
    start(target, cubeList[2], target_vec, cubeVector[2], positionVector[2])
    start(target, cubeList[3], target_vec, cubeVector[3], positionVector[3])
    start(target, cubeList[4], target_vec, cubeVector[4], positionVector[4])
    start(target, cubeList[5], target_vec, cubeVector[5], positionVector[5])
    start(target, cubeList[6], target_vec, cubeVector[6], positionVector[6])
    start(target, cubeList[7], target_vec, cubeVector[7], positionVector[7])
    start(target, cubeList[8], target_vec, cubeVector[8], positionVector[8])






    sim.simxFinish(clientID)

else:
    print("Failed connecting to remote API server")


print("program ended")
