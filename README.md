# Python Users Group Intranet Site 

See the [Jupyter Book documentation](https://jupyterbook.org/en/stable/intro.html) for information on how the site was set up and should be maintained moving forward. The site was initially created from the [v0.13.0](https://jupyterbook.org/en/stable/reference/_changelog.html#v0-13-0-2022-06-02) release. 

## Directory Structure
```
├── .github
│   └── workflows           <- Update GitHub Actions workflow here 
├── requirements.txt
└── site
    ├── _build              <- Static site files, do NOT manually update these! 
    ├── _config.yml         <- Update Jupyter Book configuration here
    ├── _static             <- Update CSS here
    ├── _toc.yml            <- Update Jupyter Book table of contents here 
    ├── content             <- Update content here 
```

## Add or Update Content 
1. Install the necessary packages:  
```
$ pip install -r requirements.txt 
```

2. Update the relevant files in the `site/content/` folder. Jupyter notebooks or Markdown files will work best. 

3. Update the table of contents in the `site/_toc.yml` file if necessary (e.g. if you added an altogether new page). 

4. Build the HTML. Note that the static files will be placed in the ` _build/html` folder: 
```
$ jupyter-book build site/
```

By default, Jupyter Book will only build the HTML for pages that have been updated since the last time you built the book. To force the full site to rebuild without caching: 

```
$ jupyter-book build --all site/
```

5. Preview the site locally by either clicking on the HTML files in the `site/build_` folder or entering the absolute path in your browser (e.g. `file://Users/my_path_to_repo/site/_build/html/index.html`). 

6. Add, commit, and push to GitHub. Updates to the `master` branch will automatically trigger a GitHub action to copy the contents to the `gh-pages` branch. This will automatically deploy via GitHub Pages, and your changes should be live after a few minutes. 

## Modify Site Formatting  
To update site formatting, modify the CSS files in `site/_static/`. To update Jupyter Book configurations, modify the `site/_config.yml` file. 


## Check Links 
Periodically, it's useful to make sure the site doesn't have stale links, which Jupyter Book make easy: 
```
$ jupyter-book build site/ --builder linkcheck
```