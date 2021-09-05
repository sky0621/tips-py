# import pandas as pd
import tabula
from IPython.core.display import display

dfs = tabula.read_pdf("test.pdf", lattice=True, pages='1')

for df in dfs:
    display(df)
