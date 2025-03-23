#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Telomere Shortening Simulation with Oxidative Stress & Visualization
import streamlit as st

import matplotlib.pyplot as plt
import random


# In[15]:


# User Inputs
# import ipywidgets as widgets
# from IPython.display import display

# def get_stress_level(default=1.0):
#     try:
#       stress_slider = widgets.FloatSlider(
#           value=default,
#           min=0.5,
#           max=5.0,
#           step=0.1,
#           description='Oxidative Stress:',
#           continuous_update=False
#       )
#       display(stress_slider)
#       return stress_slider
#     except:
#        st.write(f"Slider available. Using default stress level: {default}")
#        return default

# slider = get_stress_level()


stress_level = st.sidebar.slider(
    'Oxidative Stress Level:',
    min_value=0.5,
    max_value=5.0,
    value=1.0,
    step=0.1
)


# In[22]:


# Obtain the stress value from the slider
# stress_level = slider.value
# st.write(stress_level)

# Initialize variables 
initial_telomere = 10000
critical_length = 4000
shortening_rate = 100 # base shortening per division
telomere_length = initial_telomere
divisions = 0
telomere_over_time = []


# In[ ]:


# Simulation
while telomere_length > critical_length:
  telomere_over_time.append(telomere_length)
  telomere_length -= shortening_rate*stress_level
  divisions+=1



telomere_over_time.append(telomere_length)



# Results of Simulation
st.write(f"\nWith a stress level of {stress_level}, the cell can divide {divisions} times before senescence")
# Note that human somatic cells divide approximately 40 to 60 times before they stop dividing and enter a senescent state



# In[27]:


# Plotting the graph of Telomere Length against Cell Divisions
plt.plot(telomere_over_time)
plt.title(f"Telomere Shortening Over Time With a Stress Level of {stress_level}")
plt.xlabel("Cell Division")
plt.ylabel("Telomere Length")
plt.grid(True)
st.pyplot(plt.gcf())


# In[69]:


# from mpl_toolkits import mplot3d

# get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for 3D plot
zline = np.linspace(critical_length, initial_telomere, divisions)
xline = np.linspace(0, divisions, divisions)
yline = np.linspace(0, stress_level, divisions)

ax.scatter3D(xline, yline, zline, color='red', marker='o')
ax.plot3D(xline, yline, zline, color='gray')

# Labels
ax.set_xlabel('Cell Divisions')
ax.set_ylabel('Oxidative Stress Level')
ax.set_zlabel('Telomere Length')
ax.set_title('Telomere Shortening as 3D Scatter Plot')

st.pyplot(fig)


# In[68]:


# Multi-Cell Aging Simulation
import random 
class Cell:
  def __init__(self):
    self.telomere = 10000
    self.dna_damage = 0.0 # expressed in percentage
    self.ros_level = 1.0 # Reactive Oxygen Species (ROS) in cells
    self.state = "Healthy"

    # '''
    # Reactive Oxygen Species (ROS) are chemically reactive molecules that: 
    # - are produced as byproducts of normal metabolism (e.g., in mitochondria)
    # - increase with oxidative stress, such as UV light, toxins, radiation
    # - can damage DNA, proteins and cell membranes
    # '''

  def step(self):
    if self.state != "Healthy":
      return

    damage_chance = random.uniform(0, 1)* self.ros_level
    if damage_chance > 0.9:
      self.dna_damage += 10 # accumlate damage if damage chance is greater than 90%

    # Telomere shortening
    self.telomere -= 100* self.ros_level

    # State transitions
    if self.dna_damage >= 50 or self.telomere <= 4000:
      self.state = 'Senescent'
    elif self.dna_damage > 90:
      self.state = 'Apoptotic'

# Simulation Parameters
num_cells = 100
cycles = 50
cells = [Cell() for _ in range(num_cells)] # Creating 100 instances of Cell class

health_stats = {"Healthy": [], "Senescent": [], "Apoptotic": []}

# Simulation Loop
for _ in range(cycles):
  counts = {"Healthy" : 0, 'Senescent' : 0, "Apoptotic" : 0}

  for cell in cells: 
    cell.step()
    counts[cell.state] += 1

  for state in counts: 
    health_stats[state].append(counts[state])



# Plot Time Evolution
plt.figure()
for state in health_stats:
  plt.plot(health_stats[state], label=state) # plot health stats value against number of cycles which is fixed at 50
plt.title("Cell State Over 50 Cycles")
plt.xlabel("Cycles")
plt.ylabel("Number of Cells")
plt.legend()
plt.grid(True)
st.pyplot(plt.gcf())

