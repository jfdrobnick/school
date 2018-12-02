## Consider an ideal gas turbine cycle with two stages of compression and
## two stages of expansion. The pressure ratio across each stage of the
## compressor and the turbine is 2. Air (use the IG model) enters each stage
## of the compressor at 310 K and each stage of the turbine at 1100 K
## (see (Figure 1)). Assume an efficiency of 85 % for each compressor
## stage and an efficiency of 90 % for each turbine stage, and a
## regenerator with 85 % effectiveness.

r_c = 2 #pressure ratio across compressor
r_t = 2 #pressure ratio across turbing
n_c = 0.85 #compressor efficiency
n_t = 0.9 #turbine efficiency
n_regen = 0.85 #regen effectiveness

## PG Model for Air


#state 1 - enter compressor stage 1
t1 = 310
h1 = 310.24
u1 = 217.67
pr1 = 1.5546

#state 2 - enter intercooler, ideal
pr2 = r_c*pr1
print("pr2 is", pr2, "\n")
t2 = 377 #from table after getting pr2
h2 = 378 #from table after getting pr2

#state 3 - enter intercooler, actual
#since p3 = p2 . . .
h3 = h1

#state 4 - enter compressor, stage 2
t4 = 310
h4 = 378.34
u4 = 217.67

#state 5 - enter regen, ideal
pr5 = 167.1
h5 = 1161.1

#state 6 - enter regen, actual
pr6 = (1/r_p)*pr5
t6 = 924.1
h6 = 960.05

#state 7 - enter turbine 1
t7 = 1100
h7 = 1161.07
u7 = 845.33

#state 8 - enter reheat, ideal

#state 9 - enter reheat, actual

#state 10 - enter turbine 2
t10 = 1100
h10 = 1161.07
u10 = 845.33

#state 11 - exit turbine 2, enter regen, ideal

#state 12 - exit turbing 2, enter regen, actual

#state 13 - enter combuster (after state 5,6?)

#state 14 - enter HX (const p heat addition)
