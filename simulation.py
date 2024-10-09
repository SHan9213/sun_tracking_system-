
import numpy as np
from sun_position import simulate_sun_position
from tracking import single_axis_tracker, dual_axis_tracker
from power_output import calculate_power_output

def simulate_day(single_axis=True, latitude=0):
    day_of_year = 200  # Arbitrary day in summer
    hours = np.arange(0, 24, 0.5)  # Simulate every half hour
    power_outputs = []
    panel_angles = []

    for hour in hours:
        sun_elevation, sun_azimuth = simulate_sun_position(day_of_year, hour, latitude)
        
        if single_axis:
            panel_azimuth = single_axis_tracker(sun_azimuth)
            panel_elevation = 0  # Fixed elevation in single-axis tracking
        else:
            panel_elevation, panel_azimuth = dual_axis_tracker(sun_elevation, sun_azimuth)
        
        power_output = calculate_power_output(sun_elevation, sun_azimuth, panel_elevation, panel_azimuth)
        power_outputs.append(power_output)
        panel_angles.append((panel_elevation, panel_azimuth))
    
    return hours, power_outputs, panel_angles
