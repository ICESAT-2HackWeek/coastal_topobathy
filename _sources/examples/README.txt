Tips for ensuring that the notebooks show up correctly in the project documentation

These Jupyter notebooks will be displayed in the Sphinx documentation. If there are ipyleaflet or other widgets in the notebook, you need to make sure that `Save Widget State Automatically` is check under `Settings` in JupyterLab. That way the widget state will be saved when you save the notebook and the ipyleaflet plots will show up when the notebook is converted to markdown by `nbconvert`.

For some reason, the first code block will be run by nbconvert and will show an error since the Python packages won't be available. 

Notebooks can take a very long time to save (minutes), especially those with ipyleaflet plots and you need to fully save for the current version to show up. Watch at the bottom for the 'saving started' notice to disappear.

Make sure the first markdown heading is level one: `# heading` not level 2 `## heading` otherwise the notebook won't appear in the table of contents correctly.