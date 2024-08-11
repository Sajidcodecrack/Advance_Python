import rasterio
import matplotlib.pyplot as plt

def load_satellite_data(file_path):
    try:
        with rasterio.open(file_path) as src:
            # Access metadata
            print("Metadata:")
            print(src.meta)

            # Access data as a NumPy array
            data = src.read(1)  # Assuming a single-band image, adjust as needed
            return data
    except Exception as e:
        print(f"Error loading satellite data: {e}")
        return None

def display_satellite_image(data):
    plt.imshow(data, cmap='viridis')  # You can choose a different colormap
    plt.colorbar(label='Pixel Value')
    plt.title('Satellite Image')
    plt.show()

def main():
    # Provide the path to your satellite data file (GeoTIFF in this case)
    file_path = "C:\\Users\\Sajid\\Downloads\\MOD12Q1_UMD.tif"

    # Load satellite data
    satellite_data = load_satellite_data(file_path)

    if satellite_data is not None:
        # Perform further processing or analysis as needed
        print("Successfully loaded satellite data.")
        # Example: print the shape of the data
        print("Data shape:", satellite_data.shape)

        # Display satellite image
        display_satellite_image(satellite_data)

if __name__ == "__main__":
    main()
