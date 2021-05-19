import os

if __name__ == "__main__":
    folder_name = "Gintama"
    output_folder = "output"
    output_file_name = "collection.srt"
    with open(os.path.join(output_folder, output_file_name), "w") as out_f:
        for path, subdir, files in os.walk(folder_name):
            sorted_files = sorted(files)
            for file in sorted_files:
                with open(os.path.join(path, file), "r") as f:
                    for line in f:
                        out_f.write(f"{file}>>{line}")
                    #     print(f"{file}>>{line}")
                    # out_f.write(f"{file}\n")
                    # content = f.read()
                    # out_f.write(content)
