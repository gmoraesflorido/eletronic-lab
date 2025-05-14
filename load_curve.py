from argparse import ArgumentParser

def load_curve (source, diode_voltage, resistance):
    """
    Calculate the load curve for a diode circuit.

    Parameters:
    source (float): The voltage of the source.
    diode_voltage (float): The voltage across the diode.
    resistance (float): The resistance in the circuit.

    Returns:
    float: The current through the circuit.
    """
    # Calculate the current through the circuit
    current = (source - diode_voltage) / resistance
    return current

if __name__ == "__main__":
    # Create the argument parser
    parser = ArgumentParser(description="Calculate the load curve for a diode circuit.")
    
    # Add arguments
    parser.add_argument("-s","--source", type=float, help="The voltage of the source.")
    parser.add_argument("-v","--diode_voltage", type=float, help="The voltage across the diode.")
    parser.add_argument("-r","--resistance", type=float, help="The resistance in the circuit.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Calculate the load curve
    current = load_curve(args.source, args.diode_voltage, args.resistance)
    
    # Print the result
    print(f"Current through the circuit: {current:.9f} A")