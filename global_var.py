

_dict = {}

def _init():
    _dict.clear()

def set_value(name, value):
    _dict[name] = value

def get_value(name, defValue=None):
    try:
        return _dict[name]
    except KeyError:
        return defValue
    

# class global_var():
#     # This is a class, saving for global variables dictionary.
#     # It has functions, including set_value and get_value
#     def __init__(self):
#         self._dict = {}
    
#     def _init(self):
#         self._dict.clear()

#     def set_value(self, name, value):
#         self._dict[name] = value

#     def get_value(self, name, defValue=None):
#         try:
#             return self._dict[name]
#         except KeyError:
#             return defValue
        
#     def del_value(self, name):
#         del self._dict[name]
    
#     def clear(self):
#         self._dict.clear()    
        

