import sim
import time

sim.simxFinish(-1)
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)

print ('Program started')

cuboid = "Cuboid"
cuboid0 = "Cuboid0"

if clientID!=-1:
    print("Connected to remote API server")

    r, target = sim.simxGetObjectHandle( clientID , "IRB4600_IkTarget", sim.simx_opmode_blocking)
    r, cube1 = sim.simxGetObjectHandle(clientID, cuboid, sim.simx_opmode_blocking)
    r, cube2 = sim.simxGetObjectHandle(clientID, cuboid0, sim.simx_opmode_blocking)
    r, link1 = sim.simxGetObjectHandle(clientID, "IRB4600_link6", sim.simx_opmode_blocking)
    r, irSensor = sim.simxGetObjectHandle(clientID, "Vision_sensor", sim.simx_opmode_blocking)
    # print(target)
    # print(cube1)
    # print(link1)

    for i in range(2000):
        r, old_or = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_streaming)
        r, old_pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_streaming)
    # print(old_or)
    # print(old_pos)

    for i in range(2000):
        r, des_or = sim.simxGetObjectOrientation(clientID, cube1, -1, sim.simx_opmode_streaming)
        r, des_pos = sim.simxGetObjectPosition(clientID, cube1, -1, sim.simx_opmode_streaming)
    # print(des_or)
    # print(des_pos)

    for i in range(2000):
        r, pos = sim.simxGetObjectPosition(clientID, cube2, -1, sim.simx_opmode_streaming)
    # print(pos)

    for i in range(2000):
        sim.simxSetObjectPosition(clientID, target, -1, des_pos, sim.simx_opmode_oneshot)
        sim.simxSetObjectOrientation(clientID, target, -1, des_or, sim.simx_opmode_oneshot)

    for i in range(2000):
        r, x , y = sim.simxReadVisionSensor(clientID, irSensor, sim.simx_opmode_streaming)
        a, b, c = sim.simxGetVisionSensorDepthBuffer(clientID, irSensor, sim.simx_opmode_streaming)

    print(r)
    print(x)
    print(y)

    # print(a)
    # print(b)
    # print(c)


# move to the object ---------------
    # vec_pos = []
    # zip_pos = zip(des_pos, old_pos)
    # for des_i, old_i in zip_pos:
    #     vec_pos.append((des_i-old_i)/50)
    # # print(vec_pos)
    #
    # for i in range(50):
    #     new_pos = []
    #     for x in range(3):
    #         new_pos.append((old_pos[x] + vec_pos[x]))
    #     # print(new_pos)
    #     old_pos = new_pos
    #
    #     for i in range(2000):
    #         sim.simxSetObjectPosition(clientID, target, -1, new_pos, sim.simx_opmode_oneshot)
    #         sim.simxSetObjectOrientation(clientID, target, -1, des_or, sim.simx_opmode_oneshot)
    # print("des_pos--------")
    # print(des_pos)
#----------------------------------------

    # for i in range(2000):
    #     sim.simxSetObjectPosition(clientID, target, -1, des_pos, sim.simx_opmode_oneshot)
    #     sim.simxSetObjectOrientation(clientID, target, -1, des_or, sim.simx_opmode_oneshot)


# make a child of perant ----------------------
    # sim.simxSetObjectParent(clientID, cube1, link1, True, sim.simx_opmode_oneshot)
#------------------------------------------------

# move the object and arm -----------------------
    # vec_pos0 = []
    # zip_pos0 = zip(pos, des_pos)
    # for pos_i, old_i in zip_pos0:
    #     vec_pos0.append((pos_i-old_i)/50)
    #
    # for i in range(50):
    #     new_pos = []
    #     for x in range(3):
    #         new_pos.append((des_pos[x] + vec_pos0[x]))
    #     # print(new_pos)
    #     des_pos = new_pos
    #
    #     for i in range(2000):
    #         sim.simxSetObjectPosition(clientID, target, -1, new_pos, sim.simx_opmode_oneshot)
    # print("pos--------")
    # print(pos)
#-------------------------------------------------------

    # for i in range(2000):
    #     sim.simxSetObjectPosition(clientID, target, -1, pos, sim.simx_opmode_oneshot)

# remove child from perent -------------------
    # sim.simxSetObjectParent(clientID, cube1, -1, True, sim.simx_opmode_oneshot)
#------------------------------------------------


# move to end position--------------------------
    # end_pos = [1,1,1]
    # vec_pos1 = []
    # for x in range(3):
    #     vec_pos1.append((end_pos[x] - pos[x])/50)
    #
    # for i in range(50):
    #     new_pos0 = []
    #     for x in range(3):
    #         new_pos0.append(pos[x] + vec_pos1[x])
    #     print(new_pos0)
    #     pos = new_pos0
    #
    #     for i in range(2000):
    #         sim.simxSetObjectPosition(clientID, target, -1, new_pos0, sim.simx_opmode_oneshot)
    # print("end_pos---------")
#---------------------------------------------------------


    sim.simxFinish(clientID)

else:
    print("Failed connecting to remote API server")


print("program ended")


# old_pos = [4,5,6]
# vec_pos = [1,1,1]
#
#
# for i in range(3):
#     new_pos = []
#     for x in range(3):
#         print(old_pos[x])
#         print(vec_pos[x])
#         new_pos.append(int(old_pos[x]) + int(vec_pos[x]))
#     print(new_pos)
#     old_pos = new_pos
