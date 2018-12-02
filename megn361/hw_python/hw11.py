tmax = 1000
cp = 1.005
k = 1.4

r_comp = 4
r_turb = 2

## state 1
p1 = 100
t1 = 300

## state 2 
t2 = t1*r_comp**((k-1)/k)
p2 = p1*r_comp

print("The value of t2 is: \n", t2, "K \n")
print("the pressure at p2 is: ", p2, "kPa \n")

## state 3
p3 = p2
t3 = tmax

## state 4

p4 = p1*r_turb
t4 = t3*(p4/p3)**((k-1)/k)

## state 5
t5 = tmax
p5 = p4

## state 6
p6 = p1
t6 = t5*(p6/p5)**((k-1)/k)

## energy analysis
wc_12 = cp*(t2-t1)
qin_23 = cp*(t3-t2)
wt_34 = cp*(t3-t4)
qin_45 = cp*(t5-t4)
wt_56 = cp*(t5-t6)
qout_61 = cp*(t6-t1)

wt = wt_34 + wt_56
wc = wc_12
qin = qin_23 + qin_45

wnet = wt-wc
print("The net work per unit mass is: ", wnet, "kJ/kg \n")

## thermal efficiancy
eta_th = wnet/qin
print("The thermal efficiency is ", (eta_th*100), "percent \n")
