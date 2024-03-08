import os

def find_missing_files(folder_path, start=0, end=8436):
    expected_files = set(f"{str(i).zfill(4)}.pdf" for i in range(start, end + 1))
    actual_files = set(file for file in os.listdir(folder_path) if file.endswith('.pdf'))
    missing_files = expected_files - actual_files
    return missing_files

folder_path = 'dataset'  # Change this to the path of your folder
missing_files = find_missing_files(folder_path)

if missing_files:
    print("Missing files:")
    for file in sorted(missing_files):
        print(file)
else:
    print("All files are present.")