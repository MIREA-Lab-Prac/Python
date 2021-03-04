def f23(b):
    index = 0
    index2 = 0
    for i in range(len(b)-1,-1,-1):
        if(b[i][0] == None):
            del b[i]
    for k in b:
        if(None in k):
            index = k.index(None)
            del k[index]

    for i in range(len(b)):
        b[i][0] = b[i][0].replace("-","")
        index = b[i][0].find("(")
        index2 = b[i][0].find(")")
        s = b[i][0][index:index2+2]
        b[i][0] = b[i][0].replace(s,"")

        li = b[i][1].split("-")
        b[i][1] = "".join(li[2] + "-" + li[1] + "-" +li[0])

        b[i][2] = b[i][2].replace("%", "")
        q = list(b[i][2])
        print(q)
        if(len(q) == 2):
            if (int(q[1]) >= 5):
                e = float(q[0]) / 10
                e += 0.1
                e = round(e, 1)
                b[i][2] = str(e)
            else:
                b[i][2] = str(float(q[0]) / 10)
        else:
            if (int(q[0]) >= 5):
                b[i][2] = str(0.1)
            else:
                b[i][2] = str(0.0)

            #if (int(q[0]) >= 5):
                #e = float(q[0]) / 10 + 0.1
                #e = round(e, 1)
                #e += 0.1
                #b[i][2] = str(e)
            #else:
                #e = float(q[0]) / 10 + 0.1
                #e = round(e, 1)
                #e = e - e + 0.1
                #b[i][2] = str(e)

        b[i][3] = b[i][3].replace("@","[at]")

    return b
"""a = ([['(467) 963-7730', '19-12-1999', '16%', None, 'tamerlan62@rambler.ru'], [None, None, None, None, None], ['(764) 620-3724', '20-04-2000', '5%', None, 'vavov88@gmail.com'], ['(013) 620-9806', '15-01-2003', '9%', None, 'bikuzin97@mail.ru'], ['(941) 022-3174', '10-08-2002', '16%', None, 'fagulak50@mail.ru']])"""
"""a = [
        ["(480) 095-0802", "02-10-1999", "26%", None, "zevurman14@yandex.ru"],
        ["(810) 192-1018", "05-06-2002", "45%", None, "duzesberg24@mail.ru"],
        [None, None,None, None, None],
        [None, None,None, None, None],
        ["(268) 286-7155", "01-06-2000", "65%", None,"duzesberg24@mail.ru"],
        ["(294) 359-9668", "22-12-2000", "14%", None, "tacizev99@yandex.ru"]
    ]
l = f23(a)
print(l)"""