#include "book.hpp"

bool Book::add_person(const Person& p)
{
    std::map<std::string, Person>::iterator it = m_persons.find(p.get_name());
    if (it != m_persons.end())
        return false;
    m_persons.emplace(p.get_name(), p);
    return true;
}

const Person* Book::find_person(const std::string& name) const
{
    std::map<std::string, Person>::const_iterator it = m_persons.find(name);
    if (it == m_persons.end())
        return nullptr;
    return &it->second;
}

Person* Book::find_person(const std::string& name)
{
    std::map<std::string, Person>::iterator it = m_persons.find(name);
    if (it == m_persons.end())
        return nullptr;
    return &it->second;
}

int Book::count() const
{
    return m_persons.size();
}
