#!/usr/bin/env python3

import sys
import shutil
import os
import subprocess
import argparse
import json
import time
import qrcode

script_dir = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(script_dir, template_name)

with open(os.path.join(script_dir, "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)
with open(os.path.join(script_dir, "package.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

template_name = config["default_template"]
open_file = config["open_after_create"]
createIO = config["create_in_out"]

def printVersion():
    print("newcpp {ver}".format(ver=data["version"]))
    exit()

def openConfig():
    subprocess.run(["code", os.path.join(script_dir, "config.json")])
    time.sleep(1)
    subprocess.run(["open", script_dir])
    print("\033[32m [DONE] \033[0m Opened \033[33mconfig.json\033[0m successfully.")
    exit()

def openTemplate():
    subprocess.run(["code", template_path])
    time.sleep(1)
    subprocess.run(["open", script_dir])
    print("\033[32m [DONE] \033[0m Opened {tmp} successfully.".format(tmp=template_name))
    exit()

def kheuDonate():
    print("Thank you so much for using our product!!!")
    print("If you have too much money, you can donate us through these methods...")
    print("\033[33mONLY AVAILABLE IN VIET NAM (I think...)\033[0m")
    print("\033[32mBIDV\033[0m 8863663977 \033[36mNGHIEM TUAN DUNG\033[0m")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data("00020101021138540010A00000072701240006970418011088636639770208QRIBFTTA53037045802VN63042144")
    qr.make(fit=True)
    qr.print_ascii(invert=True)
    print("\033[32mZaloPay\033[0m \033[36mNGHIEM TUAN DUNG\033[0m")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data("00020101021126400010vn.zalopay0115gMsimoNQIsViRgP020300238620010A00000072701320006970454011899ZP24284M453437190208QRIBFTTA5204739953037045802VN630414A8")
    qr.make(fit=True)
    qr.print_ascii(invert=True)
    print("\033[32mShopeePay\033[0m \033[36mNGHIEM TUAN DUNG\033[0m")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data("https://sppay.shopee.vn/qr/00f4ccc13787251512b0")
    qr.make(fit=True)
    qr.print_ascii(invert=True)
    print("Thank you so much! Cảm ơn rất nhiều! Merci beaucoup! ありがとうございます！ ¡Muchas gracias! 谢谢! Большое спасибо! ຂອບໃຈຫຼາຍໆ! Muito obrigada! ...")
    exit()


def createNewFile(args):
    filename = args.filename
    ovw = args.overwrite
    current_dir = os.getcwd()
    destination_path = os.path.join(current_dir, filename)
    input_path = os.path.join(current_dir, filename[:-3]+"INP")
    output_path = os.path.join(current_dir, filename[:-3]+"OUT")

    if (os.path.exists(filename) and (not ovw)):
        overwrite = input(f"File {filename} already exists. Do you want to overwrite it (Y/n): ").lower()
        if (overwrite=='n'):
            print("\033[31m[ABORTED]\033[0m File already exists. Aborting creation process.")
            exit()

    if not os.path.exists(template_path):
        print("\033[31m[ERROR]\033[0m \033[33mSAMPLE.cpp\033[0m not found!")
        exit()

    shutil.copyfile(template_path, destination_path)

    with open(destination_path, "r") as f:
        lines = f.readlines()

    with open(destination_path, "w") as f:
        for line in lines:
            if "g++" in line and "X.cpp" in line:
                line = line.replace("X.cpp", filename)
            f.write(line)

    if (open_file): subprocess.run(["code", destination_path])
    print("\033[32m [DONE] \033[0m \033[33m{fn}\033[0m".format(fn=filename),end="")

    if (createIO or args.io):
        with open(filename[:-3]+"INP", "w") as f:
            pass
        with open(filename[:-3]+"OUT", "w") as f:
            pass
        if (open_file): subprocess.run(["code", input_path])
        if (open_file): subprocess.run(["code", output_path])
        print(", \033[33m{inp}\033[0m, and \033[33m{out}\033[0m".format(inp=(filename[:-3]+"INP"),out=(filename[:-3]+"OUT")),end="")
    print(" created successfully.")

    exit()


def main():

    parser = argparse.ArgumentParser(description="Create new \033[33m.cpp\033[0m file from a template (e.g. \033[33mSAMPLE.cpp\033[0m)")
    
    parser.add_argument(
        "filename",
        type=str,
        nargs="?",
        help="The name of the \033[33m.cpp\033[0m file to be created"
    )
    
    parser.add_argument(
        "--overwrite",
        "--o",
        action="store_true",
        help="Overwrite if file already exists"
    )

    parser.add_argument(
        "--io",
        action="store_true",
        help="Create input, output file with \033[33m.cpp\033[0m file"
    )

    parser.add_argument(
        "--version",
        "--v",
        action="store_true",
        help="Show help"
    )

    parser.add_argument(
        "--template",
        "--tmp",
        action="store_true",
        help="Show template file"
    )

    parser.add_argument(
        "--config",
        "--cf",
        action="store_true",
        help="Configure \033[33mnewcpp\033[0m"
    )

    parser.add_argument(
        "--donate",
        "--$",
        action="store_true",
        help="If you have too much money..."
    )

    args = parser.parse_args()

    if (args.version): printVersion()
    if (args.template): openTemplate()
    if (args.config): openConfig()
    if (args.donate): kheuDonate()
    if (args.filename): createNewFile(args)
    print("\033[33m[WARNING]\033[0m Wrong syntax. You should:\033[34m newcpp <file_name>.cpp\033[0m.\n\033[33m'--help'\033[0m for more information...")
    
if __name__ == "__main__":
    main()
