from math import cos, sin, pi, sqrt, atan2

def sph2cart(azimuth, elevation, radius):
    """
    Convert spherical coordinates to cartesian 3D coordinates.

    Azimuth and elevation must be in radians.
    """
    x = radius * cos(elevation) * cos(azimuth)
    y = radius * cos(elevation) * sin(azimuth)
    z = radius * sin(elevation)

    return (x, y, z)

def cart2sph(x, y, z):
    """
    Convert cartesian 3D coordinates to spherical coordinates.

    When returned, azimuth and elevation are expressed in radians.
    """
    x2plusy2 = x ** 2 + y ** 2
    radius = sqrt(x2plusy2 + z ** 2)
    elevation = atan2(z, sqrt(x2plusy2)) # theta
    azimuth = atan2(y, x)                # phi
    return (azimuth, elevation, radius)

def deg2rad(degrees):
    return degrees / 180 * pi

def rad2deg(radians):
    return radians / pi * 180
