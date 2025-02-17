from setuptools import setup, find_packages

setup(
    name = "beetmon",
    version = "1.0.0",
    packages = find_packages(),
    install_requires = ["watchdog","beet","pyyaml"],
    entry_points = {
        "console_scripts": [
            "beetmon=beetmon.beetmon:main",
        ],
    },
    author="Your Name",
    description="A file watcher that runs 'beet build' on file changes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/beetmon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
