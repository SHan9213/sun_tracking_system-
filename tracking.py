
def single_axis_tracker(sun_azimuth):
    """
    Adjusts the panel angle to match the sun's azimuth angle for single-axis tracking.
    :param sun_azimuth: Azimuth angle of the sun in degrees
    :return: Panel orientation angle (degrees)
    """
    return sun_azimuth

def dual_axis_tracker(sun_elevation, sun_azimuth):
    """
    Adjusts both elevation and azimuth angles for dual-axis tracking.
    :param sun_elevation: Sun's elevation angle
    :param sun_azimuth: Sun's azimuth angle
    :return: (panel_elevation, panel_azimuth) angles in degrees
    """
    return sun_elevation, sun_azimuth
