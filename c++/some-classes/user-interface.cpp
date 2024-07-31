#include "user-interface.hpp"

bool UserInterface::prompt()
{
    std::string user_input;

    return false;
}

void UserInterface::prompt_loop()
{
    bool do_continue = true;
    do {
        do_continue = prompt();
    } while (do_continue);
}

void UserInterface::add_new_record()
{
}

void UserInterface::edit_record()
{
}

void UserInterface::print_record()
{
}

void UserInterface::delete_record()
{
}
