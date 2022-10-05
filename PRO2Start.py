# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:40:02 2022

@author: drj
"""
# Step 2

import pandapower as pp
import pandapower.networks as nw
import pandapower.plotting as pplt
import matplotlib.pyplot as plt
from pandapower.plotting.plotly import pf_res_plotly


net = nw.create_cigre_network_mv()
pp.create_bus(net, name='Bus CS 14', vn_kv=0.4, type='b', geodata=((9,4)))
pp.create_bus(net, name='Bus CS 11', vn_kv=0.4, type='b', geodata=((3,6)))
pp.create_bus(net, name='Bus CS 5', vn_kv=0.4, type='b', geodata=((0,6)))
pp.create_bus(net, name='Bus CS 4', vn_kv=0.4, type='b', geodata=((1.5,8)))
pp.create_bus(net, name='Bus CS 9', vn_kv=0.4, type='b', geodata=((5,4)))


pp.create_transformer(net, hv_bus=14, lv_bus= pp.get_element_index(net,'bus', 'Bus CS 14'), name='CS 14', std_type=0.64 MVA 20/0.4 kV')
pp.create_transformer(net, hv_bus=11, lv_bus=pp.get_element_index(net, 'bus', 'Bus CS 11'),  name='CS 11',std_type=0.4 MVA 20/0.4 kV')
pp.create_transformer(net, hv_bus=5, lv_bus=pp.get_element_index (net, 'bus', 'Bus CS 5'),   name='CS 5', std_type=0.4 MVA 20/0.4 kV')
pp.create_transformer(net, hv_bus=4, lv_bus=pp.get_element_index (net, 'bus', 'Bus CS 4'),   name='CS 4', std_type=0.25 MVA 20/0.4 kV')
pp.create_transformer(net, hv_bus=9, lv_bus=pp.get_element_index (net, 'bus', 'Bus CS 9'),   name='CS 9', std_type=0.25 MVA 20/0.4 kV')

print(net)

ax = pplt.simple_plot(net, show_plot = False)
clc = pplt.create_line_collection(net, color ="g", linewidth = 3.,use_bus_geodata=(True))
pplt.draw_collections([clc], ax=ax)
plt.show()
