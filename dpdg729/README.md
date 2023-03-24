# Converter from wav to g729 format

Copied from https://gitlab.linphone.org/BC/public/bcg729

## steps to compile the c lib

```
cmake . -DCMAKE_INSTALL_PREFIX=g729 -DCMAKE_PREFIX_PATH=g729 -DENABLE_TESTS=YES
make
make install
```