from setuptools import find_packages, setup
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError
from setuptools.command.install import install

from setuptools import setup

import os

cwd = os.path.dirname(os.path.realpath(__file__))

print("CWD: ", cwd)

c_installation_file = os.path.join(cwd, 'install_c_lib.sh')



class InstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print("Running install command at %s" % os.getcwd())
        print("Items %s" % os.listdir(os.getcwd()))
        self.spawn(['bash', c_installation_file])
        install.run(self)


setup(name='dpdg729',
      version='0.1.0',
      description='Convert wav to g729',
      url='https://github.com/Vipatra/g729converter',
      author='Ranjith BR',
      author_email='ranjith@dpdzero.com',
      license='Closed source',
      cmdclass={
        'install': InstallCommand
      },
      packages='dpdg729',
      zip_safe=False)