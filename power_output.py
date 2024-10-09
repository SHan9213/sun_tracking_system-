
import numpy as np

def calculate_power_output(sun_elevation, sun_azimuth, panel_elevation, panel_azimuth, max_power=1000):
    """
    Calculates the solar panel power output based on the angle of incidence between the sun and panel.
    :param sun_elevation: Sun's elevation angle
    :param sun_azimuth: Sun's azimuth angle
    :param panel_elevation: Panel's elevation angle
    :param panel_azimuth: Panel's azimuth angle
    :param max_power: Maximum possible power output (W/m^2)
    :return: Power output (W/m^2)
    """
    angle_of_incidence = np.sqrt((sun_elevation - panel_elevation)**2 + (sun_azimuth - panel_azimuth)**2)
    power_output = max_power * np.cos(np.radians(angle_of_incidence))
    return max(0, power_output)  # No negative power output
