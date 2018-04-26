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
interface-class = interface
interface-source = ~/code/hust/reflected_impl.hpp
obj = ~/code/hust/compiled-object.o
```

This program will read interface files, write some cpp/python code about the UI, build and link pre-built objects, and run it.

### Example interface file:
```C++
#include <another.hpp>

class interface : public boost::noncopyable {
public:
    string foo() {_do_something();}
    [[noreturn]] void bar(size_t arg1, int arg2, const std::string &arg3) {_do_another_thing(arg1,arg2,arg3);}
}

extern interface __r_refl_interface;
```

### Launch UI:
```sh
hust-general-ui -c ~/code/hust/ds-final.conf
hust-general-ui-gen -c ~/code/hust/ds-final.conf -o ds-final.exe
```

## TODO
All things are todo.
