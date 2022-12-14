# -*- coding: utf-8 -*-
"""coolingTower.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BYI9OmUeiUD11iDLwQmaDC9awMNK_4zn
"""

h1 = float(input("Enter h1 in cm : "))
h2 = float(input("Enter h2 in cm : "))
T1 = float(input("Enter dry bulb inlet temperature (T1) : "))
T2 = float(input("Enter wet bulb inlet temperature (T2) : "))
T3 = float(input("Enter dry bulb outlet temperature (T3) : "))
T4 = float(input("Enter wet bulb inlet temperature (T4) : "))
T5 = float(input("Enter inlet water temperature (T5) : "))
T6 = float(input("Enter outlet water temperature (T6) : "))
Fw = float(input("Enter flow rate of water in LPH : "))
den_water = float(input("Enter density of water : "))
den_air = float(input("Enter density of air : "))
cd = float(input("Enter coefficient of discharge : "))
a1 = float(input("Enter area of orifice(a1) : "))
a2 = float(input("Enter area of orifice(a2) : "))
g = float(input("Enter acceleration due to gravity : "))

Range = T5-T6
print("Range =",round(Range,3))

approach = T6-T2
print("Approach =",round(approach,3))

effectiveness = (Range/(Range+approach))*100
print("Effectiveness =",round(effectiveness,3))

H = ((h1-h2)/100)*((den_water/den_air)-1)
print("Head in terms of air =",round(H,3))

Qa = cd*((a1*a2)/((a2**2)-(a1**2))**(1/2))*((2*g*H)**(1/2))
print("Flow rate of air in m3/sec (Qa) =",round(Qa,3))

G = Qa*3600
print("Flow rate of air in m3/hr (G) =",round(G,3))

L = Fw/1000
print("Flow rate of water (L) =",round(L,3))

L_G = L/G
print("L/G ratio =",round(L_G,3))

El = 0.00085*1.8*L*Range
print("Evaporation loss (El) =",round(El,3))

percent_El = (El)/(L)*100
print("Percentage vaporation loss =",round(percent_El,3))

Bd = 0.2*El
print("Blow down losses =",round(Bd))

Dl = 0.002*L
print("Drift losses =",round(Dl))

M = El+Bd+Dl
print("Makeup water requirement =",round(M,3))