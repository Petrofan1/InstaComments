import instagram as inst
from termcolor import colored
import datetime
import time
list_of_accounts = ['evdklar', 'senoritasaeva' ,'milalevchuk' , 'nika_viper', 'misskogut', 'masha_davay','alexandramitroshina']
list_of_posts = ['https://www.instagram.com/p/B0K7xdIBiJf/',
'https://www.instagram.com/p/B0tD0n_gAgu/',  'https://www.instagram.com/p/B1f2nitCNaI/', 'https://www.instagram.com/p/B1wDPxhhzSl/',
'https://www.instagram.com/p/B0G2G2NFWSh/', 'https://www.instagram.com/p/B0K3mt8iF9A/', 'https://www.instagram.com/p/B0Gj4m3isoR/']
for i in range(len(list_of_accounts)):
    agent = inst.WebAgent()
    settings = {
       "proxies": {
           "http": "167.114.64.174",
           "htpps": "167.114.64.174",
       }
    }
    agent.update(settings = settings)
    print("\n\n")
    account_name = list_of_accounts[i]
    post_link = list_of_posts[i]
    results_file = "results " + list_of_accounts[i] + ".txt"
    key_words = []
    key_words_file = "keyWords.txt"
    my_file = open(key_words_file, "r")
    for line in my_file.readlines():
        keyWords.append(line.rstrip('\n'))
    my_file.close()
    count = 0
    j = 2
    while 1:
        if post_link[-j] != '/':
            j += 1
            continue
        else:
            break
    code = post_link[-j+1:-1]
    account = inst.Account(account_name)
    media = inst.Media(code)
    comments = []
    com = agent.get_comments(media,  delay = 1)
    comments = comments + com[0]
    pointer = com[1]
    count = 0
    max = 0
    counter = 0
    th = 500
    my_file = open(results_file, "a")
    print("\nПолучаю комментарии...\n")
    most_popular_word = "<<ТАКОЕ СЛОВО ОТСУТСТВУЕТ>>"
    while not com[1] is None:
        time.sleep(2)
        com = agent.get_comments(media, pointer = pointer, delay = 1)
        comments = comments + com[0]
        pointer = com[1]
        counter += len(com[0])
        print("На данный момент получено", counter, "комментариев\r", end ="")
        if counter/th > 1:
            agent.update()
            time.sleep(60)
            th += 500
    print("\n\nКомментарии получены!\n")
    my_file.write("\n\nDate and time of test: " + str(datetime.datetime.now()) + "\n\n")
    my_file.write("Account: " + account_name + ". Post: " + post_link + ".\n\n")
    for k in key_words:
        count = 0
        for i in comments:
            count += i.text.lower().count(k)
        if max < count:
            most_popular_word = k
            max = count
        print("\nКоличество вхождений слова", k.upper(), "=", count)
        my_file.write("\nКоличество вхождений слова " + k.upper() + " = " + str(count))
    print("\nНаиболее часто встречающееся слово из проверенных:", most_popular_word.upper(), "\nКоличество вхождений:", max)
    print("\n\nРезультаты записаны в файл:", results_file)
    my_file.write("\nНаиболее часто встречающееся слово из проверенных: " + most_popular_word.upper() + ". Количество вхождений: " + str(max) + ".\n" + "-----------------------------------------------------------------------")
    my_file.close()