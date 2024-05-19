import os

def delete_kazakh_letter_images(root_folder):
    """Deletes images containing Kazakh Cyrillic letters from all subfolders."""

    kazakh_letters = ['а', 'ә', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'қ', 'л', 'м', 'н', 'ң', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ұ', 'ү', 'ф', 'х', 'һ', 'ц', 'і', 'А', 'Ә', 'Б', 'В', 'Г', 'Ғ', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң', 'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ұ', 'Ү', 'Ф', 'Х', 'Һ', 'Ц', 'І']

    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file.startswith("lower_") and file.endswith(".png"):
                file_path = os.path.join(subdir, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Usage
root_folder = "../content/content"  # Replace with your path
delete_kazakh_letter_images(root_folder)
