import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="accoustid-music-cleaner",
    version="0.0.1",
    author="George Ndirangu",
    author_email="ndirangu.mepawa@gmail.com",
    description="Updates your music's metadata using accoustid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ndirangug/music-cleaner_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)