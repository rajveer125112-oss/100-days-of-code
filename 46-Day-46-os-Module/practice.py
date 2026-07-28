import os
# if (not os.path.exists("Test"))
# os.mkdir("46-Day-46-os-Module/Test")

# for i in range(1,101):
#     os.mkdir(f"46-Day-46-os-Module/Test/Day {i}")
# for i in range(1,101):
#     os.rename(f"46-Day-46-os-Module/Test/Day {i}",f"46-Day-46-os-Module/Test/Tut {i}")

folders=os.listdir("46-Day-46-os-Module/Test")

for folder in folders:
    print(folder)
    print(os.listdir(f"46-Day-46-os-Module/Test/{folder}"))