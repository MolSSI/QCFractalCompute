"""
QCPortal
A client interface to the QC Archive Project
"""
from setuptools import setup, find_packages
import versioneer

short_description = "A client interface to the QC Archive Project."

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except FileNotFoundError:
    long_description = short_description

setup(
    # Self-descriptive entries which should always be present
    name='qcfractalcompute',
    author='MolSSI',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    python_requires=">=3.7",
    license='BSD-3-Clause',
    # Which Python importable modules should be included when your package is installed
    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'qcportal',
        'qcengine',
    ],

    entry_points={
        "console_scripts": [
            "qcfractal-manager=qcfractalcompute.qcfractal_manager_cli:main",
        ],
    },

    tests_require=[
        'pytest',
        'pytest-cov',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    zip_safe=True,
)
