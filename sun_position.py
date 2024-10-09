
import numpy as np

def simulate_sun_position(day_of_year, hour, latitude=0):
    """
    Simulates the sun's elevation and azimuth angles based on the time of day and latitude.
    :param day_of_year: Day of the year (1-365)
    :param hour: Hour of the day (0-23)
    :param latitude: Latitude of the location
    :return: (elevation, azimuth) angles in degrees
    """
    declination = 23.45 * np.sin(np.radians(360/365 * (day_of_year - 81)))
    time_offset = (hour - 12) * 15
    elevation = np.degrees(np.arcsin(np.sin(np.radians(latitude)) * np.sin(np.radians(declination)) +
                                     np.cos(np.radians(latitude)) * np.cos(np.radians(declination)) * np.cos(np.radians(time_offset))))
    azimuth = (hour - 12) * 15  # Simplified azimuth angle (degrees)
    
    return elevation, azimuth
