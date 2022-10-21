# Quarto for Python Demo 

## Setup 

See the [official Quarto documentation](https://quarto.org/) (specifically the [Using Python](https://quarto.org/docs/computations/python.html) section) to get set up. You'll need Python 3, Jupyter, and Quarto installed. You can verify that Quarto is configured correctly for Jupyter by running this: 

```
quarto check jupyter
```

If everything is set up, you should see something like this: 

```
[✓] Checking Python 3 installation....OK
      Version: 3.9.7 (Conda)
      Path: /Users/etyagi/opt/anaconda3/bin/python
      Jupyter: 4.9.2
      Kernels: ir, python3

[✓] Checking Jupyter engine render....OK
```

## Workflows

This directory demonstrates three workflows:  

* `jupyter-default`: Render an existing Jupyter notebook (.ipynb) as a Quarto document (e.g. html). 
    ```
    # Render to html 
    quarto render quarto-pug-demo-squirrels.ipynb

    # Render to html and execute cells 
    quarto render quarto-pug-demo-squirrels.ipynb --execute
    ```

* `jupyter-yaml`: Add YAML front matter to an existing Jupyter notebook (.ipynb) to take advantage of Quarto features when rendering as a Quarto document (e.g. html). 

    Add Quarto YAML document options to the top of the notebook in a Raw cell. 
    ```
    ---
    title: Python Lunch Lab - Quarto Demo 
    subtitle: The Squirrel Census (NYC Open Data Portal) 
    author: "Erika Tyagi"
    date: 2022-10-21  
    format:
        html:
            toc: true
            code-fold: true
            theme: urbn.scss
    ---
    ```

    ```
    # Render to html 
    quarto render quarto-pug-demo-squirrels.ipynb

    # Render to html and execute cells 
    quarto render quarto-pug-demo-squirrels.ipynb --execute
    ```

* `vscode`: Render a Quarto file (.qmd) as a Quarto document (e.g. html) and take advantage of features in the [Quarto VS Code extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto). 

    ```
    # Render to html 
    quarto render quarto-pug-demo-squirrels.qmd 
    ```

## Urban Styling 
See the `urbnquarto` [repository](https://github.com/UI-Research/urbnquarto) (credit to Aaron Williams!) and [this example web report](https://ui-research.github.io/urbnquarto/web-report.html). 

As demonstrated in the `jupyter-yaml` and `vscode` examples, to add Urban styling to a Quarto document, you'll need to [specify a SASS theme file](https://quarto.org/docs/output-formats/html-themes.html#theme-options) in the YAML header. For example: 

```
format:
    html:
        theme: urbn.scss
```
