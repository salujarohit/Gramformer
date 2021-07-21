import setuptools

setuptools.setup(
    name="gramformer",
    version="1.0",
    author="prithiviraj damodaran",
    author_email="",
    description="Gramformer",
    long_description="A framework for detecting, highlighting and correcting grammatical errors on natural language text",
    url="https://github.com/PrithivirajDamodaran/Gramformer.git",
    packages=setuptools.find_packages(),
    install_requires=['transformers @ git+https://github.com/huggingface/transformers@v4.8.2#egg=transformers', 'sentencepiece==0.1.95', 'python-Levenshtein==0.12.2', 'fuzzywuzzy==0.18.0',  'tokenizers', 'fsspec==2021.5.0', 'lm-scorer', 'errant'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)
