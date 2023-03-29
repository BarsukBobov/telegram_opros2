import asyncio
import re

from loguru import logger
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import IDFilter
import markups as btn
from db import Database
import config

db = Database("1.db")

# db.drop_table()
db.create_table()
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

class Fsm(StatesGroup):
    name = State()
    email = State()
    mob_tel = State()
    user_naber = State()


async def cancel(text, id, state):
    if text == "/cancel":
        await bot.send_message(id, "Выход.\nЕсли хотите начать заново - /start")
        await state.finish()
        return False


async def result(data, id):
    user_ie = 0
    user_sn = 0
    user_tf = 0
    user_jp = 0
    try:
        if (data["user_naber_1"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_2"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_3"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_4"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_5"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_6"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_7"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_8"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_9"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_10"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_11"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_12"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_13"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_14"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_15"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_16"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_17"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_18"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_19"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_20"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_21"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_22"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_23"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_24"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_25"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_26"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_27"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_28"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_29"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_30"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_31"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_32"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_33"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_34"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_35"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_36"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_37"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_38"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_39"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_40"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_41"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_42"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_43"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_44"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_45"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_46"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_47"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_48"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_49"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_50"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_51"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_52"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_53"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_54"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_55"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_56"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_57"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_58"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_59"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_60"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_61"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_62"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_63"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_64"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_65"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_66"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_67"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_68"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_69"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_70"] == 'a'):
            user_jp = user_jp + 1
    except:
        pass
    if (user_ie > 5):
        user_i = 'E'
    else:
        user_i = 'I'

    if (user_sn > 10):
        user_n = 'S'
    else:
        user_n = 'N'
    if (user_tf > 10):
        user_f = 'T'
    else:
        user_f = 'F'

    if (user_jp > 10):
        user_p = 'J'
    else:
        user_p = 'P'

    user_nnnn = user_i + user_n + user_f + user_p
    sum=user_ie+user_sn+user_tf+user_jp
    text=f"Буквенный код оценки: {user_nnnn}\nВашей оценкой является балл: {sum}/70\n" \
         f"Баллы расширенные: {user_ie} {user_sn} {user_tf} {user_jp} "
    await bot.send_message(id, text)
    await bot.send_message(id, 'Спасибо! Тестирование закончилось.')
    db.post_result(id, data['name'], data['email'], data['mob_tel'], user_nnnn, user_ie, user_sn, user_tf, user_jp, sum)



####################################СТАРТ########################################
@dp.message_handler(commands=['start'])
async def admin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, btn.text1, parse_mode='html')
    await bot.send_message(message.chat.id, btn.name)
    await Fsm.name.set()


####################################АВТОРИЗАЦИЯ########################################

@dp.message_handler(state=Fsm.name)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(name=message.text)
    await bot.send_message(message.from_user.id, btn.email)
    await Fsm.email.set()


@dp.message_handler(state=Fsm.email)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    if not re.findall(pattern, message.text):
        await bot.send_message(message.from_user.id, "Неверный емэйл, попробуйте снова")
        return
    await state.update_data(email=message.text)
    await bot.send_message(message.from_user.id, btn.mob_tel)
    await Fsm.next()
    await state.update_data(state=1)

@dp.message_handler(state=Fsm.mob_tel)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    try:
        if len(message.text) == 11 and int(message.text):
            await state.update_data(mob_tel=message.text)
            await bot.send_message(message.from_user.id, btn.ready)
            await bot.send_message(message.from_user.id, btn.user_naber_1, reply_markup=btn.choice)
            await Fsm.next()
            await state.update_data(state=1)
            return
    except:
        pass
    await bot.send_message(message.from_user.id, "Неверный номер, попробуйте снова")
    return



####################################КНОПКИ########################################
@dp.message_handler(state=Fsm.user_naber)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return


@dp.callback_query_handler(state=Fsm.user_naber)
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data(state)
    state_user = data["state"]
    if callback.data == "⏭":
        state_user += 1
        if len(data)-state_user==1:
            # txt='Вы ответили не на все вопросы! Для коректного теста необходимо ответить на все'
            # await bot.send_message(callback.from_user.id, txt)
            state_user -= 1

    elif callback.data == "⏮":
        if state_user != 1:
            state_user -= 1
    else:
        dic = {f"user_naber_{state_user}": callback.data}
        await state.update_data(dic)
        state_user += 1
        if state_user == 2:
            data = await state.get_data(state)
            await result(data, callback.from_user.id)
            await state.finish()

            return

    await state.update_data(state=state_user)
    txt = btn.__dict__[f"user_naber_{state_user}"]
    try:
        already_answer = data[f"user_naber_{state_user}"]
        txt += f'''
<i>Ваш ответ:{already_answer}
</i>
'''
    except:
        pass
    await bot.send_message(callback.from_user.id, txt, reply_markup=btn.choice, parse_mode='html')
    
    # data = await state.get_data(state)
    # logger.info(data)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
