# Задание

```
Написать класс "Колода карт".
Реализовать 2 метода: перемешать карты и взять N карт из колоды.
Класс Deck инициализируется массивом карт (все возможные комбинации карт
и мастей, каждая карта - это объект класса Card).

Дополнительно: У карт есть текстовое представление (например "Дама пик"
или "6 треф"), нужно реализовать метод, который принимает на вход шаблон
строки и находит карты в колоде по этому шаблону.
Шаблон может содержать две металитеры. '*' соответствует любой
последовательности литер, включая пустую. '%' соответствует в точности
одной литере.
Обязательное ограничение: не использовать готовые средства для работы с
регулярными выражениями и прочие паттерн матчеры.

Код покрыть тестами.
```

# Требования к пакетам
```
Для тестов используется unittest:
pip  install unittest

Для анализа покрытия coverage.
pip  install coverage
```
# Покрытие
![coverage](https://github.com/VladRusakov/Deck/blob/master/coverage.png?raw=true)
