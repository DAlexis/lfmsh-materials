project(phonebook)

add_compile_options(-Wall -Werror=return-type)
add_executable(phonebook main.cpp person.cpp person.hpp book.cpp book.hpp user-interface.cpp user-interface.hpp)
