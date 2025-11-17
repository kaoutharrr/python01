import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        img_array = ft_load("animal.jpeg")
        if img_array is None:
            return
        zoomed_gray = img_array[100:500, 350:750, 0]
        print(f"New shape after slicing: {zoomed_gray.shape}")
        print(zoomed_gray)
        plt.imshow(zoomed_gray, cmap='gray')
        plt.title('Zoomed Raccoon Face')
        plt.xlabel('X-axis scale')
        plt.ylabel('Y-axis scale')
        plt.show()
    except Exception as e:
        print(f"Error during zoom processing: {e}")


if __name__ == "__main__":
    main()
