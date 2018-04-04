# HUST-Homework-General-UI
Are you still suffering from silly HUST CS homework? Are you still writing disgusting UI for HUST teachers? Now just implement your algorithm and I'll provide a simple but usable, cross-platform GUI, to pleasure your teacher!

Warning: This GUI is simply designed to pleasure HUST teacher. DO NOT 

## Designation
There's a example config.conf.

```conf
[ui]
ui-type = python-gui
# ui-type = java-gui
# ui-type = cpp-cui
# ui-type = cpp-faketerm

[source]
language = cpp
port = ~/code/hust/reflected_impl.hpp,~/code/hust-avl/reflected_impl.hpp
obj = ~/code/hust/compiled-object
```

This program will read port files, write some cpp/python code about the UI, build and link pre-built objects, and run it.

### Example port file:
```C++
#include <another.hpp>

__refl_class__ class port : public boost::noncopyable {
public:
    __refl_func__ string foo() {_do_something();}
    [[noreturn]]
    __refl_func__ void bar(size_t arg1, int arg2, const string &arg3) {_do_another_thing(arg1,arg2,arg3);}
}

extern port __r_refl_port;
```

### Launch UI:
```sh
hust-general-ui -c ~/code/hust/ds-final.conf
```

## TODO
All things are todo.
