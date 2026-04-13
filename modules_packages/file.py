# from mainpackage import mainpackagefile
# from mainpackage import mainpackagefile, anotherhiddenfile
# from mainpackage import *
from mainpackage import anotherhiddenfile
from mainpackage.subpackage.subpackagefile import sub_func
# mainpackagefile.main_func()
# mainpackagefile.another_main_func()
anotherhiddenfile.hidden_func()
sub_func()
