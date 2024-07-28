def send_email(message, recipient, sender="university.help@gmail.com"):
    if (('@' in recipient and '@' in sender) and
            (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and
            (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
        if sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
            print(message)
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
            print(message)
    else:
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.')
    return


#  тестовые сообщения:

send_email('это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
