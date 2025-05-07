#!/usr/bin/env python3

import sys
import shutil
import os
import subprocess

def main():
    if len(sys.argv) != 2:
        print("\033[33m[WARNING]\033[0m Wrong syntax. You should:\033[34m newcpp <file_name>.cpp \033[0m")
        return
    
    filename = sys.argv[1]
    current_dir = os.getcwd()
    destination_path = os.path.join(current_dir, filename)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    sample_path = os.path.join(script_dir, "SAMPLE.cpp")

    if not os.path.exists(sample_path):
        print("\033[31m[ERROR]\033[0m \033[33mSAMPLE.cpp\033[0m not found!")
        return

    # Copy file template
    shutil.copyfile(sample_path, destination_path)

    # Replace dòng biên dịch
    with open(destination_path, "r") as f:
        lines = f.readlines()

    with open(destination_path, "w") as f:
        for line in lines:
            if "g++" in line and "X.cpp" in line:
                line = line.replace("X.cpp", filename)
            f.write(line)

    # Open file in VSCode
    subprocess.run(["code", destination_path])
    print("\033[32m [DONE] \033[0m \033[33mSAMPLE.cpp\033[0m created successfully. ")

if __name__ == "__main__":
    main()
