__author__ = 'liashi'

import argparse
import ConfigParser
from emulator_writer import emulator_writer
import shutil

def copy_emulator_source():

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AVD Manager")
    parser.add_argument("-e", "--iemi", help="The iemi string you want to write into the emulator")
    parser.add_argument("-m", "--imsi", help="The imsi string you want to write into the emulator")
    parser.add_argument("-b", "--buildprop", help="The build.prop path.")

    args = parser.parse_args()

    configParser = ConfigParser.ConfigParser()
    ConfigParser.optionxform = str
    configParser.read("AVDManager.properites")

    emulator_name = configParser.get("sdk", "emulator_path")[configParser.get("sdk", "emulator_path").rindex("/") + 1:]

    system_img_name = configParser.get("sdk", "system_img_path")[configParser.get("sdk", "system_img_path").rindex("/") + 1:]

    shutil.copyfile(configParser.get("sdk", "emulator_path"), "./output/" + emulator_name)

    shutil.copyfile(configParser.get("sdk", "system_img_path"), "./output" + system_img_name)


    if args.iemi:
        emulator_writer.write_iemi("./output/" + emulator_name, "123456789012345")
    if args.imsi:
        emulator_writer.write_imsi("./output/" + emulator_name, "310260123456789")
    if args.buildprop:
        pass