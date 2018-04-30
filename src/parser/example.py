#/usr/bin/env python3
# This is an example interface, which must be implemented by src/parser/<frontend>.py
def generate_funclist_from_files(files, interface_class_identify):
    """ @arg: files = [file1, file2, ...]
              interface_class_identify = str()
        @return: funclist = [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...] 
    """
    return []

if __name__ == '__main__':
    import sys
    print(generate_funclist_from_files(sys.argv[2:], sys.argv[1]))