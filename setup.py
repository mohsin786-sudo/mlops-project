from setuptools import setup, find_packages

setup(
    name ="my_package",
    version="0.0.1",
    author="Mohsin",
    author_email="kazimohsin778@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "flask"
    ],
)