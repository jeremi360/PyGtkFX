import os as _os
import importlib as _imp
imports = _os.listdir('.')
print(imports)
for i in imports:
    if i.split('.')[1] == 'py':
        n = i.split('.')[0]
        p = "grabbo." + n
        _imp.import_module(n.capitalize(), p)



