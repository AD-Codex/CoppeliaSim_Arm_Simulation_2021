import sim
import time

sim.simxFinish(-1)
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)

print ('Program started')



Rcube = ["Cuboid"]
for x in range(179):
    cuboid = "Cuboid" + str(x)
    Rcube.append( cuboid )

Ycube = []
num = 0
for x in range(225):
    cuboid = "Cuboid" + str(181 + num)
    Ycube.append( cuboid )
    num = num + 1

Ocube = []
num = 0
for x in range(32):
    cuboid = "Cuboid" + str(442 + num)
    Ocube.append( cuboid )
    num = num + 1

Gcube = []
num = 0
for x in range(32):
    cuboid = "Cuboid" + str(406 + num)
    Gcube.append( cuboid )
    num = num + 1





if clientID!=-1:
    print("Connected to remote API server")

    r, target = sim.simxGetObjectHandle( clientID , "IRB4600_IkTarget", sim.simx_opmode_blocking)
    r, link1 = sim.simxGetObjectHandle(clientID, "IRB4600_link6", sim.simx_opmode_blocking)

# Handle Cuboids -------------------------------------------------
    RcubeList = []
    YcubeList = []
    OcubeList = []
    GcubeList = []

    for cube in Rcube :
        r, cuboid = sim.simxGetObjectHandle(clientID, cube, sim.simx_opmode_blocking)
        RcubeList.append(cuboid)

    for cube in Ycube :
        r, cuboid = sim.simxGetObjectHandle(clientID, cube, sim.simx_opmode_blocking)
        YcubeList.append(cuboid)

    for cube in Ocube :
        r, cuboid = sim.simxGetObjectHandle(clientID, cube, sim.simx_opmode_blocking)
        OcubeList.append(cuboid)

    for cube in Gcube :
        r, cuboid = sim.simxGetObjectHandle(clientID, cube, sim.simx_opmode_blocking)
        GcubeList.append(cuboid)
# ----------------------------------------------------------

    # print(RcubeList)
    # print(YcubeList)
    # print(OcubeList)
    # print(GcubeList)

 # target reading ---------------------------------------
    for i in range(2000):
        r, target_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
        r, target_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)
    if target_or == [0,0,0]:
        for i in range(4000):
            r, target_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
            r, target_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)
    print(target_or)
# --------------------------------------------------------

#  variable for cube reading -------------------------------
    Rcube_pos = []
    Rcube_ori = []
    Ycube_pos = []
    Ycube_ori = []
    Ocube_pos = []
    Ocube_ori = []
    Gcube_pos = []
    Gcube_ori = []
    position = []
    orientation0 = [ 0.0, 0.0 , 0.0]
    orientation2 = [ -3.141592502593994, 0.0 , 0.0]

#  cube reading ---------------------------------------------
    for x in range(len( RcubeList )) :
        for i in range(2000):
            r, cubePos = sim.simxGetObjectPosition(clientID, RcubeList[x], -1, sim.simx_opmode_streaming)
            r, cubeOri = sim.simxGetObjectOrientation(clientID, RcubeList[x], -1, sim.simx_opmode_streaming)
        if cubePos == []:
            for i in range(4000):
                r, cubePos = sim.simxGetObjectPosition(clientID, RcubeList[x], -1, sim.simx_opmode_streaming)
                r, cubeOri = sim.simxGetObjectOrientation(clientID, RcubeList[x], -1, sim.simx_opmode_streaming)
        Rcube_pos.append( cubePos )
        Rcube_ori.append( cubeOri )

    for x in range(len( YcubeList )) :
        for i in range(2000):
            r, cubePos = sim.simxGetObjectPosition(clientID, YcubeList[x], -1, sim.simx_opmode_streaming)
            r, cubeOri = sim.simxGetObjectOrientation(clientID, YcubeList[x], -1, sim.simx_opmode_streaming)
        if cubePos == []:
            for i in range(4000):
                r, cubePos = sim.simxGetObjectPosition(clientID, YcubeList[x], -1, sim.simx_opmode_streaming)
                r, cubeOri = sim.simxGetObjectOrientation(clientID, YcubeList[x], -1, sim.simx_opmode_streaming)
        Ycube_pos.append( cubePos )
        Ycube_ori.append( cubeOri )

    for x in range(len( OcubeList )) :
        for i in range(2000):
            r, cubePos = sim.simxGetObjectPosition(clientID, OcubeList[x], -1, sim.simx_opmode_streaming)
            r, cubeOri = sim.simxGetObjectOrientation(clientID, OcubeList[x], -1, sim.simx_opmode_streaming)
            if cubePos == []:
                for i in range(4000):
                    r, cubePos = sim.simxGetObjectPosition(clientID, OcubeList[x], -1, sim.simx_opmode_streaming)
                    r, cubeOri = sim.simxGetObjectOrientation(clientID, OcubeList[x], -1, sim.simx_opmode_streaming)
        Ocube_pos.append( cubePos )
        Ocube_ori.append( cubeOri )

    for x in range(len( GcubeList )) :
        for i in range(2000):
            r, cubePos = sim.simxGetObjectPosition(clientID, GcubeList[x], -1, sim.simx_opmode_streaming)
            r, cubeOri = sim.simxGetObjectOrientation(clientID, GcubeList[x], -1, sim.simx_opmode_streaming)
        if cubePos == []:
            for i in range(4000):
                r, cubePos = sim.simxGetObjectPosition(clientID, GcubeList[x], -1, sim.simx_opmode_streaming)
                r, cubeOri = sim.simxGetObjectOrientation(clientID, GcubeList[x], -1, sim.simx_opmode_streaming)
        Gcube_pos.append( cubePos )
        Gcube_ori.append( cubeOri )
