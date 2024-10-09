
from simulation import simulate_day
from plot_results import plot_results

if __name__ == "__main__":
    # Single-axis tracking
    hours, power_outputs, _ = simulate_day(single_axis=True, latitude=30)
    plot_results(hours, power_outputs, 'Single-Axis Tracking Power Output')

    # Dual-axis tracking
    hours, power_outputs, _ = simulate_day(single_axis=False, latitude=30)
    plot_results(hours, power_outputs, 'Dual-Axis Tracking Power Output')
