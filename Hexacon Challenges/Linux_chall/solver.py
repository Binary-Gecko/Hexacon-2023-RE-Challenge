from z3 import *

s = Solver()

for i in range(56):
    globals()['a%i' % i] = BitVec('a%i' % i, 32)
    # Ensure only ASCII input
    s.add(globals()['a%i' % i] >= 33)
    s.add(globals()['a%i' % i] <= 126)

s.add(a0 == 68)
s.add(a3 ^ a5 ^ a11 ^ a15 ^ a20 ^ a22 ^ a26 ^ a36 ^ a45 ^ a50 == 108)
s.add(a0-a3 == -5)
s.add(a35 == a44)
s.add(a4*2+a6 == 294)
s.add(a3+a7+1337*a8 == 147192)
s.add(a9+2*a11-a10-a3 == 181)
s.add(a9*2+a0 == 282)
s.add(a11+a12 == 169)
s.add(a44 == a49)
s.add(a8+a15+1337+a0 == 1624)
s.add(a14*2+a13+a0 == 375)
s.add(a1 == 67)
s.add((a16 << 1 & a18 >> 1)^a17^a1 == 39)
s.add(a16+a1 == 164)
s.add(a20+a15-a16 == 64)
s.add(a4 == 95)
s.add(a19+a15+1337*a18 == 68391)
s.add(~(0xc0de*a19)+a17 == -4690431)
s.add(a22+2*a21-a16-a17 == 59)
s.add(a23+a15-a22 == 92)
s.add((a22 << 1 & a24 >> 1)^a23^a21 == 110)
s.add(a23 == 49)
s.add(a24-a2 == -24)
s.add(a4 == a10)
s.add(a26+2*a24 == 251)
s.add(a25+2*a26-a28-a29 == 154)
s.add(a28 == 108)
s.add(a30+a25-a16 == 113)
s.add(a2 == 95)
s.add((a31 << 1 & a33 >> 1)^a2^a32 == 16)
s.add(~(0xc0de*a30)+a0 == -5677943)
s.add(a30+a0 == 183)
s.add(a30+a27+1337+a34 == 1608)
s.add(a31+2*a34-a32-a33 == -3)
s.add(a10 == a14)
s.add(a2+a35+1337+a33 == 1637)
s.add(a37-a2 == -44)
s.add(a36+a15+1337+a0 == 1596)
s.add(a36+a37+1337*a2 == 127148)
s.add(a34 == a39)
s.add(a14 == a19)
s.add(a34+a37-a38 == 16)
s.add(a39*2+a36 == 184)
s.add((a38 << 1 & a39 >> 1)^a40^a1 == 25)
s.add(a39+2*a41-a40-a43 == 53)
s.add(a42+a45+1337*a37 == 68313)
s.add(a41 == 83)
s.add(a46 == 51)
s.add(a19 == a21)
s.add(a55 == 125)
s.add(a14 ^ a25 ^ a31 ^ a52 ^ a21 ^ a18 ^ a27 ^ a39 ^ a49 ^ a53 == 66)
s.add(a55-a47 == 74)
s.add(a45 == 75)
s.add(a21 == a25)
s.add((a46 << 1 & a48 >> 1)^a49^a47 == 76)
s.add(~(0xc0de*a48)+a55 == -5529764)
s.add(a49+2*a51-a50-a53 == 10)
s.add(a55+a54-a52 == 179)
s.add(a55*2+a52 == 299)
s.add(a25 == a35)
s.add(a46+a54+1337*a51 == 64330)
s.add(a53+a55+1337+a0 == 1640)

##flag: DC{I_th1nk_y0u_mad3_4_B1G_mil3ston3_R3V3RS3R_K33p_G01ng} NOOOOOOOOOOOOOOOOOO
##flag: FLAG{DC_I_th1nk_y0u_mad3_4_B1G_mil3ston3_R3V3RS3R_K33p_G01ng}

print(s.check())
print(s.model())
modl = s.model()
res=""
for i in range(56):
    obj = globals()['a%i' % i]
    c = modl[obj].as_long()
    res = res + chr(c)
print(res)







 