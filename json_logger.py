''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line
 
util_submodule_l = ['file_system_utils']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules
 
# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l
 
''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
 
from util_submodules.file_system_utils import file_system_utils as fsu    ; util_submodule_import_check_count += 1
 
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
 
 
import jsonplus__non_merged as json
import os.path
 
 
# changes values of headers already in the file, and appends lines with new headers to the end, or creates new file if dosn't already exist
def log_vars(log_dict, json_file_path):
    if os.path.isfile(json_file_path): 
        json_data = read(json_file_path)
    else:
        json_data = {}
 
    for log_header, log_val in log_dict.items():
        json_data[log_header] = log_val
 
    write(json_data, json_file_path)
                 
     
     
def write(data, output_file_path, indent = 4):
    fsu.make_file_if_not_exist(output_file_path)
     
    with open(output_file_path, 'w') as outfile:  
         
        # if data is a namedtuple, write it as a dict
        if isinstance(data, tuple) and hasattr(data, '_asdict'):
            json.dump(data._asdict(), outfile, indent = indent)
        else:
            json.dump(data, outfile, indent = indent)
 
 
def read(json_file_path):
    with open(json_file_path, "r") as read_file:
        data = json.load(read_file)
    return data
     
     
     
def read_fast(json_file_path):
    with open(json_file_path, "r") as read_file:
        return json.load(read_file)
 
 
 
''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  json_logger')
     
    data = {}  
    data['people'] = []  
    data['people'].append({  
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({  
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({  
        'name': 'Tim',
        'website': [1,2,3,4],
        'from': 'Alabama'
    })
    # 
    #     
#     write(data,'missing_dir//json_test.jsond')
#     print(read('json_test.jsond'))
    # print(read('project_vars.json'))
     
     
    # var_data = {'a': 5,
    #             'b': 6}
    # 
    # #log_vars(var_data, 'test.json')
    # log_vars({'c': 11}, 'test.json')
     
     
     
     
     
     
     
     
     
     
     
     
    print('End of Main:  json_logger')



