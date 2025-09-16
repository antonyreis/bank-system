from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirementes.txt") as f:
    page_description = f.read().splitlines()
    
setup(
    name="bank_sys",
    version="0.0.1",
    author="Antony Matheus",
    author_email="tonyto.matheus@gmail.com",
    description="Bank System package with basic operations",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonyreis/bank-system",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10'
)