import os

def rename_images(root_folder):
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)
        if os.path.isdir(subfolder_path):  # Check if it's a directory
            for filename in os.listdir(subfolder_path):
                if filename.startswith("upper_") and filename.endswith(".png"):  # Adjust file extension if needed (e.g., .jpg)
                    letter = filename.split("_")[1]  # Extract the middle letter
                    new_filename = f"{letter}.png"  # Create the new filename
                    old_path = os.path.join(subfolder_path, filename)
                    new_path = os.path.join(subfolder_path, new_filename)
                    os.rename(old_path, new_path)
                else :
                    print(f"Skipping {filename}")

# Example Usage:
root_folder = "../content/content" # Replace with actual path
rename_images(root_folder)
