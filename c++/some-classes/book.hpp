#ifndef BOOK_HPP
#define BOOK_HPP

#include <map>
#include "person.hpp"

/**
 * @brief Класс, который олицетворяет записную книжку саму по себе
 *        ЗАДАНИЕ (очень дополнительное):
 *        * Добавить функцию поиска наиболее похожего имени
 */
class Book
{
public:
    bool add_person(const Person& p);
    const Person* find_person(const std::string& name) const;
    Person* find_person(const std::string& name);
    int count() const;

private:
    std::map<std::string, Person> m_persons;
};

#endif // PERSON_HPP
