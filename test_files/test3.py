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
    r, link1 = sim.simxGetObjectHandle(clientID, "IRB4600_link6", sim.simx_opmode_blocking)



    for i in range(2000):
        r, target_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
        r, target_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)
    target_vec = target_pos + target_or


    for i in range(2000):
        r, cube_or = sim.simxGetObjectOrientation(clientID, cube, -1, sim.simx_opmode_streaming)
        r, cube_pos = sim.simxGetObjectPosition(clientID, cube, -1, sim.simx_opmode_streaming)
    Rcube_or = [ (cube_or[0]-3.1415) , cube_or[1] , cube_or[2] ]
    cube_vec = cube_pos + Rcube_or



    for i in range(2000):
        r, cube0_or = sim.simxGetObjectOrientation(clientID, cube0, -1, sim.simx_opmode_streaming)
        r, cube0_pos = sim.simxGetObjectPosition(clientID, cube0, -1, sim.simx_opmode_streaming)
    Rcube0_or = [ (cube0_or[0]-3.1415) , cube0_or[1] , cube0_or[2] ]
    cube0_vec = cube0_pos + Rcube0_or

    # for i in range(2000):
    #     r, cube1_or = sim.simxGetObjectOrientation(clientID, cube1, -1, sim.simx_opmode_streaming)
    #     r, cube1_pos = sim.simxGetObjectPosition(clientID, cube1, -1, sim.simx_opmode_streaming)
    #
    # for i in range(2000):
    #     r, cube2_or = sim.simxGetObjectOrientation(clientID, cube2, -1, sim.simx_opmode_streaming)
    #     r, cube2_pos = sim.simxGetObjectPosition(clientID, cube2, -1, sim.simx_opmode_streaming)


    position1 = [0, 0, 0.05, - 3.1415, 0.0, 0.0]
    position2 = [0, -0.1 ,0.05, - 3.1415, 0.0, 0.0]
    position3 = [0, -0.2 ,0.05]
    position4 = [0, -0.3 ,0.05]



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
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, arm, -1, newVec[0:3], sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, arm, -1, newVec[3:6], sim.simx_opmode_oneshot)


        for i in range(2000):
            sim.simxSetObjectPosition(clientID, arm, -1, desVec[0:3], sim.simx_opmode_oneshot)
            sim.simxSetObjectOrientation(clientID, arm, -1, desVec[3:6], sim.simx_opmode_oneshot)


    def start(arm, cube, armVec, cubeVec, positionVec):
        move(arm, cube, armVec, cubeVec)
        sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
        move(arm, cube, cubeVec, armVec)
        move(arm, cube, armVec, positionVec)
        sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
        move(arm, cube, positionVec, armVec)



    # move(target, cube, target_vec, cube_vec)
    # sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
    # move(target, cube, cube_vec, target_vec)
    # move(target, cube, target_vec, position1)
    # sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
    # move(target, cube, position1, target_vec)

    start(target, cube, target_vec, cube_vec, position1)
    start(target, cube0, target_vec, cube0_vec, position2)

    # move(target, cube0, target_vec, cube0_vec)
    # sim.simxSetObjectParent(clientID, cube0, link1, True, sim.simx_opmode_oneshot)
    # move(target, cube0, cube0_vec, target_vec)
    # move(target, cube0, target_vec, position2)
    # sim.simxSetObjectParent(clientID, cube0, -1, True, sim.simx_opmode_oneshot)
    # move(target, cube0, position2, target_vec)









    sim.simxFinish(clientID)

else:
    print("Failed connecting to remote API server")


print("program ended")
