import smtplib
from email.mime.text import MIMEText

from django.test import TestCase

# Create your tests here.
"""
1) Пользователь оставляет заявку на ремонт автомобиля.
Заполняет ее.
2) Далее заявка улетает к менеджеру.
Он ее дополняет, вносит какие-то коррективы и отправляет заявку мастеру.
3) Мастер принимает заявку, выбирает детали для ремонта и назначает рабочих для выполнения работ.
4) Рабочий принимает заявку на выполнение, по окончанию работ закрывает заявку и отправляет мастеру.
5) Мастер проверяет заявку и может вернуть ее на доработку или отправить уже менеджеру со статусом выполнено.
6) Менеджер принимает заявку которая выполнена, и может позвонить клиенту что заявка выполнена.
(или можно сделать чтобы он нажимал на кнопку уведомить клиента о завершении работ и ему на
 почту прилетало уведомление )
 
У пользователей будут статусы
У заявки тоже будут статусы, которые будут видны клиенту
Хочу сделать "Склад запчастей", "Расчет зарплаты"
"""


"""
'test@mail.ru' - '12345' - superuser

'user1@mail.ru' - '069miroslav069' - пользователь
--------------------------------------------------
'user2@mail.ru' - '069miroslav069' - пользователь
--------------------------------------------------
'miroslav_shagun@mail.ru' - '069miroslav069' - пользователь
--------------------------------------------------
'technician@mail.ru' - '069miroslav069' - менеджер
--------------------------------------------------
'master@mail.ru' - '069miroslav069' - мастер
--------------------------------------------------
'worker1@mail.ru' - '069miroslav069' - рабочий
--------------------------------------------------
'worker2@mail.ru' - '069miroslav069' - рабочий
--------------------------------------------------
"""
"""
testemailz744@gmail.com
testemail2023
kklpvgtrsdxprlxy
"""


"""
Закрываем текущие сессии
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'database_name' AND pid <> pg_backend_pid();

Удаляем базу
DROP DATABASE database_name;
"""


# def send_email(message):
#     sender = 'testemailz744@gmail.com'
#     password = 'kklpvgtrsdxprlxy'
#
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     try:
#         server.login(sender, password)
#         msg = MIMEText(message)
#         msg["Subject"] = "Ваша заявка на ремонт автомобиля выполнена!"
#         server.sendmail(sender, sender, msg.as_string())
#
#         return "Сообщение было отправлено успешно!"
#     except Exception as _ex:
#         return f"{_ex}\nПроверьте свой логин или пароль, пожалуйста!"
#
#
# def main():
#     message = 'Pype your message'
#     print(send_email(message=message))
#
#
# if __name__ == "__main__":
#     main()