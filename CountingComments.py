import instagram as inst
from termcolor import colored
import datetime
import time

list_of_accounts = []
list_of_posts = []
keywords = []
length = 1

if input("\nПрочитать список аккаунтов из файла (y or n)?") == "y":
    accounts_file = open(input("\nВведите название файла со списком аккаунтов: "), 'r')
    posts_file = open(input("\nВведите название файла со списком постов: "), 'r')
    for line in accounts_file.readlines():
        list_of_accounts.append(line.rstrip('\n'))
    accounts_file.close()
    for line in posts_file.readlines():
        list_of_posts.append(line.rstrip('\n'))
    posts_file.close()
    if(len(list_of_posts) != len(list_of_accounts)):
        print("Ошибка! Количество постов не соотвествует количиству аккаунтов!")
        exit(0)
    else:
        length = len(list_of_accounts)
else:
    list_of_accounts.append(input("\nВведите имя аккаунта: "))
    list_of_posts.append(input("\nВведите ссылку на пост: "))

keywords_file_name = input("\nВведите название файла с ключевыми словами: ")
keywords_file = open(keywords_file_name, 'r')
for line in keywords_file.readlines():
        keywords.append(line.rstrip('\n'))
keywords_file.close()

for i in range(length):
    max = 0
    counter = 0
    th = 500
    most_popular_word = "<<ТАКОЕ СЛОВО ОТСУТСТВУЕТ>>"

    account_name = list_of_accounts[i]
    post_link = list_of_posts[i]
    results_file_name = "results " + list_of_accounts[i] + ".txt"
    comments_file_name = "comments " + list_of_accounts[i] + ".txt"

    j = 2
    for char in post_link:
        if post_link[-j] != '/':
            j += 1
        else:
            break

    agent = inst.WebAgent()
    code = post_link[-j+1:-1]
    account = inst.Account(account_name)
    media = inst.Media(code)

    comments = []
    com = agent.get_comments(media,  delay = 1)
    comments = comments + com[0]
    pointer = com[1]
    results_file = open(results_file_name, 'a')
    comments_file = open(comments_file_name, 'a')

    print("\nПолучаю комментарии под постом", colored(post_link, "blue", attrs = ['underline']), "пользователя с именем", colored(account_name, "red"))

    while not com[1] is None:
        time.sleep(2)
        com = agent.get_comments(media, pointer = pointer, delay = 1)
        comments = comments + com[0]
        pointer = com[1]
        counter += len(com[0])
        for i in com[0]:
            comments_file.write(i.text + '\n')
        print('\n')
        print("На данный момент получено", counter, "комментариев\r", end ="")
        if counter/th > 1:
            agent.update()
            time.sleep(60)
            th += 500
    
    print("\n\nВсе комментарии получены и записаны в файл\n", colored(comments_file_name, "green"))
    results_file.write("\n\nDate and time of test: " + str(datetime.datetime.now()) + "\n\n")
    results_file.write("Account: " + account_name + ". Post: " + post_link + ".\n\n")

    for k in keywords:
        count = 0
        for i in comments:
            count += i.text.lower().count(k)
        if max < count:
            most_popular_word = k
            max = count
        print("\nКоличество вхождений слова", k.upper(), "=", count)
        results_file.write("\nКоличество вхождений слова " + k.upper() + " = " + str(count))
    print("\nНаиболее часто встречающееся слово из проверенных:", most_popular_word.upper(), "\nКоличество вхождений:", max)
    print("\n\nРезультаты записаны в файл:", colored(results_file, "green"))
    results_file.write("\nНаиболее часто встречающееся слово из проверенных: " + most_popular_word.upper() + ". Количество вхождений: " + str(max) + ".\n" + "-----------------------------------------------------------------------")
    results_file.close()
    comments_file.close()