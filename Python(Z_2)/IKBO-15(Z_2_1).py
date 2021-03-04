def f21(a):
    num = 0
    T = [
         [0,1,2],
         [0,0,0],
         [0,11],
         [0,9,10],
         [3,4,5],
         [6,7,8]
        ]
    if (a[3] == 1961):
        if(num < T[2][0]):
            num = T[2][0]
    if (a[3] == 1985):
        if(num < T[2][1]):
            num = T[2][1]

    if (a[2] == "nim"):
        if(num < T[3][0]):
            num = T[3][0]
    if (a[2] == "sqlpl"):
        if(num < T[3][1]):
            num = T[3][1]
    if (a[2] == "tcsh"):
        if(num < T[3][2]):
            num = T[3][2]

    if(a[0] == "ston" and a[1] == "nl"):
        if(num < T[0][0]):
            num = T[0][0]
    if (a[0] == "mtml" and a[1] == "nl"):
        if(num < T[0][1]):
            num = T[0][1]
    if (a[0] == "cirru" and a[1] == "nl"):
        if(num < T[0][2]):
            num = T[0][2]



    if (a[4] == "e" and a[1] == "c"):
        if(num < T[4][0]):
            num = T[4][0]
    if (a[4] == "nim" and a[1] == "c"):
        if(num < T[4][1]):
            num = T[4][1]
    if (a[4] == "fish" and a[1] == "c"):
        if(num < T[4][2]):
            num = T[4][2]
    if (a[4] == "e" and a[1] == "mirah"):
        if(num < T[5][0]):
            num = T[5][0]
    if (a[4] == "nim" and a[1] == "mirah"):
        if(num < T[5][1]):
            num = T[5][1]
    if (a[4] == "fish" and a[1] == "mirah"):
        if(num < T[5][2]):
            num = T[5][2]
    return num
