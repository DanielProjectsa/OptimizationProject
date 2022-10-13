
# Step 1 Optimization Energy Networks

import pandas as pd
import pandapower as pp
import pandapower.networks as nw
import pandapower.plotting as pplt
import matplotlib.pyplot as plt


net= nw.create_cigre_network_mv()

#print(net)
pp.runpp(net)

#print(net.res_trafo.loading_percent)
#print(net.res_line.loading_percent)
#print(net.res_bus)



print("-----------------------------    STEP 1.2    -----------------------")


net = nw.create_cigre_network_mv()

net
vmax = 1.1
vmin = 0.9
max_ll = 100

lines = net.line.index 
N = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N.append(l)
        print("critical line")
        print(l)
        net.res_bus.vm_pu
        net.res_bus.vm_pu
        net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
ax = pplt.simple_plot(net, show_plot = False)
clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
pplt.draw_collections([clc], ax=ax)
plt.show()
print(N)

print("-----------------------------    STEP 1.3    -----------------------")


net
vmax_3 = 1.05
vmin_3 = 0.95
max_ll_3 = 100

lines = net.line.index 
N_3 = list()
overvoltage_line= list()
overvoltage_value= list()

undervoltage_line= list()
undervoltage_value= list()

overloaded_line= list()
overloaded_value= list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    overvoltage_line= list()
    overvoltage_value= list()

    undervoltage_line= list()
    undervoltage_value= list()

    overloaded_line= list()
    overloaded_value= list()
    
    check= list()
    
   # for c in (1,9)
    
    if net.res_bus.vm_pu.max() > vmax_3 or net.res_bus.vm_pu.min() < vmin_3 or net.res_line.loading_percent.max() > max_ll_3:
        N_3.append(l) 
        print("Disconnected line")
        print(l)
        #print("Bus voltage")
        #print(net.res_bus.vm_pu)
        #print("Loading percent")
        #print(net.res_line.loading_percent)
        
        for i in lines:
            if net.res_bus.vm_pu[i] > vmax_3:
                overvoltage_line.append(i)
                overvoltage_value.append(net.res_bus.vm_pu[i])
                
        overvoltage = overvoltage_line, overvoltage_value
        
        print("overvoltage")
        print(overvoltage)
        
        for i in lines:
            if net.res_bus.vm_pu[i] < vmin_3:
                undervoltage_line.append(i)
                undervoltage_value.append(net.res_bus.vm_pu[i])
                
        undervoltage = undervoltage_line, undervoltage_value
        
        print("Undervoltage")
        print(undervoltage)
        
        for i in lines:
            if net.res_line.loading_percent[i] > max_ll_3:
                overloaded_line.append(i)
                overloaded_value.append(net.res_line.loading_percent[i])
                
        overloaded = (overloaded_line, overloaded_value)
        
        print("Overloaded")
        print(overloaded)
      
        
    net.line.loc[l,"in_service"] = True
    print()
    
print("      Critical lines:")
print(N_3) 
    
ax = pplt.simple_plot(net, show_plot = False)
clc = pplt.create_line_collection(net, N_3, color ="r", linewidth = 3.,use_bus_geodata=(True))
pplt.draw_collections([clc], ax=ax)
plt.show()


print("-----------------------------    STEP 1.3 Switches variations   -----------------------")

net = nw.create_cigre_network_mv()
net.switch.closed[1] = True
net.switch.closed[2] = True
net.switch.closed[4] = True
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_1 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_1.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
ax = pplt.simple_plot(net, show_plot = False)
clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
pplt.draw_collections([clc], ax=ax)
plt.show()
print(N_1)

#print(net.switch.closed[1] )
#print(net.switch.closed[2] )
#print(net.switch.closed[4] )
print(net.switch)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = False
net.switch.closed[2] = False
net.switch.closed[4] = False
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_2 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_2.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_2)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = False
net.switch.closed[2] = True
net.switch.closed[4] = True

net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_3 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_3.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_3)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = True
net.switch.closed[2] = False
net.switch.closed[4] = True
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_4 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_4.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_4)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = True
net.switch.closed[2] = True
net.switch.closed[4] = False
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_5 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_5.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_5)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = False
net.switch.closed[2] = False
net.switch.closed[4] = True
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_6 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_6.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_6)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = False
net.switch.closed[2] = True
net.switch.closed[4] = False
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_7 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_7.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_7)

net = nw.create_cigre_network_mv()
net.switch.closed[1] = True
net.switch.closed[2] = False
net.switch.closed[4] = False
net
vmax = 1.05
vmin = 0.95
max_ll = 100

lines = net.line.index 
N_8 = list()

for l in lines:
    net.line.loc[l,"in_service"] = False
    pp.runpp(net)
    
    
    if net.res_bus.vm_pu.max() > vmax or net.res_bus.vm_pu.min() < vmin or net.res_line.loading_percent.max() > max_ll:
        N_8.append(l)
        #print("critical line")
        #print(l)
        #net.res_bus.vm_pu
        #net.res_bus.vm_pu
        #net.res_line.loading_percent
        
    net.line.loc[l,"in_service"] = True
    
#ax = pplt.simple_plot(net, show_plot = False)
#clc = pplt.create_line_collection(net, N, color ="r", linewidth = 3.,use_bus_geodata=(True))
#pplt.draw_collections([clc], ax=ax)
#plt.show()
print(N_8)

print(N_1)
print(N_2)
print(N_3)
print(N_4)
print(N_5)
print(N_6)
print(N_7)
print(N_8)

crit= list()
for l in lines:       
        if l in N_1 and l in N_2  and l in N_3  and l in N_4  and l in N_5  and l in N_6  and l in N_7  and l in N_8 :
         crit.append(l)
print(crit)

ax = pplt.simple_plot(net, show_plot = False)
clc = pplt.create_line_collection(net, crit, color ="r", linewidth = 3.,use_bus_geodata=(True))
pplt.draw_collections([clc], ax=ax)
plt.show()
