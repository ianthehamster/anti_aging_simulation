import streamlit as st
import matplotlib.pyplot as plt

# Title for the web app
st.title("Telomere Shortening Simulation with Oxidative Stress")

# Sidebar slider to get user input interactively
stress_level = st.sidebar.slider(
    'Oxidative Stress Level',
    min_value=0.5,
    max_value=5.0,
    value=1.0,
    step=0.1
)

# Initialize variables
initial_telomere = 10000
critical_length = 4000
shortening_rate = 100  # base shortening per division
telomere_length = initial_telomere
divisions = 0
telomere_over_time = []

# Simulation logic
while telomere_length > critical_length:
    telomere_over_time.append(telomere_length)
    telomere_length -= shortening_rate * stress_level
    divisions += 1

telomere_over_time.append(telomere_length)

# Display results on the Streamlit app (not the console!)
st.subheader("Simulation Result")
st.write(f"With a stress level of **{stress_level}**, the cell can divide **{divisions}** times before senescence.")

# Plotting results
fig, ax = plt.subplots()
ax.plot(telomere_over_time, marker='o')
ax.set_title(f"Telomere Shortening Over Time\n(Stress Level: {stress_level})")
ax.set_xlabel("Cell Division")
ax.set_ylabel("Telomere Length")
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
