from random import randint

from BotConnect import *
from Text import *
from pyqiwip2p import QiwiP2P
async def patternPay(st,mes):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    keyboard.add(InlineKeyboardButton(text = payVariants[0], callback_data= payVariants[0]+str(list(imodji.values())[st])))
    keyboard.add(InlineKeyboardButton(text= payVariants[1], callback_data=payVariants[1]+str(list(imodji.values())[st])))
    keyboard.add(InlineKeyboardButton(text= payVariants[2], callback_data= payVariants[2]+str(list(imodji.values())[st])))
    await mes.message.answer(f"{list(imodji.keys())[st]}\nСтоимость расскалада"
                             f" {list(imodji.values())[st]}\n✅Выберите способ оплаты✅",
                             reply_markup=keyboard)


@dp.message_handler(commands=["start"])
async def start(mes:Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    for i in range(0,len(buttonStartText)-2,2):
        keyboard.add(*[InlineKeyboardButton(text = buttonStartText[i], callback_data= buttonStartText[i]),
                       InlineKeyboardButton(text = buttonStartText[i+1], callback_data= buttonStartText[i+1])])
    else:
        keyboard.add(InlineKeyboardButton(text = buttonStartText[-1], callback_data= buttonStartText[-1]))
    await mes.answer(startText,reply_markup=keyboard)

@dp.callback_query_handler(text=buttonStartText[0])
async def pat(mes:CallbackQuery):
    await patternPay(0,mes)

@dp.callback_query_handler(text=buttonStartText[1])
async def pat(mes:CallbackQuery):
    await patternPay(1,mes)

@dp.callback_query_handler(text=buttonStartText[2])
async def pat(mes:CallbackQuery):
    await patternPay(2,mes)

@dp.callback_query_handler(text=buttonStartText[3])
async def pat(mes:CallbackQuery):
    await patternPay(3,mes)

@dp.callback_query_handler(text=buttonStartText[4])
async def pat(mes:CallbackQuery):
    await patternPay(4,mes)

@dp.callback_query_handler(text=buttonStartText[5])
async def pat(mes:CallbackQuery):
    await patternPay(5,mes)

@dp.callback_query_handler(text=buttonStartText[6])
async def pat(mes:CallbackQuery):
    await patternPay(6,mes)

@dp.callback_query_handler(text_contains=payVariants[0])
async def pay(mes:CallbackQuery):
    sum = mes.data[-3:]

    await mes.message.answer(text=sber[0]+sum+sber[1],
                             reply_markup=InlineKeyboardMarkup().
                             add(InlineKeyboardButton(text="Оплачено",callback_data="Оплачено")))

@dp.callback_query_handler(text_contains=payVariants[2])
async def pay(mes:CallbackQuery):
    sum = mes.data[-3:]
    await mes.message.answer(text=tinkof[0]+sum+tinkof[1],
                             reply_markup=InlineKeyboardMarkup().
                             add(InlineKeyboardButton(text="Оплачено",callback_data="Оплачено")))


@dp.callback_query_handler(text_contains=payVariants[1])
async def pay(mes: CallbackQuery):
    sum = mes.data[-3:]

    bill = qiwi.bill(amount=int(sum), lifetime=30,
                                comment=str(mes.data[:-3]+str(mes.from_user.id)) + "_" + str(randint(1000, 9999)))


    await mes.message.answer(text=qiwiP2Prr[0] + sum + qiwiP2Prr[1]+str(bill.pay_url)+qiwiP2Prr[2],
                             reply_markup=InlineKeyboardMarkup().
                             add(InlineKeyboardButton(text="Оплачено", url = urla)))


executor.start_polling(dp,skip_updates=True)
