# Installing Python

## Python 2 or 3? 

[**Python 2.x is legacy, Python 3.x is the present and future of the language.**](https://wiki.python.org/moin/Python2orPython3)

There are two versions of Python - Python 2 and Python 3. Unless you have inherited an old project that requires you to use Python 2, or need libraries that are available only in Python 2, then you should install and use Python 3 exclusively.

## Using Anaconda 

We strongly recommend using Anaconda if you want to use Python for data science. This will simplify dealing with things like privileges, environments and packages. 

Anaconda is a Python distribution that includes a Python interpreter, a number of Python packages (including pandas, numpy, and scipy), and tools like editors. To install, go to the [Anaconda Download page](https://www.anaconda.com/distribution/#download-section). Select Windows, MacOS, or Linux, then select a Python version, and click Download.

For a guided walk-through of installing and getting started with Anaconda, follow [this notebook](https://github.com/UI-Research/python-resources/blob/main/notebooks/anaconda-installation.ipynb) from a previous Python Users Group session. 

On opening Anaconda, you will be brought to the Navigator page from which you can launch various applications in order to run your code, including Jupyter Notebook and Spyder. 

Jupyter Notebook is similar to R Markdown, where you can edit and run blocks of code along with markdown text. It allows you to create and share documents that contain live code, equations, visualizations and narrative text. 

Spyder is an environment for running Python, similar to RStudio for R. It offers editing, analysis, and debugging. For tips on using Spyder, see [these resources](https://urbanorg.box.com/s/3raiuvsykulh290884xkogduzbdhi371) from a previous Python Users Group session. 

## Installing Packages 

Anaconda comes with a package management system called `conda`. To install a package, open your command prompt and run 

`conda install {package-name}`

Note that this must be done from the command line and **not** the Python session (in contrast to package management in R).

Base Python has its own package management tool called `pip`. If a package is not available with `conda install`, you can try running 

`pip install {package-name}`

You should always try running `conda install` first, as this will do a better job of resolving package dependency issues.

## Using Virtual Environments 
 
To avoid running into version issues between multiple projects that rely on different Python versions or different versions of packages, you might want to try using virtual environments. A virtual environment is a way to create an isolated space so you can, for example, run Python 2.7 for one project and Python 3.7 for another on the same computer. `conda` includes robust support for creating and managing different environments. For more detail, see the [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). 

## Choosing an IDE 

There are a number of different integrated development environments (IDEs) for Python. Some popular ones include:

* [Spyder](https://www.spyder-ide.org/) comes installed with Anaconda, and is most similar to RStudio for R. 
* [Jupyter](https://jupyter.org/) also comes with Anaconda, and is most similar to RMarkdown.
* [Visual Studio Code](https://code.visualstudio.com/) includes support for debugging, syntax highlighting, code completion, and more. It also offers thousands of extensions (including Python-specific extensions). 
* [PyCharm](https://www.jetbrains.com/pycharm/) is another popular Python IDE. The free version offers syntax highlighting, access to plugins, and web development support.

## Installing Python Directly

You can also install Python directly onto your machine rather than using Anaconda. See the Python [downloads page](https://www.python.org/downloads/) for the most up to date Mac, Linux, and Windows versions of Python. 