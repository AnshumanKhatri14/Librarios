from setuptools import setup, find_packages

VERSION='0.6'

setup(
    name="librarios",
    version=VERSION,
    description="A Library Management Program on python And MySQL",
    author="Anshuman",
    author_email="<anshumankhatri2004@gmail.com>",
    url="https://github.com/AnshumanKhatri14/Librarios",
    packages=find_packages(),
    license="MIT",
    install_requires=['mysql.connector','datetime'],
    keywords=['python','mysql'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "librarios=librarios.cli:mainf",
        ]
    },

)











