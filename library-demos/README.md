# PDF Library Demos

This folder provides demos of two python PDF libraries I researched to use in my FYP

## Requirements

[Python 3.x](https://www.python.org/downloads/)

I use [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) a packaging tool to simplify the pip -> venv -> requirements.txt workflow.

```sh
$ pip install --user pipx

$ pipx install pipenv
```

## Installation

If you already have Pipenv installed run these commands to install our dependencies or go install.

From the `library-demos` directory:
```sh
$ pipenv shell

$ pipenv install
```

And you are ready to go.

## Usage

In the folder there are two files `pdfkit-demo.py` and `pypdf2-demo.py` In there I have code showing the basic usage of each library. You can run each one and see the results in the PDF's they generate.

Usage is simple:
```sh
python pdfkit-demo.py
```
