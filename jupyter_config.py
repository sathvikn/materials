c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.export_format = 'notebook'
c.NbConvertApp.use_output_suffix = False
c.NbConvertApp.notebooks = ['**/*.ipynb']
c.Exporter.preprocessors = ['preprocessors.MainPreprocessor']
