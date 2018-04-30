#!/usr/bin/env python3
# This is an example interface, which must be implemented by src/cli-app-generator/<language>.py

'''
/* CPP template: */
#include <string>
#include <vector>
// TODO: expand all these rlib headers before release.
#include <rlib/opt.hpp>
#include <rlib/terminal.hpp>
#include <rlib/stdio.hpp>

using namespace rlib::literals;

$interface_classname hustgen_impl;

class parser {
private:
    static void print_help() {
        std::string help_msg = R"_RHELPG_(
            rcodegen backend v1.00

            >>> Usage: ./main <command> [args ...]

            >>> Commands:
            CommandName [Argument ...] -> ReturnValue # Instructions

            help -> null # Show this message.
            $funcname [$argname:$argtype, ...] -> $returntype
                ...
        )_RHELPG_";
        rlib::print(help_msg);
    }
public:
    static void parse(const std::vector<rlib::string> &to_parse) {
        if (to_parse.empty())
            return;
        rlib::print(std::boolalpha);

#define AREA_BEGIN if(to_parse.begin()->empty()) {}
#define IFCMD(str) else if(*to_parse.begin() == str)
#define AREA_END else

#define WANT_ARG(n) if(to_parse.size() != n+1) {throw std::runtime_error("{} arguments wanted but {} provided."_format(n, to_parse.size()-1));}

        AREA_BEGIN

        IFCMD("$funcname") {
            WANT_ARG(sizeof...(($argtype) ...))
            $if ($novoid($return_type))
            auto return_val = 
            $endif
            hustgen_impl.$funcname(to_parse[1].as<$argtype>(), to_parse[2].as<$argtype>(), ...);
            $if ($novoid($return_type))
            rlib::println(return_val);
            $endif
        }
            ...

        IFCMD("help")
            print_help();

        AREA_END
            throw std::invalid_argument("Invalid command. Try `help` to get helped.");
    }
};

int main(int argc, char **argv) {
    std::vector<rlib::string> args;
    for(char *p = argv[0]; p; ++p) {
        args.push_back(rlib::string(p));
    }
    parser::parse(args);
    return 0;
}
'''

def compile_cliapp_from_interface(funclist, output_main_location):
    """ @arg: funclist = [(func_name_str, return_type_str, [(arg_type_str, arg_name_str), ...], ), ...]
              output_main_location = str
                  where to generate source for main (main.c for C, main.cpp for C++, main.go for Golang, main.py for Python, Main.java for java).
        @return: None
    """


