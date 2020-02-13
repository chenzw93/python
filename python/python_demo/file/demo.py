import os

current_local = os.getcwd()
print(current_local)
print(os.listdir(current_local))
print([file for file in os.listdir(current_local) if os.path.splitext(file)[1] == ".py"])
print([os.path.splitext(file)[1] for file in os.listdir(current_local)])


def list_files(file_path):
    for file in os.listdir(file_path):
        file_absolute = os.path.join(file_path, file)
        if os.path.isfile(file_absolute):
            print(file_absolute)
        else:
            list_files(file_absolute)


print("-" * 10)
list_files(current_local)
print("-" * 10)
for dirs in os.walk(current_local):
    print(dirs)
# for root, dirs, files in os.walk(current_local):
#     print(root)
#     print(dirs)
#     print(files)
