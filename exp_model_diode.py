"""
This script calculates whether the diode current or voltage using the
exponential model of a diode. The script takes the following arguments:
    -t, --thermal_voltage: The thermal voltage of the diode.
    -r, --reverse_current: The reverse current of the diode.
    -v, --diode_voltage: The voltage across the diode.
    -c, --diode_current: The current through the diode.
    -o, --options: The function to use for the calculation.
The options are:
    - current: Calculate the diode current.
    - voltage: Calculate the diode voltage. 
"""

from argparse import ArgumentParser
from common_utils.utils import exp_current_diode, exp_voltage_diode


def main(args):
    #VD_POINTS = [0.5, 0.6, 0.65, 0.68, 0.7, 0.72, 0.75]
    VD_POINTS = [0.6]

    if all(arg is not None for arg in [args.thermal_voltage, args.reverse_current,
                                       args.options]):

        if args.options == "current":
            for voltage in VD_POINTS:
                print(f"{exp_current_diode(voltage, args.thermal_voltage,
                                           args.reverse_current):.9f} A")
        elif args.options == "voltage":
            for voltage in VD_POINTS:
                print(f"{exp_voltage_diode(args.diode_current, args.thermal_voltage,
                                           args.reverse_current):.9f}")

    else:
        print("Please provide the required arguments: -t, -r, -d, -o")
        print("Example: python exp_model_diode.py -t 0.025 -r 1e-15 -d 0.7 -o current")

if __name__ == "__main__":
    parser = ArgumentParser(description="Calculate the load curve for a diode circuit.")
    
    parser.add_argument("-t","--thermal_voltage", type=float,
                        help="The thermal voltage of the diode.")
    parser.add_argument("-r","--reverse_current", type=float,
                        help="The reverse current of the diode.")
    parser.add_argument("-c", "--diode_current", type=float,
                        help="The current through the diode.")
    parser.add_argument("-v", "--diode_voltage", type=float,
                        help="The voltage across the diode.")
    parser.add_argument("-o", "--options", type=str, choices=["current", "voltage"], 
                        help="The function to use for the calculation.")
    
    args = parser.parse_args()

    main(args)
