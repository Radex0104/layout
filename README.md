# Анализ удобства раскладок
> В современном мире существует множество различных раскладок. Многие считают Йцукен не самой удобной раскладкой для использования.
> Использование наиболее эргономичной раскладки может существенно ускорить набор текста и снизить количество ошибок.
> Неправильно подобранная раскладка увеличивает нагрузку на руки, что может привести к усталости или профессиональным заболеваниям, таким как синдром запястного канала.




В своей работе мы анализируем 4 раскладки:
* Йцукен
* Диктор
* Зубачев
* Скоропись

Для всех 4 раскладок мы считаем нагрузку на каждый палец, используя файл full_text.txt и количество диграмм, нажатых "удобным" перебором, используя файл digrams.txt, состоящий из двухбуквенных сочетаний.
Более подробно мы рассматриваем раскладку Диктор и сравниваем количество штрафов на пальцы, а также количество диграмм и триграмм, нажатых "удобным" перебором, используя файл 1grams-3.txt


**Раскладка йцукен**

![Раскладка йцукен](https://st.overclockers.ru/legacy/v3/02/29/29/2016/04/10/0u4311987e-6f40b1c2-549b7887.png)

**Раскладка диктор**

![раскладка диктор](https://sun9-54.userapi.com/impg/l8jpSm6nDYG_80EUwio_EbE0ijSewHzH1LkdFw/cSANdY32a7o.jpg?size=742x256&quality=95&sign=adbbb76d316f284d7d3ea0b6f1a755ad&type=album)

**Раскладка зубачев**
<!--- замени картинку -->
![Раскладка Зубачев](https://github.com/user-attachments/assets/e33e18da-eeb6-46eb-a86f-3b8510d52453)


**Раскладка скоропись**

![раскладка скоропись](https://sun9-77.userapi.com/impg/_qiS-UbsM_U3DgoxK-yPLOAfGEM0VMJvGqhG4g/VZrc0FOXDWk.jpg?size=710x245&quality=95&sign=430bc5534cf9e508e03e4f1c184b6ae3&type=album)




## Установка


```sh
git clone https://gitlab.com/Radex0104/diktor.git
```

Запустить лабу 

```sh
python3 main.py
```


## Результаты работы программы

**Лабораторная №1 "Подсчёт нагрузок на пальцы в различных раскладках":**

![лабораторная 1](https://github.com/user-attachments/assets/8d544b43-e5dc-4ff2-b401-6442b11aedda)

**Лабораторная №3 "Подсчёт штрафов на пальцы:**

![лабораторная 3](https://github.com/user-attachments/assets/6ce28e01-019f-4927-85ff-3ca8ed9d25b5)

<!--- на что эту хуйню менять? 
**Лабораторная №4 "Подсчёт диграмм, нажатых удобным перебором в различных раскладках":**

![лабораторная 4](https://sun9-46.userapi.com/impg/_jN6nFcOpgEsQGTDDtzOpJasXd7k6S_SSJfCuA/g9x9l9XHNP8.jpg?size=1000x600&quality=95&sign=c628ccad0e7f65879b586dde29a370e0&type=album)
-->
**Лабораторная №5 "Подсчёт диграмм и триграмм, нажатых удобным перебором:**

![лабораторная 5](https://github.com/user-attachments/assets/214e4117-bd0f-4937-a6db-cb7cc6e2ddfb)


## Вывод
<!--- ПЕРЕДЕЛАТЬ -->
  Так как более подробно мы рассматривали раскладку *Диктор* и сравнивали её с привычным всем *Йцукеном*, вывод хотелось бы сделать, акцентируя внимание имеено на них.  
  Проведенные исследования и результаты программного анализа демонстрируют явное преимущество раскладки *Диктор* перед традиционной *Йцукен*.  
  Оптимальное расположение клавиш, особенно часто встречающихся диграмм и триграмм, достаточно неплохо снижает количество ошибок и повышает скорость набора текста. Это подтверждается данными, полученными в ходе моделирований, где раскладка *Диктор* показала существенно меньшее количество штрафов по сравнению с *Йцукен*. Несмотря на несколько большую нагрузку на средний палец левой руки, характерную для данной раскладки, ее эргономичность и эффективность делают *Диктор* предпочтительным выбором для пользователей, стремящихся повысить свою производительность при работе с текстом. Таким образом, результаты нашего исследования позволяют сделать вывод, что раскладка *Диктор* является более эффективной и удобной для набора текста на русском языке, нежели столь популярная *Йцукен*.    
Если смотреть на количество нажатий в других раскладках, то раскладки *Зубачев* и *Скоропись* имеют примерно одинаковое количество нажатий каждым пальцем. Кроме того, количество диграмм, набранных "удобным" перебором, тоже имеют одинаковые значения.   
  
> "Удобный" перебор: на левой руке - слева направо, на правой руке - справа налево, то есть от мизинца до большого пальца


## Разработчики
Тим-лид - Скуратов Даниил
Помошник кодера - Макейкин Яков
Тестировик, ридми - Бронников Руслан
докфайл, ридми - Веряскин Максим
Граф дизайн - Ширшов Кирилл
