# Installing Python


## Installing Anaconda

There are countless ways to install Python, which can make knowing how to get started notoriously intimidating. For new users at Urban, we strongly recommend [Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/) as a great way to quickly set up and manage your Python environment. Anaconda is an open-source distribution that includes a Python interpreter, hundreds of useful Python packages for data science (including pandas, numpy, and scipy), and tools like code editors. 

To install Anaconda, simply go to the [Anaconda Download page](https://www.anaconda.com/distribution/#download-section), and click Download. We recommend the suggested defaults (i.e., install for "Just Me", use the default destination folder, and do not add Anaconda to your PATH environment). With these settings, you will NOT need administrator privileges to install Anaconda on your Urban computer.

Once you have successfully installed Anaconda, you can open the Anaconda Navigator. This is a graphical interface that lets you launch applications to run Python code. To launch the Anaconda Navigator, search for it from the Start menu. 

For more information, see the getting started guides for [Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/) and [Anaconda Navigator](https://docs.anaconda.com/navigator/getting-started/). 

## Choosing a Code Editor  

There are a number of different code editors or integrated development environments (IDEs) for Python. The most popular ones among users at Urban include the following: 

* [Jupyter Notebook](https://jupyter.org/) comes installed with Anaconda, and is similar to RMarkdown. Jupyter notebooks are web-based applications that let you edit and run blocks of code along with markdown text, equations, and visualizations in a single notebook file. 
* [Spyder](https://www.spyder-ide.org/) also comes installed with Anaconda and is most similar to RStudio for R. It offers editing, analysis, and debugging support for Python. 
* [Visual Studio Code](https://code.visualstudio.com/) (or VS Code) can be installed through Anaconda, and includes support for debugging, syntax highlighting, code completion, and more. It also offers thousands of extensions (including [Python-specific extensions](https://code.visualstudio.com/docs/languages/python), a [Quarto extension](https://quarto.org/docs/tools/vscode.html), and an [AWS extension](https://aws.amazon.com/visualstudiocode/)).  

## Installing Packages 

Anaconda comes with a package management system called `conda`. To install a package, open your command prompt and run 

`conda install package-name`

Note that this must be done from the command line and **not** the Python session (in contrast to package management in R).

Base Python has its own package management tool called `pip`. If a package is not available with `conda install`, you can try running 

`pip install package-name`

You should always try running `conda install` first, as this will do a better job of resolving package dependency issues.

## Using Virtual Environments 
 
To avoid running into version issues between multiple projects that rely on different Python versions or different versions of packages, you might want to try using virtual environments. A virtual environment is a way to create an isolated space so you can, for example, run Python 2.7 for one project and Python 3.7 for another on the same computer. `conda` includes robust support for creating and managing different environments. For more detail, see [this guide](https://ui-research.github.io/virtual-envs/) on using virtual environments at Urban or the official [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). 