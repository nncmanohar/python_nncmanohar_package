import pkgutil
import pkg_resources
from pprint import pprint as pp

def show_methods_of_a_class(cls):
    """Inspects a class and distinguishes its methods."""

    from pprint import pprint as pp 
    built_in_methods = []
    slot_wrappers = []
    static_methods = []
    instance_methods = []
    other_methods=[]

    for name, attr in cls.__dict__.items():
        if isinstance(attr, staticmethod):
            static_methods.append(name)
        elif isinstance(attr, type(str.__add__)): #checks if it is a wrapper descriptor, which slots are
            slot_wrappers.append(name)
        elif callable(attr) and not name.startswith('__'): #any callable that is not a special method.
            instance_methods.append(name)
        elif callable(attr) and name in dir(dict) and name.startswith('__'):
            built_in_methods.append(name)
        else:
            other_methods.append(name)
    print(f"Static methods: ")
    pp(static_methods)
    print(f"Instance methods: ")
    pp(instance_methods)
    print(f"Built-in methods:")
    pp(built_in_methods)
    print(f"Slot wrappers: ")
    pp(slot_wrappers)
    print(f"Other methods: ")
    pp(other_methods)

def show_installed_packages(filter=None):
  installed_packages = pkg_resources.working_set
  installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
  if filter:
      installed_packages_list=[package for package in installed_packages_list if filter in package]
  pp(installed_packages_list)
  
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