# -------------------------------------

    print("----------------satrted-------------------------- ")

    # print(Rcube_pos)
    # print(Ycube_pos)
    # print(Ocube_pos)
    # print(Gcube_pos)


# arm move_1 function ------------------------------------------
    def move_1(object1, currentPos, newPos, newOri):
        print(newPos)
        new = [ newPos[0], newPos[1], 0.225  ]
        vec = []
        for x in range(3):
            vec.append( (new[x] - currentPos[x])/20 )

        for i in range(20):
            pos = []
            for x in range(3):
                pos.append( currentPos[x] + vec[x] )

            currentPos = pos
            for i in range(1000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, orientation2, sim.simx_opmode_oneshot)
        for x in range(11):
            pos = [ newPos[0], newPos[1], 0.225 - 0.02 * x  ]
            for i in range(1000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, orientation2, sim.simx_opmode_oneshot)
# -----------------------------------------------------------------------------------

# arm move_2 function ------------------------------------------
    def move_2(object1, currentPos, newPos, newOri):
        for x in range(11):
            pos = [ currentPos[0], currentPos[1], 0.025000 + 0.02 * x  ]
            for i in range(1000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, orientation2, sim.simx_opmode_oneshot)

        current = [ currentPos[0], currentPos[1], 0.225 ]
        vec = []
        for x in range(3):
            vec.append( (newPos[x] - current[x])/20 )
        for i in range(20):
            pos = []
            for x in range(3):
                pos.append( current[x] + vec[x] )

            current = pos
            for i in range(1000):
                sim.simxSetObjectPosition(clientID, object1, -1, pos, sim.simx_opmode_oneshot)
                sim.simxSetObjectOrientation(clientID, object1, -1, orientation2, sim.simx_opmode_oneshot)
# -----------------------------------------------------------------------------------

# cube move function -----------------------------------------
    def start(cube, cubePos, cubeOri, position):
        move_1(target, target_pos, cubePos, cubeOri)
        sim.simxSetObjectParent(clientID, cube, link1, True, sim.simx_opmode_oneshot)
        move_2(target, cubePos, target_pos, cubeOri)
        move_1(target, target_pos, position, orientation0)
        sim.simxSetObjectParent(clientID, cube, -1, True, sim.simx_opmode_oneshot)
        move_2(target, position, target_pos, target_or)
#  -------------------------------------------------------------

# cube place function ---------------------------------------
    def place(point):
        global YCnum
        global RCnum
        global GCnum
        global OCnum
        global position

        column = point[0]
        if point[2] == "Y" or point[2] == "En":
            start( YcubeList[YCnum], Ycube_pos[YCnum], Ycube_ori[YCnum], position )
            YCnum = YCnum + 1
        elif point[2] == "R":
            start( RcubeList[RCnum], Rcube_pos[RCnum], Rcube_ori[RCnum], position )
            RCnum = RCnum + 1
        elif point[2] == "G":
            start( GcubeList[GCnum], Gcube_pos[GCnum], Gcube_ori[GCnum], position )
            GCnum = GCnum + 1
        elif point[2] == "O":
            start( OcubeList[OCnum], Ocube_pos[OCnum], Ocube_ori[OCnum], position )
            OCnum = OCnum + 1
# ------------------------------------------------------------------------------


