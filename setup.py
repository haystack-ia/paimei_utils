from setuptools import setup

setup(
    name = "paimei_utils",
    version = "0.1",
    author = "haystack",
    author_email = "haystackinfosec@gmail.com",
    description = "a subset of PaiMei utils that are useful outside of PaiMei",
    license="GPL",
    packages=["paimei_utils"],
    install_requires=['pydbg']
)
