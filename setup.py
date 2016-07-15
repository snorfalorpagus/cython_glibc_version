from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("hello", ["hello.pyx"], include_dirs=["."])
]

setup(name="Hello", ext_modules=cythonize(extensions))
