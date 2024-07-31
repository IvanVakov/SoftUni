text = input().split("\\")

path_file_name_with_ext = text[-1]
path_file_parts = path_file_name_with_ext.split(".")
file_name = path_file_parts[-2]
extension = path_file_parts[-1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")