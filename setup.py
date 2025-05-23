# Copyright (c) 2021-2024 Tommaso Carraro
# Licensed under the MIT License. See LICENSE file in the project root for details.

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LTNtorch",
    version="1.0.2",
    packages=find_packages(include=["ltn"]),
    install_requires=["numpy", "torch"],
    python_requires=">=3.7",
    url="https://github.com/bmxitalia/LTNtorch",
    download_url="https://github.com/bmxitalia/LTNtorch",
    license="MIT",
    author="Tommaso Carraro",
    author_email="tommaso.carraro@studenti.unipd.it",
    description="LTNtorch: PyTorch implementation of Logic Tensor Networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "pytorch",
        "machine-learning",
        "framework",
        "neural-symbolic-computing",
        "fuzzy-logic",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
)
