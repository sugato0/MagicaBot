from pyqiwip2p import QiwiP2P

token = "5713358743:AAEcyG7-QNBHjGU7-pft8ybXnMBDSUvHYlg"

startText = '''
🔮Добро пожаловать на Magic_Taro🔮

Выберите интересующий расклад:'''


buttonStartText  = ["⚒Карьера⚒","💵Финансы💵","💎Отношения💎","⚖Бизнес⚖","🏰Недвижимость🏰","❓Вопрос-Ответ❓","🃏Расклад с доп.вопросами🃏"]

imodji = {"⚒Вы выбрали рассклад \"Карьера\"⚒":500,
          "💵Вы выбрали рассклад \"Финансы\"💵":500,
          "💎Вы выбрали рассклад \"Отношения\"💎":500,
          "⚖Вы выбрали рассклад \"Бизнес\"⚖":500,
          "🏰Вы выбрали рассклад \"Недвижимость\"🏰":500,
          "❓Вы выбрали рассклад \"Вопрос-Ответ\"❓":800,
          "🃏Вы выбрали рассклад \"Расклад с доп.вопросами\"🃏":800}

payVariants = ["Сбербанк💳","Qiwi♻","Тинькофф💳"]

sber= ['''Переведите на банковскую карту ''' , """ рублей удобным для вас способом.
Важно пополнить ровную сумму.
💳 4817760326694514 💳
✅После оплаты нажмите кнопку "ОПЛАЧЕНО"✅"""]

tinkof = ['''Переведите на банковскую карту ''' , """ рублей удобным для вас способом.
Важно пополнить ровную сумму.
💳 2200 7007 3693 2202 💳
✅После оплаты нажмите кнопку "ОПЛАЧЕНО"✅"""]

qiwiP2Prr = ["""Переведите на Qiwi кошелёк ""","""  рублей удобным для вас способом.
Важно пополнить ровную сумму.♻""","""
♻️
✅После оплаты нажмите кнопку "ОПЛАЧЕНО"✅"""]


urla = "https://t.me/ShopTest151Bot"


qiwi = QiwiP2P(auth_key="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InU2MjN5NC0wMCIsInVzZXJfaWQiOiI3OTIzNDk3ODA4MiIsInNlY3JldCI6ImEyYTM1ZjE3ZDhkNTAyZTMxZDEzY2UwYWJhZmI5MTgyODFjZmZjMGJhMGY1NDkyYjY4ZjcyOGI4YTIxZmJhNjcifX0=")