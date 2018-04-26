#/usr/bin/env python3
# This is an example interface, which must be implemented by src/ui/<gui-generater>.py
def generate_ui(funclist, output_project_dir):
    """ @arg: funclist = [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...] 
                  All type str has been transformed to a uniform format (refer to src/translate.py).
              output_project_dir = str()
        @action: Generate a complete project with requirements below.
            - All files (html/binary executable/css/js/py/jar executable/other resource...) except dependency libraries
              must be in output_project_dir.
            - Can be safely moved/copied to other path / other computer (with dependency installed).
            - Can be launched by type `$output_project_dir/run.sh` in terminal (cmd for windows), and must block the caller process.
        @return: null
    """
    return

if __name__ == '__main__':
    print(generate_funclist_from_files(sys.argv[2:], sys.argv[1]))

