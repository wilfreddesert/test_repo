import os
curr_dir = os.listdir(os.getcwd())

for item in curr_dir:
    if item.endswith(".pdf"):
        correct_name = item[:7]
        os.rename(item, "MRS-" + correct_name + "-MRS-1" + ".pdf")
