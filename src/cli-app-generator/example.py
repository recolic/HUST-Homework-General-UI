#!/usr/bin/env python3
# This is an example interface, which must be implemented by src/cli-app-generator/<language>.py
def compile_cliapp_from_interface(funclist, interface_classname, output_main_location):
    """ @arg: funclist = [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...]
              output_main_location = str
                  where to generate source for main (main.c for C, main.cpp for C++, main.go for Golang, main.py for Python, Main.java for java).
        @return: None
    """