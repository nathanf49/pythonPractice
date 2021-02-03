from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.pyx")
)

# run 'python3 setup.py build_ext --inplace' in terminal to compile
# run python3 from command prompt and import helloworld to run