# flag changing points -----------------------------------------------------
    changingPoint = [ [0,0,"Y"],[0,17,"En"],
    [1,18,"Y"],[1,19,"R"],[1,35,"En"],
    [2,36,"Y"],[2,37,"R"],[2,38,"Y"],[2,39,"R"],[2,51,"Y"],[2,52,"R"],[2,53,"En"],
    [3,54,"Y"],[3,55,"R"],[3,59,"Y"],[3,60,"R"],[3,61,"Y"],[3,64,"R"],[3,65,"Y"],[3,68,"R"],[3,71,"En"],
    [4,72,"Y"],[4,73,"R"],[4,74,"Y"],[4,75,"R"],[4,76,"Y"],[4,77,"R"],[4,78,"Y"],[4,88,"R"],[4,89,"En"],
    [5,90,"Y"],[5,91,"R"],[5,92,"Y"],[5,93,"R"],[5,94,"Y"],[5,95,"R"],[5,96,"Y"],[5,103,"R"],[5,105,"Y"],[5,106,"R"],[5,107,"En"],
    [6,108,"Y"],[6,109,"R"],[6,110,"Y"],[6,111,"R"],[6,112,"Y"],[6,113,"R"],[6,114,"Y"],[6,121,"R"],[6,125,"En"],
    [7,126,"Y"],[7,127,"R"],[7,129,"Y"],[7,130,"R"],[7,132,"Y"],[7,142,"R"],[7,143,"En"],
    [8,144,"Y"],[8,145,"R"],[8,151,"Y"],[8,156,"R"],[8,159,"Y"],[8,160,"R"],[8,161,"En"],
    [9,162,"Y"],[9,163,"R"],[9,168,"Y"],[9,174,"R"],[9,179,"En"],
    [10,180,"Y"],[10,181,"R"],[10,186,"Y"],[10,192,"R"],[10,197,"En"],
    [11,198,"Y"],[11,199,"R"],[11,201,"Y"],[11,202,"R"],[11,203,"Y"],[11,214,"R"],[11,215,"En"],
    [12,216,"Y"],[12,217,"R"],[12,218,"Y"],[12,219,"R"],[12,220,"Y"],[12,229,"R"],[12,231,"Y"],[12,232,"R"],[12,233,"En"],
    [13,234,"Y"],[13,235,"R"],[13,236,"Y"],[13,246,"R"],[13,251,"En"],
    [14,252,"Y"],[14,253,"R"],[14,254,"Y"],[14,256,"R"],[14,257,"Y"],[14,259,"R"],[14,263,"Y"],[14,264,"R"],[14,269,"En"],
    [15,270,"Y"],[15,271,"R"],[15,273,"Y"],[15,274,"R"],[15,275,"Y"],[15,277,"R"],[15,282,"Y"],[15,283,"R"],[15,287,"En"],
    [16,288,"Y"],[16,289,"R"],[16,299,"Y"],[16,300,"R"],[16,305,"En"],
    [17,306,"Y"],[17,307,"R"],[17,310,"Y"],[17,319,"R"],[17,323,"En"],
    [18,324,"Y"],[18,325,"R"],[18,326,"Y"],[18,327,"R"],[18,334,"Y"],[18,335,"R"],[18,339,"Y"],[18,340,"R"],[18,341,"En"],
    [19,342,"Y"],[19,343,"R"],[19,359,"En"],
    [20,360,"Y"],[20,377,"En"],
    [21,378,"Y"],[21,379,"O"],[21,395,"En"],
    [22,396,"Y"],[22,397,"O"],[22,413,"En"],
    [23,414,"Y"],[23,415,"G"],[23,431,"En"],
    [24,432,"Y"],[24,433,"G"],[24,449,"En"],
    [25,450,"Y"],[25,467,"En"]    ]
# --------------------------------------------------------------------------------


# flage makig function --------------------------------------------
    curPoint = changingPoint[0]
    curr = changingPoint[0]
    x = 0
    YCnum = 0
    RCnum = 0
    GCnum = 0
    OCnum = 0
    y = 0
    end = ""

    for i in range(467):
        if curr[1] == i:
            curPoint = []
            curPoint = curr
            x = x + 1
            curr = []
            curr = changingPoint[x]
        else:
            row = curPoint[0]
            color = curPoint[2]
            curPoint = []
            curPoint = [row , i, color ]

        print(curPoint)
        position = [ 0.0 + 0.05*curPoint[0] , -3 + 0.05*y , 0.025 ]
        print(position)
        y = y + 1
        place(curPoint)
        if curPoint[2] == "En":
            y = 0
    position = [ 0.0 + 0.05*curPoint[0] , -3 + 0.05*y , 0.025 ]
    place(curr)
# -----------------------------------------------------------------------






    sim.simxFinish(clientID)

else:
    print("Failed connecting to remote API server")


print("program ended")
