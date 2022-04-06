How to contribute
=================

* Use our Slack channel ICESat2 - Coastal or GitHub issues to suggest new things we might work on or changes to our repo. 
* Use the ``contributors`` directory to add notebooks or try out ideas. You can use the ``examples`` notebooks as templates.
* Add an issue if you make a function or notebook that you think would be good to incorporate into ``coastal`` or ``examples`` but don't want to do that yourself.
* ``coastal`` directory: Here we have functions that can be used across our examples. Please add a documentation header to your functions. See existing functions for examples. We are using the [numpy documentation style guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* ``examples`` directory: Here we have notebooks that work fully through an example. Note after adding an example, you need to edit ``docs/source/index.rst`` and add it so that it shows up in the docs.
* ``docs`` directory: This is the code that used to generate the landing page https://icesat-2hackweek.github.io/coastal_topobathy/. If you want to update a page to the docs it goes here. You can also post an issue with the suggested change/addition, if you don't want to go into ``docs`` yourself. 

Changing the documentation
---------------------

The documentation pages are generated automatically when you push content to the repo (main branch) to the ``coastal`` or ``examples`` folders, with the caveat that if you add an example you also need to edit ``docs/source/index.rst`` and add it to the list of examples so that it shows up in the docs.
If you want to edit the documentation layout. Here is what you need to know. Everything you want is in ``docs/source``.

* To add a new page to the side-bar:  
    * Add a ``.rst`` file to `source`. 
    * Edit ``index.rst`` and add where you want it. It'll be obvious when you open ``index.rst``
* To add a new example: 
    * After adding the notebook to ``examples``, add the example to the examples section in ``index.rst``
* To add move info to an existing page: 
    * Just edit that ``.rst`` file in ``docs/source``
* To change the look of the side bar
    - *Is it part of Index or API or Links?* Look in ``source/_templates/layouts.html``. You'll see the code for add/edit that there.
    - *Is it examples or the main pages?* Look in ``source/index.rst``
* Where is the html and how is it created?
    * It is on the ``gh-pages`` branch and GitHub Pages is set to build the docs off of that branch.
    * The html is being created by ``sphinx`` using the makefile in ``docs`` and ``docs/source/conf.py``
    * *Want to futz with the Sphinx part?* Edit ``docs/source/conf.py``
* What triggers the docs build?
    * A GitHub Action  ``.github/workflows/docs_pages.yml`` is what is running sphinx and some other stuff.
    * *How are the examples notebooks getting converted to markdown?* That's happening in the ``docs_pages.yml`` via ``nbconvert`` though we may switch to ``jupytext``.
    * *Are the examples notebooks getting executed to make the markdown?* No. They do have ipyleaflet widgets so we have to save the widget state so the ipyleaflet plots show up.
* How is the API references generated from the code?
    * `sphinx-autoapi <https://sphinx-autoapi.readthedocs.io/>`_ extension is being used. I had changed the ``index.rst`` template for ``autoapi`` to get to change the title to Reference instead of API Reference.

