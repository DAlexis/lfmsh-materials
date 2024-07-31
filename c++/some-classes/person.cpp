#include "person.hpp"

Person::Person(const std::string& name)
{
    m_name = name;
}

std::string Person::get_name() const
{
    return m_name;
}

void Person::set_name(const std::string& name)
{
    m_name = name;
}

int Person::get_age() const
{
    return m_age;
}

void Person::set_age(int age)
{
    m_age = age;
}
