#!/usr/bin/env python3
""" Testing usage: call with <filename> <classname>
"""

import clang.cindex as cindex

def list_public_func(class_node):
    '''
    @return: [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...]
    '''
    result = []
    is_public = False
    for c in class_node.get_children():
        if c.kind == cindex.CursorKind.CXX_ACCESS_SPEC_DECL:
            if c.access_specifier == cindex.AccessSpecifier.PUBLIC:
                is_public = True
            else:
                is_public = False
        if not is_public:
            continue
        if c.kind == cindex.CursorKind.CXX_METHOD:
            # CursorKind.CONSTRUCTOR != CursorKind.CXX_METHOD, so do DESTRUCTOR.
            args = []
            for arg in c.get_arguments():
                args.append((arg.type.spelling, arg.spelling))
            result.append((c.spelling, c.result_type.spelling, args))
    return result

def find_class(root_node, classname):
    '''
    @return: class_node
    '''
    for c in root_node.get_children():
        if c.kind == cindex.CursorKind.CLASS_DECL and c.spelling == classname:
            return c

def libclang_parse(filename):
    index = cindex.Index.create()
    root = index.parse(filename).cursor
    return root

def generate_funclist_from_files(files, interface_class_identify):
    """ @arg: files = [file1, file2, ...]
              interface_class_identify = str()
        @return: funclist = [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...] 
    """
    assert(len(files) == 1)
    return list_public_func(find_class(libclang_parse(files[0], interface_class_identify)))

if __name__ == '__main__':
    import sys
    print(generate_funclist_from_files(sys.argv[2:], sys.argv[1]))
