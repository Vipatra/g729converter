from setuptools import find_packages, setup
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError
from setuptools.command.install import install

from setuptools import setup
import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))

print("CWD: ", cwd)


c_installation_file = os.path.join(cwd, 'install_c_lib.sh')

def get_virtualenv_path():
    """Used to work out path to install compiled binaries to."""
    if hasattr(sys, 'real_prefix'):
        return sys.prefix

    if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        return sys.prefix

    if 'conda' in sys.prefix:
        return sys.prefix

    return None



class InstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        target = get_virtualenv_path()

        print("installing to", target)
        self.spawn(['bash', c_installation_file, target])
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
      packages=['dpdg729'],
      include_package_data=True,
      zip_safe=False
)