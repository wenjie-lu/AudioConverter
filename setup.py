from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    install_requires = f.readlines()

setup(
    name="audioconverter",
    version="0.0.1",
    author="Wenjie Lu",
    author_email="luwenjie2002@gmail.com",
    description="A small package to convert audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wenjielu123/AudioConverter.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("."),
    package_dir={"": "."},
    install_requires=install_requires,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "converta=convert_audio:main",
            "convertv=convert_video:main",
        ]
    },
)
