import os
import subprocess
import logging

log = logging.getLogger('g729converter')
cwd = os.path.dirname(os.path.realpath(__file__))

executable = os.path.join(cwd, 'test/encoderTest')

class ConversionError(Exception):
    pass

def convert(file_path):
    expected = file_path.replace('.wav', '.G749')
    output = subprocess.run([executable, file_path])
    if os.path.exists(expected):
        log.error("Unable to convert file: %s due to %s" % (file_path, output))
        raise ConversionError("Unable to convert file: %s due to %s" % (file_path, output))
    return expected




if __name__ == "__main__":
    convert('/home/ubuntu/test.wav')
