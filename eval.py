import os
import subprocess

def run_inference_for_all_subfolders(img_root, config_path, weight_path, content_font, saving_root):
    # Get list of all subdirectories in img_root
    subfolders = [f.path for f in os.scandir(img_root) if f.is_dir()]

    for subfolder in subfolders:
        subfolder_name = os.path.basename(subfolder)
        saving_subfolder = os.path.join(saving_root, subfolder_name)

        # Create the command to run inference.py
        command = [
            "python", "inference.py",
            config_path,
            "--weight", weight_path,
            "--content_font", content_font,
            "--img_path", subfolder,
            "--saving_root", saving_subfolder
        ]

        # Run the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Print the output and error (if any)
        print("Running inference for:", subfolder)
        print("Output:", result.stdout.decode())
        print("Error:", result.stderr.decode())

if __name__ == "__main__":
    # Define paths
    img_root = "data/test"
    config_path = "cfgs/custom.yaml"
    weight_path = "last.pth"
    content_font = "data/content/arial"
    saving_root = "./infer_res"

    run_inference_for_all_subfolders(img_root, config_path, weight_path, content_font, saving_root)
