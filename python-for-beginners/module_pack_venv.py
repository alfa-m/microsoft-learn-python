# Modules, packages and virtual environments (33-35) 
## Main file

### Import module as namespace
import sample_module_1 as samp
samp.display_1('Test message 1', False)
samp.display_1('Test message 2')
samp.display_1(is_alert = False)

### Import all package into current namespace
from sample_module_1 import *
display_2('Hello message 1', False)
display_2('Hello message 2')
display_2(is_hello = False)

display_3('Goodbye message 1', False)
display_3('Goodbye message 2')
display_3(is_adieu = False)

### Import specific modules into current namespace
from sample_module_2 import display_4, display_5
display_4('Uncolored message 1', False)
display_4('Uncolored message 2')
display_4(is_boring = False)

#### This example uses an package installed inside a virtual environment
#### Check the sample_module_2.py file
display_5('Uncolored message 3', False)
display_5('Colored message 1')
display_5(is_dope = False)
