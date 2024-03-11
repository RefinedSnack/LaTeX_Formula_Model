import os

def find_missing_files(folder_path, extension: str, start=0, end=1217):
    expected_files = set(f"{str(i).zfill(4)}.{extension}" for i in range(start, end + 1))
    actual_files = set(file for file in os.listdir(folder_path) if file.endswith(f'.{extension}'))
    missing_files = expected_files - actual_files
    return missing_files

folder_path_1 = 'dataset'  # Change this to the path of your folder
folder_path_2 = 'png_dataset'  # Change this to the path of your folder
missing_files_1 = find_missing_files(folder_path_1, "pdf")

if missing_files_1:
    print("Missing files:")
    for file in sorted(missing_files_1):
        print(file)
else:
    print("All files are present.")
# missing_files_2 = find_missing_files(folder_path_2, "png")
# if missing_files_2:
#     print("Missing files:")
#     for file in sorted(missing_files_2):
#         print(file)
# else:
#     print("All files are present.")
