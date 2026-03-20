from PIL import Image
import os

while True:
    folder_path = input("Copy and paste the full path to the folder containing your images: ").strip().strip("\"").strip('\'')

    if not os.path.isdir(folder_path):
        print("Folder not found. Please check the path and try again.")
        continue
    break

while True:
    try:
        width, height = map(int, input("Enter new dimensions (width height): ").strip().split())
        break
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")


resized_folder = os.path.join(folder_path, "resized")
os.makedirs(resized_folder, exist_ok=True)

for file in os.listdir(folder_path):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(folder_path, file)
        name, ext = os.path.splitext(file)
        output_path = os.path.join(resized_folder, f"{name}_resized{ext}")

        try:
            img = Image.open(input_path)
            img = img.thumbnail((width, height), Image.Resampling.LANCZOS)  
            img.save(output_path)
            print(f"Resized {file} -> {output_path}")
        except Exception as e:
            print(f"Failed to process {file}: {e}")

print(f"\nAll images resized! Check the folder: {resized_folder}")
