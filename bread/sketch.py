#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:53:56 2023

@author: Calum
"""
# =============================================================================
# imports
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# data
# =============================================================================

x = np.linspace(0,15,1000)
y = np.zeros(1000)
a = 5 / np.log(100)
b = 100 / 7

# =============================================================================
# main
# =============================================================================

for i in range(len(x)):
    
    y[i] = np.exp(x[i]/a)
    
    if y[i] > 100:
        y[i] = 100
    
    if x[i] > 8:
        y[i] = 100 - b*(x[i]-8)
        
# =============================================================================
# plotting
# =============================================================================

plt.rc('font', family='Helvetica')

fig = plt.figure(1, figsize=(7,3))
ax = fig.add_subplot(111)

ax.plot(x, y, c='r')

ax.vlines(5, 0, 100, color='k', linestyle='--',alpha=0.5)
ax.vlines(8, 0, 100, color='k', linestyle='--',alpha=0.5)

ax.set_xlim(0, 15)
ax.set_ylim(0, 150)

ax.set_xticks([0,5,8,15])
ax.set_yticks([0,20,40,60,80,100])

ax.set_xlabel('Time, $t$ [hrs]', fontsize=10)
ax.set_ylabel('Activity, $A$ [%]')

plt.savefig('fig.png', dpi=400, bbox_inches='tight')


