from nbconvert.preprocessors import *
import nbformat as nbf

initial_cell = dict(metadata=dict(),cell_type='markdown',source="""<table align="left" style="border-style: hidden" class="table"> <tr> <td class="col-md-2"><img style="float" src="http://prob140.org/assets/icon256.png" alt="Prob140 Logo" style="width: 120px;"/></td><td><div align="left"><h3 style="margin-top: 0;">Probability for Data Science</h3><h4 style="margin-top: 20px;">UC Berkeley, Spring 2018</h4><p>Ani Adhikari</div></td></tr></table><!-- not in pdf -->""")

class MainPreprocessor(Preprocessor):
    def preprocess(self, nb, resources):
        """



        """
        if '<table' not in nb['cells'][0]['source']:
            nb['cells'].insert(0,nbf.from_dict(initial_cell))
        return nb,resources


