import matplotlib.pyplot as plt
import numpy as np

# Properties of Saturated Water
T_w = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])  # °C
rho_w = np.array([
    999.9, 999.7, 999.1, 998, 997, 996, 994, 992.1, 990.1, 988.1, 985.2, 983.3, 980.4, 977.5
])  # Kg/m^3
Cp_w = np.array([
    4205, 4194, 4185, 4182, 4180, 4178, 4178, 4179, 4180, 4181, 4183, 4185, 4187, 4190
])  # J/KgK
K_w = np.array([
    0.571, 0.580, 0.589, 0.598, 0.607, 0.615, 0.623, 0.631, 0.637, 0.644, 0.649, 0.654, 0.659, 0.663
])  # W/mK
u_w = np.array([
    1.519, 1.307, 1.138, 1.002, 0.891, 0.798, 0.720, 0.653, 0.596, 0.547, 0.504, 0.467, 0.433, 0.404
]) * 1e-3  # Pas
Pr_w = np.array([
    11.2, 9.45, 8.09, 7.01, 6.14, 5.42, 4.83, 4.32, 3.91, 3.55, 3.25, 2.99, 2.75, 2.55
])

# Plotting the graphs
fig, ax1 = plt.subplots()

ax1.set_xlabel('Temperature (°C)')
ax1.set_ylabel('Density (Kg/m^3), Specific Heat (J/KgK)', color='tab:red')
ax1.plot(T_w, rho_w, color='tab:red', label='Density')
ax1.plot(T_w, Cp_w, color='tab:orange', label='Specific Heat')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Thermal Conductivity (W/mK), Dynamic Viscosity (Pas), Prandtl Number', color='tab:blue')
ax2.plot(T_w, K_w, color='tab:blue', label='Thermal Conductivity')
ax2.plot(T_w, u_w, color='tab:green', label='Dynamic Viscosity')
ax2.plot(T_w, Pr_w, color='tab:purple', label='Prandtl Number')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout()
plt.title('Properties of Saturated Water')
plt.show()
