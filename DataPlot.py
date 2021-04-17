from RunReader import sum, roof_co2, seat_co2, motor_co2

import matplotlib.pyplot as plt
import pandas as pd

# Initial Variable assignment
phase = ('Production', 'Betrieb', 'Recycle')

roof_co2_btb = 4  # my dummies in Betrieb
roof_co2_rcy = 9  # my dummies in Recycle
roof = [roof_co2, roof_co2_btb, roof_co2_rcy]

seat_co2_btb = 4
seat_co2_rcy = 9
seat = [seat_co2, seat_co2_btb, seat_co2_rcy]

motor_co2_btb = 4
motor_co2_rcy = 9
motor = [motor_co2, motor_co2_btb, motor_co2_rcy]

# Plotting in Diagram

df = pd.DataFrame({'Roof': roof, 'Seat': seat, 'Motor': motor})
ax = df.plot.barh(stacked=True)
ax.figure.set_size_inches(10, 6)
ax.set_yticklabels(phase)

ax.legend(loc='upper right')

# Saving plot into png
plt.savefig('my_emission.png')
# plt.show()
