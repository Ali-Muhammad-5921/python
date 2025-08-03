import os

def clear_clutter(folder_path):
    # Dictionary to store files by extension
    files_by_ext = {}

    # List all files in the folder
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(full_path):
            continue

        # Get extension (e.g., '.png') and remove the dot
        ext = os.path.splitext(filename)[1].lower()
        if ext:
            files_by_ext.setdefault(ext, []).append(filename)

    # Rename files by extension
    for ext, files in files_by_ext.items():
        files.sort()  # Optional: sort alphabetically before renaming
        for i, old_name in enumerate(files, start=1):
            new_name = f"{i}{ext}"
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)

            # If the new file name already exists and isn't the same file, skip it
            if old_name == new_name:
                continue

            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name} -> {new_name}: {e}")

# 🧪 Example usage (replace with your actual folder path)
folder_path = r"C:\Users\YourUsername\Desktop\clutter"  # <-- change this path
clear_clutter(folder_path)
