from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "Fortress SDK"
LONG_DESCRIPTION = (
    "SDK for accesssing and performing private computation on Fortress platform"
)

# Setting up
setup(
    name="fortress_sdk",
    version=VERSION,
    author="Fortress Labs",
    url="https://github.com/Atbash-Labs/python-sdk",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pysftp", "requests"],
    keywords=["python", "sdk package"],
    classifiers=["Health", "Private Computation", "Data Analysis", "SDK"],
)
