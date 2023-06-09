import os
import subprocess
import logging
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('g729converter')
cwd = os.path.dirname(os.path.realpath(__file__))


class ConversionError(Exception):
    pass


def convert_wav_to_g749(file_path):
    expected = file_path.replace('.wav', '.G749')
    output = subprocess.run(["g749Encoder", file_path], env={'LD_LIBRARY_PATH': os.path.join(sys.prefix, 'lib')}, capture_output=True)
    if os.path.exists(expected):
        log.error("Unable to convert file: %s due to %s" % (file_path, output))
        raise ConversionError("Unable to convert file: %s due to %s" % (file_path, output))
    return expected




if __name__ == "__main__":
    f = convert_wav_to_g749('/home/ubuntu/test.wav')
    log.info(f"File is at {f}")
