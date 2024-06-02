from setuptools import setup, find_packages

setup(
    name="hello_world_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project needs here
    ],
    entry_points={
        "console_scripts": [
            "hello=hello:hello_world",
        ],
    },
)
