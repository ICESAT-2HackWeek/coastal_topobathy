# How the Sphinx docs work

Everything you want is in `source`

## To add a new page to the side-bar

* Add a `.rst` file to `source`.
* Edit `index.rst` and add where you want it. It'll be obvious when you open `index.rst`

## To add a new example

* Add the example to the examples section in `index.rst`

## To add move info to an existing page

* Just edit that `.rst` file

## To change the look of the side bar

* **Is it part of Index or API or Links?** Look in `_templates/layouts.html`. You'll see the code for add/edit that there.
* **Is it examples or the main pages?** Look in `source/index.rst`

