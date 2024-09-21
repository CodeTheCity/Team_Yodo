import os
for file_type in ["train", "test", "valid"]:
    dir_path = f".\datasets\data\{file_type}\labels"

    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            with open(os.path.join(dir_path, file), "r") as f:
                lines = f.readlines()

            with open(os.path.join(dir_path, file), "w") as f:
                for line in lines:
                    line = line.split(" ")
                    line[0] = "0"
                    f.write(" ".join(line))