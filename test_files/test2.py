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
    # r, vaccum = sim.simxGetObjectHandle(clientID, "BaxterVacuumCup", sim.simx_opmode_blocking)
    r, link1 = sim.simxGetObjectHandle(clientID, "IRB4600_link6", sim.simx_opmode_blocking)
    sim.simxSetIntegerSignal(clientID, 'BaxterVacuumCup_active', 0, sim.simx_opmode_oneshot)


    for i in range(4000):
        r, target_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
        r, target_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)

    print(target_or)


    for i in range(4000):
        r, cube_or = sim.simxGetObjectOrientation(clientID, cube, -1, sim.simx_opmode_streaming)
        r, cube_pos = sim.simxGetObjectPosition(clientID, cube, -1, sim.simx_opmode_streaming)

    for i in range(4000):
        r, cube0_or = sim.simxGetObjectOrientation(clientID, cube0, -1, sim.simx_opmode_streaming)
        r, cube0_pos = sim.simxGetObjectPosition(clientID, cube0, -1, sim.simx_opmode_streaming)

    for i in range(2000):
        r, cube1_or = sim.simxGetObjectOrientation(clientID, cube1, -1, sim.simx_opmode_streaming)
        r, cube1_pos = sim.simxGetObjectPosition(clientID, cube1, -1, sim.simx_opmode_streaming)

    for i in range(2000):
        r, cube2_or = sim.simxGetObjectOrientation(clientID, cube2, -1, sim.simx_opmode_streaming)
        r, cube2_pos = sim.simxGetObjectPosition(clientID, cube2, -1, sim.simx_opmode_streaming)


    position1 = [1, 1, 0.025]
    position2 = [1, 1.05 ,0.025]
    position3 = [-1, -1.2 ,0.05]
    position4 = [-1, -1.3 ,0.05]
    orientation1 = [ 0.0, 0.0 , 0.0]
    orientation2 = [ 3.1415927410125732, 0.0 , 0.0]

    for i in range(2000):
        sim.simxSetObjectOrientation(clientID, target, -1, orientation2, sim.simx_opmode_oneshot)




    def move1_1(object1, object2, currentPos, newPos, newOri):
        new = [ newPos[0], newPos[1], 0.2265  ]
        vec = []
        for x in range(3):
            vec.append( (new[x] - currentPos[x])/50 )

        for i in range(50):
            pos = []
            for x in range(3):
                pos.append( currentPos[x] + vec[x] )

            currentPos = pos
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, orientation2, sim.simx_opmode_oneshot)

        ori = (newOri[2] )/10

        for x in range(11):
            cur = [ 3.1415927410125732 , 0, ori*x]
            pos1 = [ newPos[0], newPos[1], 0.2265 - 0.02 * x  ]
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos1, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, cur, sim.simx_opmode_oneshot)
        print(newOri)
        print(newPos)
        print(cur)

    def move2_1(object1, object2, currentPos, newPos, newOri):
        currentOri = (newOri[2] )/10
        if newOri[2] >= 0 :
            currentOri = (3.1415927410125732/2 - newOri[2] )/20
            for x in range(21):
                ori = [3.1415927410125732, 0,currentOri*x]
                pos1 = [ currentPos[0], currentPos[1], 0.027000 + 0.01 * x  ]
                for i in range(2000):
                    sim.simxSetObjectPosition(clientID, object1, -1, pos1, sim.simx_opmode_oneshot)
                    sim.simxSetObjectOrientation(clientID, object1, -1, ori, sim.simx_opmode_oneshot)
        else:
            for x in range(11):
                ori = [3.1415927410125732, 0, newOri[2] -currentOri*x]
                pos1 = [ currentPos[0], currentPos[1], 0.027000 + 0.02 * x  ]
                for i in range(2000):
                    sim.simxSetObjectPosition(clientID, object1, -1, pos1, sim.simx_opmode_oneshot)
                    sim.simxSetObjectOrientation(clientID, object1, -1, ori, sim.simx_opmode_oneshot)

            # print(pos1)

        current = [ currentPos[0], currentPos[1], 0.227 ]
        vec = []
        for x in range(3):
            vec.append( (newPos[x] - current[x])/50 )

        for i in range(50):
            pos = []
            for x in range(3):
                pos.append( current[x] + vec[x] )
            # print(pos)

            current = pos
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, [3.141592502593994, 0.0, 0.0], sim.simx_opmode_oneshot)


    def move1(object1, object2, currentPos, newPos, newOri):
        new = [ newPos[0], newPos[1], 0.125  ]
        vec = []
        for x in range(3):
            vec.append( (new[x] - currentPos[x])/50 )

        for i in range(50):
            pos = []
            for x in range(3):
                pos.append( currentPos[x] + vec[x] )

            currentPos = pos
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, [3.141592502593994, 0.0, 0.0], sim.simx_opmode_oneshot)


        for x in range(25):
            pos1 = [ newPos[0], newPos[1], 0.125 - 0.004 * x  ]
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos1, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, [3.141592502593994, 0.0, 0.0], sim.simx_opmode_oneshot)

    def move2(object1, object2, currentPos, newPos, newOri):
        for x in range(26):
            pos1 = [ currentPos[0], currentPos[1], 0.025000 + 0.004 * x  ]
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos1, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, [3.141592502593994, 0.0, 0.0], sim.simx_opmode_oneshot)
            # print(pos1)

        current = [ currentPos[0], currentPos[1], 0.125 ]
        vec = []
        for x in range(3):
            vec.append( (newPos[x] - current[x])/50 )

        for i in range(50):
            pos = []
            for x in range(3):
                pos.append( current[x] + vec[x] )
            # print(pos)

            current = pos
            for i in range(2000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, [3.141592502593994, 0.0, 0.0], sim.simx_opmode_oneshot)






    move1_1(target, -1, target_pos, cube0_pos, cube0_or)
    sim.simxSetIntegerSignal(clientID, "BaxterVacuumCup_active",  1, sim.simx_opmode_oneshot)
    sim.simxSetObjectParent(clientID, cube0, link1, True, sim.simx_opmode_oneshot)
    move2_1(target, -1, cube0_pos, target_pos, cube0_or)
    move1(target, cube0, target_pos, position1, orientation1)
    sim.simxSetIntegerSignal(clientID, 'BaxterVacuumCup_active', 0, sim.simx_opmode_oneshot)
    sim.simxSetObjectParent(clientID, cube0, -1, True, sim.simx_opmode_oneshot)
    move2(target, -1, position1, target_pos, target_or)

    for i in range(2000):
        sim.simxSetObjectOrientation(clientID, target, -1, orientation2, sim.simx_opmode_oneshot)

    move1_1(target, -1, target_pos, cube_pos, cube_or)
    sim.simxSetIntegerSignal(clientID, "BaxterVacuumCup_active",  1, sim.simx_opmode_oneshot)
    sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
    move2_1(target, -1, cube_pos, target_pos, cube_or)
    # move1(target, cube, target_pos, position2, orientation1)
    # sim.simxSetIntegerSignal(clientID, 'BaxterVacuumCup_active', 0, sim.simx_opmode_oneshot)
    # sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
    # move2(target, -1, position2, target_pos, target_or)


    # sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
    # move(target, -1, target_pos, cube_pos, cube_or)
    # sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
    # move(target, -1, cube_pos, target_pos, cube_or)
    # move(target, cube, target_pos, position1, orientation1)
    # sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
    # move(target, -1, position1, target_pos, target_or)
    #
    #
    #
    #
    # move(target, -1, target_pos, cube0_pos, cube0_or)
    #
    # sim.simxSetObjectParent(clientID, cube0, link1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, cube0_pos, target_pos, cube0_or)
    #
    # move(target, cube0, target_pos, position2, orientation1)
    #
    # sim.simxSetObjectParent(clientID, cube0, -1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, position2, target_pos, target_or)
    #
    #
    #
    #
    # move(target, -1, target_pos, cube1_pos, cube1_or)
    #
    # sim.simxSetObjectParent(clientID, cube1, link1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, cube1_pos, target_pos, cube1_or)
    #
    # move(target, cube1, target_pos, position3, orientation1)
    #
    # sim.simxSetObjectParent(clientID, cube1, -1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, position3, target_pos, target_or)
    #
    #
    #
    # move(target, -1, target_pos, cube2_pos, cube2_or)
    #
    # sim.simxSetObjectParent(clientID, cube2, link1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, cube2_pos, target_pos, cube2_or)
    #
    # move(target, cube2, target_pos, position4, orientation1)
    #
    # sim.simxSetObjectParent(clientID, cube2, -1, True, sim.simx_opmode_oneshot)
    #
    # move(target, -1, position4, target_pos, target_or)






    sim.simxFinish(clientID)

else:
    print("Failed connecting to remote API server")


print("program ended")
