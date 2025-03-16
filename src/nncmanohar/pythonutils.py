import pkgutil
from pprint import pprint as pp

def show_sub_packages_and_modules(package_name):
  package = package_name

  package_names=[]
  module_names=[]
  #print(f"Sub packages of {package}")
  if hasattr(package, "__path__")  and hasattr(package, '__name__'):
    for finder, name, ispkg in pkgutil.iter_modules(package.__path__, package.__name__+'.'):
      if (not name.replace(str(package.__name__)+".",'').startswith('_')):
        if ispkg:
          package_names.append(name)
        else:
          module_names.append(name)

    if package_names:
      print(f"Below packages exist in {package.__name__}")
      pp(package_names)
    else:
      print(f"No packages are found in {package.__name__}")  

    if module_names:  
      print(f"Below Modules exist in {package.__name__}")
      pp(module_names)
    else:
      print(f"No modules are found in {package.__name__}")  
  else:
    print(f"{str(package)} does not seems to be a package")

