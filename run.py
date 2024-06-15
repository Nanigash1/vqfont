import subprocess
import gdown
import zipfile
import os

def download_zip():
    def convert_drive_url(original_url):
        if 'drive.google.com/file/d/' in original_url:
            file_id = original_url.split('/d/')[1].split('/')[0]
            return f'https://drive.google.com/uc?id={file_id}'
        else:
            raise ValueError('Invalid Google Drive URL format')

    original_url = 'https://drive.google.com/file/d/1VWmIHfX7RK6LaejzxiRVsRV7LAwY05WG/view?usp=sharing'
    converted_url = convert_drive_url(original_url)
    print(converted_url)

    # Путь для сохранения файла в Colab
    output = '/results16500_b32.zip'
    # Загрузка файла
    gdown.download(converted_url, output, quiet=False)

def extract_zip():
    # Path to the downloaded archive
    zip_path = '/results16500_b32.zip'

    # Path to save the extracted folder
    extract_path = 'results'

    # Function to extract only the required folder
    def extract_specific_folder(zip_path, extract_path, folder_name):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                print(f'Found member: {member}')  # Debugging line
                if member.startswith(folder_name):
                    # Compute the target path
                    target_path = os.path.join(extract_path, os.path.relpath(member, folder_name))
                    # Create directories if they don't exist
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    # Skip directories
                    if not member.endswith('/'):
                        # Extract the file
                        with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                            target.write(source.read())

    # Extract only the folder 'vqfont/'
    extract_specific_folder(zip_path, extract_path, 'content/vqfont/results')

def install_dependencies():
    """Installs the required Python packages using pip."""
    packages = ['numpy', 'opencv-python', 'lmdb', 'Pillow', 'tqdm', 'PyYAML', 'pygame', 'scipy', 'scikit-image', 'einops', 'seaborn', 'matplotlib', 'apex', 
'tensorboard', 'sconf']
    subprocess.run(["pip", "install"] + packages)


def install_dependencies2():
    """Installs the required Python packages using pip."""
    packages = ['gdown']
    subprocess.run(["pip", "install"] + packages)

def install_dependencies3():
    """Installs the required Python packages using pip."""
    packages = ['zipfile', 'subprocess']
    subprocess.run(["pip", "install"] + packages)

def run_training():
    """Executes the vqfont training script."""
    subprocess.run(["python", "train.py", "test", "cfgs/custom.yaml", "--resume", "./results/your_task_name/checkpoints/test/last.pth"])

if __name__ == "__main__":
    install_dependencies()
    install_dependencies2()
    install_dependencies3()
    download_zip()
    extract_zip()
    run_training()
