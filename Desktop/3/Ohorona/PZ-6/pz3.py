



S1 = 160
S2 = 78
h1 = 2.5
h2 = 2.3
Sod = 0.5
Sdop1 = 35
Sdop2 = 25

Mn1 = S1/Sod
Mn2 = S2/Sod
print("Mn1 = ", Mn1, "osib")
print("Mn2 = ", Mn2, "osib")

Mo1 = ((S1+Sdop1)*h1)/1.5
Mo2 = ((S2+Sdop2)*h2)/1.5
print("Mo1 = ", Mo1, "osib")
print("Mo2 = ", Mo2, "osib")

min = Mn1+Mn2
print("min+10% = ",min+15+32)


print("============== I ===============")
n = 2
Npov1 = n*1200/8
n = 1
Npov2 = n*1200/8
print("Npov1 = ", Npov1)
print("Npov2 = ", Npov2)
print("============== II ==============")
n = 2
Npov1 = n*300/2
n = 1
Npov2 = n*300/2
print("Npov1 = ", Npov1)
print("Npov2 = ", Npov2)
print("================================")


T = 3
Vshov1 = 2800
Vshov2 = 1300
Vod = 3

Nvod1 = Vshov1/(Vod * T)
Nvod2 = Vshov2/(Vod * T)
print("Nvod1 = ", Nvod1)
print("Nvod2 = ", Nvod2)
print("================================")
print("zapas vodu:")

print("1 basement =  ", 19*3*3, "L")
print("2 basement =  ", 6*3*3, "L")
