# imports
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Io
moonIo = {
    "period": 1.7691,
    "sma": 421700,
    "mass": 8931900
}
# Europa
moonEuropa = {
    "period": 3.5512,
    "sma": 671034,
    "mass": 4800000
}
# Ganymede
moonGanymede = {
    "period": 7.1546,
    "sma": 1070412,
    "mass": 14819000
}
# Callisto
moonCallisto = {
    "period": 16.689,
    "sma": 1882709,
    "mass": 10759000
}

# arrays
period = np.array([moonIo["period"], moonEuropa["period"], moonGanymede["period"], moonCallisto["period"]])
sma = np.array([moonIo["sma"], moonEuropa["sma"], moonGanymede["sma"], moonCallisto["sma"]])
mass = np.array([moonIo["mass"], moonEuropa["mass"], moonGanymede["mass"], moonCallisto["mass"]])

# part a
fig_a, ax_a = plt.subplots()
ax_a.scatter(period, sma, color="black")
ax_a.plot(period, sma, color="black", alpha=0.5)
ax_a.set_xlabel("Period (days)")
ax_a.set_ylabel("Semi-Major Axis (km)")
ax_a.set_title("Period vs. SMA of Jupiters Moons")
ax_a.grid()
fig_a.tight_layout()
plt.savefig("part_a")

# part b
log10_period = np.log10(period)
log10_sma = np.log10(sma)
fig_b, ax_b = plt.subplots()
ax_b.scatter(log10_period, log10_sma, color="black")
ax_b.plot(log10_period, log10_sma, color="black", alpha=0.5)
# linear regression
def linear(x, m, b):
    return (m*x)+b
coefficients, pcov = sp.optimize.curve_fit(linear, log10_period, log10_sma)
print(coefficients) # ~= [0.66666156 5.45983372]
residuals = log10_sma - linear(log10_period, *coefficients)
res_sum = np.sum(residuals**2)
tot_sum = np.sum((log10_sma - np.mean(log10_sma))**2)
r_squared = 1 - (res_sum / tot_sum)
print("R**2:", r_squared) # ~= R**2: 0.9999999998845956
fit_x = [min(log10_period), max(log10_period)]
fit_y = [linear(min(log10_period), *coefficients), linear(max(log10_period), *coefficients)]
ax_b.plot(fit_x, fit_y, "--",color="tab:red", alpha=0.8)
# graph
ax_b.set_xlabel("Log10 Period (days)")
ax_b.set_ylabel("Log10 Semi-Major Axis (km)")
ax_b.set_title("Log10 of Period vs. Log10 of SMA of Jupiters Moons")
text1 = "y = "+str(round(coefficients[0],5))+"x + "+str(round(coefficients[1],5))
text2 = r"$R^2$ = "+str(round(r_squared,5))
plt.text(0.625, 5.84, text1, color="tab:red")
plt.text(0.625, 5.805, text2, color="tab:red")
ax_b.grid()
fig_b.tight_layout()
plt.savefig("part_b")