from setuptools import setup, find_packages

setup(
    name="cryzen",
    version="0.1.1",
    description="Small focused cryptography & hashing utilities",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mahadi bin iqbal",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.7",
    install_requires=[
        "pycryptodome>=3.10; platform_system!='Windows' or True"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
