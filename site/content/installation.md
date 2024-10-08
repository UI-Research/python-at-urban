# Installing Python

We recommend installing Python directly from the official website at [python.org](https://www.python.org/downloads/). Reach out to helpdesk@urban.org for the administrative permissions needed to do this. 

**When you install Python, make sure to check the box that says "Add Python to PATH". This will allow you to run Python from the command line.**

Note: We now recommend against using Anaconda due to recent changes in the terms of service.

To confirm Python and `pip` (a package management tool) are both installed correctly, open a command prompt or terminal and run the following in the command line:
`python --version` and `pip --version`.

## Choosing a Code Editor  

There are a number of different code editors or integrated development environments (IDEs) for Python. We recommend using [Visual Studio Code](https://code.visualstudio.com/) (or VS Code), which can be installed  from the [official website](https://code.visualstudio.com/download). VS Code can be used for standard .py files, as well as for Quarto and IPython notebooks (.qmd and .ipynb files).

VSCode includes support for debugging, syntax highlighting, code completion, and more. It also offers thousands of extensions (including [Python-specific extensions](https://code.visualstudio.com/docs/languages/python), a [Quarto extension](https://quarto.org/docs/tools/vscode.html), and an [AWS extension](https://aws.amazon.com/visualstudiocode/)).  

## Installing Packages 

We recommend using the package management tool `pip` that comes with Base Python. To install a package, you can run `pip install package-name` from the command line.

Note that this must be done from the command line and **not** the Python session (in contrast to package management in R).

If you are working on a computer that already has Anaconda installed (and predates the TOS changes), you can still use `conda-forge` (the open-source alternative to `conda`) to install packages. To do this, you can run:
- `conda config --add channels conda-forge`
- `conda install package-name`

## Running Code Interactively
To run Python code in Quarto notebooks or IPython notebooks (.ipynb files), we recommend installing the Jupyter package. You can do this by running `pip install jupyter` from the command line.)

We also recommend installing the following from the `Extensions` section of VS Code:
- Python
- Jupyter
- Quarto

## Using Virtual Environments 
 
To avoid running into version issues between multiple projects that rely on different Python versions or different versions of packages, you might want to try using virtual environments. A virtual environment is a way to create an isolated space so you can, for example, run Python 2.7 for one project and Python 3.7 for another on the same computer. 

We recommend using the `virtualenv` package, which can be installed by running `pip install virtualenv` on the command line. `virtualenv` includes robust support for creating and managing different environments. For more detail, see [this guide](https://ui-research.github.io/virtual-envs/) on using virtual environments at Urban or the official [virtualenv documentation](https://virtualenv.pypa.io/en/latest/).