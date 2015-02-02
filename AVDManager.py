__author__ = 'liashi'

import argparse
import ConfigParser
from emulator_writer import emulator_writer
import shutil
import os
import platform

def copy_emulator_source():

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AVD Manager")
    parser.add_argument("-e", "--iemi", help="The iemi string you want to write into the emulator.")
    parser.add_argument("-m", "--imsi", help="The imsi string you want to write into the emulator.")
    parser.add_argument("-p", "--port", help="The port AVD use.")
    parser.add_argument("-b", "--buildprop", help="The build.prop path.")
    parser.add_argument("-o", "--output", help="Output path for system.img.")

    args = parser.parse_args()

    configParser = ConfigParser.ConfigParser()
    ConfigParser.optionxform = str
    configParser.read("AVDManager.properites")

    #system_img_name = configParser.get("sdk", "system_img_path")[configParser.get("sdk", "system_img_path").rindex(os.sep) + 1:]
    #shutil.copyfile(configParser.get("sdk", "system_img_path"), "./output/" + system_img_name)

    if args.iemi or args.imsi:
        emulator_name = configParser.get("sdk", "emulator_path")[configParser.get("sdk", "emulator_path").rindex(os.sep) + 1:]
        emulator_name_after = ""

        if platform.system() == "Windows":
            emulator_name_after = emulator_name[0: emulator_name.index("-")] + "-" + args.port + ".exe"
        elif platform.system() == "Linux":
            emulator_name_after = emulator_name[0: emulator_name.index("-")]  + "-" + args.port

        shutil.copyfile(configParser.get("sdk", "emulator_path"), emulator_name_after)



        shutil.move(emulator_name, emulator_name_after)

        if args.iemi:
            emulator_writer.write_iemi(emulator_name_after, args.iemi)
        if args.imsi:
            emulator_writer.write_imsi(emulator_name_after, args.imsi)

        shutil.move(emulator_name_after, configParser.get("sdk", "emulator_path")[0:configParser.get("sdk", "emulator_path").rindex(os.sep) + 1] + emulator_name_after)
    #if args.buildprop:
        #print platform.architecture()
        #extract the img file
        #os.system("./libs/yaffs2utils/unyaffs2 -f " + "./output/" + system_img_name)

        #overwrite the file

        #pack the img
