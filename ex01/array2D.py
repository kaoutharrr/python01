import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ takes as parameters a 2D array, prints its shape, and returns a
        truncated version of the array based on
        the provided start and end arguments."""

    try:
        family_np = np.array(family)
        if family_np.ndim != 2:
            print("Error: Input list must represent a uniform 2D array.")
            return []
        print(f"My shape is: {family_np.shape}")
        sliced_array_np = family_np[start:end]
        if sliced_array_np.size == 0 and start != end:
            print("Error:  Check start and end indices.")
            return []
        print(f"My new shape is: {sliced_array_np.shape}")
        return sliced_array_np.tolist()
    except Exception as e:
        print(f"error: {e}")
        return []


def main():
    # Tester.py equivalent
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, 2))


if __name__ == "__main__":
    main()
