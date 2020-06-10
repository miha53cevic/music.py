from setuptools import setup, find_packages

setup(
    name="music.py",
    version="1.0",
    author="Mihael Petričević",
    packages=find_packages(),

    install_requires=["pygame", "mutagen"],
    
    # Create a console script named music that runs the main() function
    # from music.py
    entry_points = {
        "console_scripts": ["music=musicpy.music:main"]
    },
);