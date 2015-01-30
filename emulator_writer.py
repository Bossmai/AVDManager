__author__ = 'Alfred'

class emulator_writer:

    @staticmethod
    def write_iemi(path, new_iemi):
        '''
        :param path:        The path of the emulator you want to modify. Normally points to the emulator source repo.
        :param new_iemi:    The iemi string you want to write into the emulator.
        :return:
        '''
        f = open(path, 'rb+')
        buf = f.read()
        index = buf.find('\x2b\x43\x47\x53\x4e')
        f.seek(index + 6)
        f.write(new_iemi)
        f.close()

    @staticmethod
    def write_imsi(path, new_imsi):
        '''
        :param path:        The path of the emulator you want to modify. Normally points to the emulator source repo.
        :param new_imsi:    The imsi string you want to write into the emulator. If it is not start with 310260, the emulator cannot connect to the Internet.
        :return:
        '''
        f = open(path, 'rb+')
        buf = f.read()
        index = buf.find('\x2b\x43\x49\x4d\x49')
        f.seek(index + 6)
        f.write(new_imsi)
        f.close


if __name__ == "__main__":
    emulator_writer.write_iemi("/Users/Alfred/Desktop/emulator64-x86", "123456789012345")
    emulator_writer.write_imsi("/Users/Alfred/Desktop/emulator64-x86", "310260123456789")
