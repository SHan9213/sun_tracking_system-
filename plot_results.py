
import matplotlib.pyplot as plt

def plot_results(hours, power_outputs, title):
    plt.plot(hours, power_outputs)
    plt.title(title)
    plt.xlabel('Time of Day (hours)')
    plt.ylabel('Power Output (W/m^2)')
    plt.grid(True)
    plt.show()
