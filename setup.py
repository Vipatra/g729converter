from setuptools import setup
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError

from setuptools import setup

import os

cwd = os.path.dirname(os.path.realpath(__file__))

print("CWD: ", cwd)

c_installation_file = os.path.join(cwd, 'install_c_lib.sh')


class sdist(sdist_orig):
    def run(self):
        try:
            self.spawn(['bash', c_installation_file])
        except DistutilsExecError:
            self.warn('listing directory failed')
        super().run()


setup(name='dpdg729',
      version='0.1',
      description='Convert wav to g729',
      url='https://github.com/ranjith19/g729converter',
      author='Ranjith BR',
      author_email='ranjith@dpdzero.com',
      license='Closed source',
      cmdclass={
        'sdist': sdist
      },
      packages=['dpdg729'],
      zip_safe=False)