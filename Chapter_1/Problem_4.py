#Q4. WAP to print content of a directory using os module.

import os
doc_path= r'\Users\midhu\Downloads\Programs\Python\Python_CodeWithHarry_programs\Chapter_1'
contents =os.listdir(doc_path)
for item in contents:
    print(item)

''''

\Users\midhu\Downloads\Programs\Python\Python_CodeWithHarry_programs\Chapter_1' 
is written with backslashes (\). In Python, backslashes are escape characters.
Therefore, either use forward slashes(/) or use "r" infront of the path to work 
the code perfectly.

'''    