import math

def find_period(L0, L1):
    """
    This function calculates and displays the pendulum period (T)
    for all lengths between L0 and L1 (inclusive).
    It also returns the period values T0 and T1 for L0 and L1, respectively.
    """

    g = 9.81  # gravitational acceleration (m/s^2)

    # Loop through each length from L0 to L1
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"When L = {L:4.1f} m, T = {T:3.1f} s")

    # Calculate T0 and T1
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)

    # Return both period values
    return T0, T1
