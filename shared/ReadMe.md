## Structure

The `shared` folder has functions that can be used across any notebook.

* utils: utility functions
* functions: more involved functions that do something more complex
* demos: if someone wanted to run a notebook example say with a different location

Not sure if this is a good way to break things up. Maybe `demos` should just be a folder with notebooks in it.

## How to use

To use the shared functions in your notebook:

```
import sys
sys.path.append('/home/jovyan/coastal_topobathy')
from shared import coastal as co
```

List what modules are available within `co`

```
dir(co)
```

List what functions are available within the utils module

```
dir(utils)
```

Use a function

```
co.utils.print1()
```

## How to contribute

### Let's say you wanted to add a function to the utils module.

* Add your `.py` file to the `utils` folder or edit one of the existing `.py` files in that folder.
* Edit `utils/__init__.py` with the function you want to import into the utils module.

### Let's say you wanted to add a new module called `foo` to the coastal module.

Option 1: 
* Add your `foo.py` file with all your functions to shared. 
* Add `from shared import foo.py` to `coastal.py`

Option 2: If your module functions are broken into different files
* Take a look at the files in the utils folder
* Add a folder called `foo`. 
* Add your individual `.py` files with your functions.
* Add `__init__.py` to the `foo` folder.
* Edit `__init__.py` to import the functions in the `.py` files

### Let's say you wanted to add a new module called `foo` NOT part of the coastal module

* Add your `foo.py` file with all your functions to shared. 

Team members will now get your module with

```
import sys
sys.path.append('/home/jovyan/coastal_topobathy')
from shared import foo
```

