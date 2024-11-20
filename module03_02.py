def send_email(message, recipient, sender = "university.help@gmail.com"):
    rec_dog = recipient.find('@')
    rec_com = recipient.find('.com')
    rec_ru = recipient.find('.ru')
    rec_net = recipient.find('.net')
    send_dog = sender.find('@')
    send_com = sender.find('.com')
    send_ru = sender.find('.ru')
    send_net = sender.find('.net')
    if (rec_dog == -1) or (rec_com == -1 and rec_ru == -1 and rec_net == -1) or (send_dog == -1) or (send_com == -1 and send_ru == -1 and send_net == -1):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Hello, you are very smart','rdthhfthtfhf@gmail.com')
send_email('Прошу отправить мне файл с кодом','rdthhfthtfhf@gmail.com', 'rdthhfthtfhf@gmail.com')
send_email('Отправляю отчет за этот месяц','rdthhfthtfhf@gmail.cz')
send_email('Добрый день! Прошу вас записать меня на конкурс','rdthhfthtfhf@gmail.com','metall.info@gmail.com' )
