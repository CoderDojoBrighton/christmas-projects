# Christmas Projects

## Presentation

The presentation can be launched with

```shell
python code/presentation/presentation.py
# or
make presentation
```

## Projects

Code for each project can be in the `code` folder.


### Christmas Tree - Python

A Christmas tree with turtle graphics.

To run:
```shell
python code/christmas-tree.py
```

### Snowman - Python

A snowman with turtle graphics``

To run:
```
python code/snowman.py
```


## Running Docs Site Locally

This repository uses submodules.
To ensure you have everything you need, clone recursively:
```shell
git clone --recursive https://github.com/CoderDojoBrighton/christmas-projects.git
```

We use the static site generator [Hugo](https://gohugo.io/).
You can find the installation instructions [here](https://gohugo.io/installation/).

To run the docs:
```shell
hugo serve
# Or
make docs
```
This should live-reload as you edit content.


## Editing Tips

The docs site uses the following layout:

```
christmas-projects
├─ hugo.toml - Site settings
├─ content/
|  ├─ _index.md - Main page content
|  ├─ docs/
|  |  ├─ python/
|  |  |  ├─ _index.md - Python page contents. Defines sidebar settings
|  |  |  ├─ project-name
|  |  |  |  ├─ _index.md - Content for project-name 
```

Hugo uses [Markdown](https://www.markdownguide.org/basic-syntax/).

Additionally, [shortcodes](https://gohugo.io/content-management/shortcodes/) can be used - essentially templates for content.
For example, highlightable code blocks, YouTube video player and Gists.
The theme we use provides [additional shortcodes](https://hugo-book-demo.netlify.app/) for things like mermaid diagrams, hints and expandable sections.

Photos should be added to `static/project-name/...`.
They can then be added to a page like this:
```markdown
![Description here](/christmas-projects/project-name/...)
```

