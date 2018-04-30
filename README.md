# HUST-Homework-General-UI

Are you still suffering from silly HUST CS homework? Are you still writing disgusting UI for HUST teachers? Now just implement your algorithm and I'll provide a simple but usable, cross-platform GUI, to pleasure your teacher!

Warning: This GUI is simply designed to pleasure HUST teacher. DO NOT 

## Designation
There's a example Hustuifile.

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
```

This program will read interface files, write some cpp/python code about the UI, build and link pre-built objects, and run it.

### Example interface file
```C++
#include <another.hpp>
#include <string>

class interface_helper {
    // some other thing
};

class interface : public boost::noncopyable {
public:
    interface() = default;
    ~interface() {}
    string foo() {
        _do_something();
    }
    [[noreturn]] void bar(size_t arg1, int arg2, const std::string &arg3);
};

[[noreturn]] void interface::bar(size_t, int, const std::string &) {
    //impl
}

extern interface __r_refl_interface;
```

### Usage
```sh
vim Hustuifile
hustui-make main
cd build && cmake .. && make && cd - # Build your own project with generated main.cpp
hustui-make ui
./ui.sh # Launch final cui/gui
hustui-make exe # Ready for final submit
```

## TODO
All things are todo.

I'm currently puzzled by some designation problems, and hesitating in some options:

- (backend|gRPC daemon) ~~~ (gRPC client|frontend) # Too heavy.

- (backend daemon) ~~ shell/exec ~~ (frontend) # must save/load by serialize/deserialize, which is expensive.

- (backend|simpler hand-designed RPC daemon) ~~~ (frontend) # Tiring.

- (backend|frontend daemon) # Too dirty. Hard to maintain.

Suggestions wanted!!!! (root@recolic.net)