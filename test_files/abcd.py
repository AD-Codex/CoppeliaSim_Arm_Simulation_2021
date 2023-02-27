# changingPoint = [ [0,0,"Y"], [0,2,"R"], [0,3,"Y"], [0,4,"En"], [1,5,"Y"], [1,7,"R"],  [1,9,"En"], [2,10,"Y"], [2,12,"R"], [2,13,"G"], [2,14,"Y"] ]
#
# curPoint = changingPoint[0]
# curr = changingPoint[0]
# x = 0
#
# for i in range(14):
#     if curr[1] == i:
#         # print(curr)
#         # print(x)
#         curPoint = []
#         curPoint = curr
#         if curPoint[2] == "En":
#             curPoint[2] = "Y"
#
#         x = x + 1
#         curr = []
#         curr = changingPoint[x]
#         # print("curr", curr)
#
#     else:
#         row = curPoint[0]
#         color = curPoint[2]
#         curPoint = []
#         curPoint = [row , i, color ]
#
#     print(curPoint)
#
#
#
#
#
# print(curr)

Ycube = []
num = 0
for x in range(466,-1,-1):
    cuboid = "Cuboid" + str(x)
    Ycube.append( cuboid )
    num = num + 1

Ycube.append("Cuboid")
print(Ycube)
