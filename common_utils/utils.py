from math import exp
from math import log


def exp_current_diode(diode_voltage, thermal_voltage, reverse_current):
    """Calculate the current through a diode using the exponential model.
    Parameters:
    diode_voltage (float): The voltage across the diode.
    thermal_voltage (float): The thermal voltage of the diode.
    reverse_current (float): The reverse current of the diode.
    Returns:
    float: The current through the diode.
    """
    I_S = reverse_current
    V_T = thermal_voltage
    V_D = diode_voltage
    I_D = I_S * (exp((V_D/V_T)) - 1)
    return I_D


def exp_voltage_diode(diode_current, thermal_voltage, reverse_current):
    """Calculate the voltage across a diode using the exponential model.
    Parameters:
    diode_current (float): The current through the diode.
    thermal_voltage (float): The thermal voltage of the diode.
    reverse_current (float): The reverse current of the diode.
    Returns:
    float: The voltage across the diode.
    """
    I_S = reverse_current
    V_T = thermal_voltage
    I_D = diode_current
    V_D = V_T * log((I_D / I_S) + 1)
    return V_D