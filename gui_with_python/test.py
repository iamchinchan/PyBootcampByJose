import ipywidgets as widgets
from IPython.display import display

w = widgets.HTMLMath(
    value=r"Some math and <i>HTML</i>: $x^2$ and $$\frac{x+1}{x-1}$$",
    description='Some HTML'
)
display(w)
