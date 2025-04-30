from math import sqrt
para = str(input().replace(",","")).split()
parb = str(input().replace(",","")).split()
parc = str(input().replace(",","")).split()

#tratamento se input = "(x,y)"
para = str(para).strip("['']").strip("()")
parb = str(parb).strip("['']").strip("()")
parc = str(parc).strip("['']").strip("()")

xa = int(para[0])
ya = int(para[1])
xb = int(parb[0])
yb = int(parb[1])
xc = int(parc[0])
yc = int(parc[1])

dab = sqrt((xa-xb)** 2 + (ya-yb) **2)
dac = sqrt((xa-xc)** 2 + (ya-yc) **2)
dbc = sqrt((xb-xc)** 2 + (yb-yc) **2)

if (dab > dac+dbc) or  (dac > dab+dbc) or (dbc > dab+dac) or ya==yb==yc or xa==xb==xc:
    print("triângulo inexistente")
else: 
    if dab == dac == dbc:
        print("triângulo equilátero")
    elif dab != dac != dbc and dbc != dab:
        print("triângo escaleno")
    else: 
        print("triângulo isósceles")
