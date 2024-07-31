#ifndef PERSON_HPP
#define PERSON_HPP

#include <string>

/**
 * @brief Этот класс олицетворяет запись в записной книжке.
 *        ЗАДАНИЕ:
 *        * Дополнить класс телефонным номером (string) с геттерами и сеттерами
 */
class Person
{
public:
    /**
     * @brief Конструктор класса принимает имя, которое является обязательныи
     *        для Person
     */
    Person(const std::string& name);

    /**
     * @brief Метод get_name является "геттером" для поля m_name. Он возвращает
     *        имя и является константным методом, что значит, что он не меняет
     *        никаких полей класса и может быть вызван у константного объекта
     *        (например, если мы имеем const Person& p;, то моно выхывать
     *        p.get_name();
     * @return собственно, само имя
     */
    std::string get_name() const;
    /**
     * @brief Метод set_name является "сеттером" - он устанавливает приватное поле
     *        класса
     * @param name - новое имя для данного Person
     */
    void set_name(const std::string& name);

    /**
     * @brief get_age работает по аналогии с get_name
     */
    int get_age() const;

    /**
     * @brief set_age работает по аналоги с set_name
     */
    void set_age(int age);


private:
    std::string m_name;
    int m_age;
};

#endif // PERSON_HPP
