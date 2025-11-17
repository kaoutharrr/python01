import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate and return a list of BMI values"""
    if len(height) != len(weight):
        print("error : lists must have the same size")
        return []
    try:
        height_arr = np.array(height)
        weight_arr = np.array(weight)
        result_np = weight_arr / (height_arr ** 2)
        res = result_np.tolist()
        return res

    except Exception as e:
        print(f"Error  during calculation : {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """checks if each BMI value in the list is above a specified limit"""
    try:
        bmi_arr = np.array(bmi)
        res_np = bmi_arr > limit
        res = res_np.tolist()
        return res
    except Exception as e:
        print(f"Error during BMI comparison or type conversion: {e}")
        return []


def main():
    # Example test cases (like the provided tester.py)
    height = [2.71, 1.15]
    weight = [166.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    # Example error case
    height_err = [2.71]
    weight_err = [166.3, 38.4]
    print(give_bmi(height_err, weight_err))


if __name__ == "__main__":
    main()
