import sys
from typing import Tuple


def compute_ever(length: float, net_ele: float) -> Tuple[float, float]:
    """
    Computes the amount of laps and the total length required to achieve an everesting.
    :param length: Length of one uphill in km.
    :type length: float
    :param net_ele: Netto elevation gain of one uphill.
    :type net_ele: float
    :return: First is the amount of laps. Second is total length of the all laps.
    :rtype: tuple[float, float]
    """
    laps: float = 8848 / net_ele
    total_length: float = 2 * length * laps
    return laps, total_length


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise IOError(f'Two arguments are required. Lap length and net elevation gain.')
    lap_length = float(sys.argv[1])
    net_ele_gain = float(sys.argv[2])
    laps, total_length = compute_ever(lap_length, net_ele_gain)
    print(f'Laps: {laps:.2f}\n'
          f'Total length: {total_length:.1f}km')
    exit(0)
