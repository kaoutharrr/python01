import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(original_array: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 2D array by swapping the row and column indices.
    No library function (like np.transpose or .T) is used.
    """
    rows, cols = original_array.shape
    transposed_array = np.zeros((cols, rows), dtype=original_array.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed_array[j, i] = original_array[i, j]
    return transposed_array


def main():
    try:
        # --- 1. Load and Slice (Reuse logic from Exercise 03) ---
        img_array = ft_load("animal.jpeg")
        if img_array is None:
            return

        # Slice/Zoom: Selects 400x400 area and the grayscale channel (0)
        original_slice = img_array[100:500, 350:750, 0]

        # --- 2. Print Original Slice Info ---
        print(f"The shape of image is: {original_slice.shape}")
        print(original_slice)  # Print truncated array

        # --- 3. Perform Manual Transpose ---
        rotated_array = ft_transpose(original_slice)

        # --- 4. Print Transposed Info ---
        print(f"New shape after Transpose: {rotated_array.shape}")
        print(rotated_array)

        # --- 5. Display the Rotated Image ---
        plt.imshow(rotated_array, cmap='gray')
        plt.title('Rotated Raccoon')
        plt.show()

    except Exception as e:
        print(f"Error during rotation processing: {e}")


if __name__ == "__main__":
    main()
