# InstaComments
### Описание
Простая программа, позволяющая найти и обработать ключевые слова в комментариях под конкретным постом конкретного пользователя Инстаграм. Программа была написана по просьбе студентов Социологического факультета МГУ им. М. В. Ломоносова, которые проводили исследование на тему домашнего насилия в России. В результате работы программы, пользователь получает не только готовую статистику по заданным ключевым словам, но и "сырые" данные, пригодные для дальнейшего исследования.

Для загрузки комментариев мной была использована библиотека instagram, найденная у пользователя GitHub @OlegYurchik. 
### Описание работы программы
Программа очень проста в использовании. Для корректной работы требуется имя пользователя Инстаграм и ссылка на пост, комментарии под которым требуется обработать. Имена пользователей и ссылки на посты можно вводить как с клавиатуры, так и считывать списком из соответствующих файлов (см. "**accounts.txt**" и "**posts.txt**"). Одному имени пользователя в файле "имена_пользователей.txt" должна соответствовать ровно одна ссылка на пост в файле "ссылки_на_посты.txt". Ключевые слова так же должны быть записаны в отдельный файл (см. "**keywords.txt**"). Результат работы программы записывается в файл "results <имя_пользователя>.txt", считанные комментарии в файл "comments <имя_пользователя>.txt". Пример работы программы можно увидеть в файлах "**comments milalevchuk.txt**" и "**results milalevchuk.txt**".

### Description
A simple program that allows to find and procces the keywords in comments under a certain post of a certain Instagram user. The program was written at the request of students of the Sociology Faculty of Lomonosov Moscow State University, who conducted a study on domestic violence in Russia. As a result of the program, the user receives not only ready-made statistics for the specified keywords, but also "raw" data suitable for further research.

I used the instagram library found on GitHub user @OlegYurchik to upload comments.
### User guide
The program is very easy to use. To work correctly, you need the Instagram user name and a link to the post that you want to process comments under. User names and links to posts can be entered using the keyboard or read from the corresponding files (see "**accounts.txt**" and "**posts.txt**"). One user name in the "user_names.txt" must match exactly one link to a post in the "links_to_posts.txt". Keywords must also be written to a separate file (see "**keywords.txt**"). The result of the program is written to the file "results <user_name>.txt", read comments to the file "comments <user_name>.txt". An example of how the program works can be seen in the "**comments milalevchuk.txt**" and "**results milalevchuk.txt**".
