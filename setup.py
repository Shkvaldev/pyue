from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="pyue",
    version="0.0.1",
    author="Shkvaldev",
    author_email="shkvalgrozny@gmail.com",
    description="Simple component-based Web UI generator in Python (inspired by Vue JS and Flutter)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shkvaldev/pyue",
    packages=find_packages(exclude=["__pycache__", "*.pyc"]),
    package_data={
        "pyue": ["skel/**/*", "skel/**/.*", "skel/*", "skel/.*"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require={
        "flask": ["flask"],
        "dev": [
            "pytest",
            "black",
        ],
    },
    entry_points={
        "console_scripts": ["pyue=pyue.cli:main"],
    },
)
