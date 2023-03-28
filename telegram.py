from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import IDFilter
import markups as btn
from db import Database
import config

db = Database("sigh_in.db")
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Fsm(StatesGroup):
    NIF = State()
    Nombre = State()
    apellido = State()
    Segundo_apellido = State()
    Provincia = State()
    Fecha = State()
    conductor = State()
    email = State()
    phone = State()
    accept = State()
    city = State()
    delete = State()
    Pais = State()


async def cancel(text, id, state):
    if text == "/cancel":
        await bot.send_message(id, "Выход")
        await state.finish()
        return False


####################################АДМИН########################################
@dp.message_handler(IDFilter(chat_id=spisok), commands=['start'])
async def admin(message: types.Message):
    await bot.send_message(message.chat.id, btn.text1, reply_markup=btn.inline(btn.buttons1))


@dp.callback_query_handler()
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    if callback.data == "Добавить":
        await bot.send_message(callback.from_user.id, btn.Pais, reply_markup=btn.inline(btn.paises[0]))
        await Fsm.Pais.set()
        await state.update_data(state1=0)
        return
    if callback.data == "Удалить":
        await bot.send_message(callback.from_user.id, db.get_all_sigh())
        await Fsm.delete.set()
        return


####################################Добавить########################################
@dp.message_handler(state=Fsm.Pais)
async def bot_message(message: types.Message, state: FSMContext):
    arg_dic = {
        "text":message.text,
        "state": state,
        "id": message.from_user.id,
    }
    if await cancel(**arg_dic) is False:
        return


@dp.callback_query_handler(state=Fsm.Pais)
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    if callback.data == "⏭":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] + 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.paises[user_data["state1"]]))
        return
    if callback.data == "⏮":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] - 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.paises[user_data["state1"]]))
        return
    await state.update_data(state1=0)
    await state.update_data(Pais=callback.data)
    await bot.send_message(callback.from_user.id, btn.city, reply_markup=btn.inline(btn.cities[0]))
    await Fsm.city.set()


@dp.message_handler(state=Fsm.city)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return


@dp.callback_query_handler(state=Fsm.city)
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    if callback.data == "⏭":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] + 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.cities[user_data["state1"]]))
        return
    if callback.data == "⏮":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] - 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.cities[user_data["state1"]]))
        return

    await state.update_data(state1=0)
    await state.update_data(city=callback.data)
    await bot.send_message(callback.from_user.id, btn.NIF)
    await Fsm.NIF.set()


def anketa(fsm):
    @dp.message_handler(state=Fsm.__dict__[fsm])
    async def bot_message(message: types.Message, state: FSMContext):
        if await cancel(message.text, message.from_user.id, state) is False:
            return
        r = await state.get_state()
        dic = {r[4:]: message.text}
        await state.update_data(dic)
        await Fsm.next()
        fsm2 = await state.get_state()
        await bot.send_message(message.from_user.id, btn.__dict__[fsm2[4:]])


anketa('NIF')
anketa('Nombre')
anketa('apellido')

# anketa(Fsm.apellido, Fsm.Segundo_apellido, btn.Segundo_apellido)




@dp.message_handler(state=Fsm.Segundo_apellido)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(Segundo_apellido=message.text)
    await bot.send_message(message.from_user.id, btn.Provincia, reply_markup=btn.inline(btn.Provincias[0]))
    await Fsm.Provincia.set()


@dp.message_handler(state=Fsm.Provincia)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return


@dp.callback_query_handler(state=Fsm.Provincia)
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    if callback.data == "⏭":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] + 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.Provincias[user_data["state1"]]))
        return
    if callback.data == "⏮":
        user_data = await state.get_data()
        await state.update_data(state1=user_data["state1"] - 1)
        user_data = await state.get_data()
        await bot.edit_message_text(callback.message.text, callback.from_user.id, callback.message.message_id,
                                    reply_markup=btn.inline(btn.Provincias[user_data["state1"]]))
        return
    await state.update_data(Provincia=callback.data)
    await bot.send_message(callback.from_user.id, btn.Fecha)
    await Fsm.Fecha.set()


@dp.message_handler(state=Fsm.Fecha)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(Fecha=message.text)
    await bot.send_message(message.from_user.id, btn.conductor)
    await Fsm.conductor.set()


@dp.message_handler(state=Fsm.conductor)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(conductor=message.text)
    await bot.send_message(message.from_user.id, btn.email)
    await Fsm.email.set()


@dp.message_handler(state=Fsm.email)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(email=message.text)
    await bot.send_message(message.from_user.id, btn.phone)
    await Fsm.phone.set()


@dp.message_handler(state=Fsm.phone)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    await state.update_data(phone=message.text)
    user_data = await state.get_data()
    del user_data['state1']
    zapis = ''
    for key in user_data:
        zapis = f'{zapis}{key}:{user_data[key]}\n'
    await bot.send_message(message.from_user.id, zapis + "\nПодтвердите запись.", reply_markup=btn.inline(btn.accept))
    await Fsm.accept.set()


@dp.message_handler(state=Fsm.accept)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return


@dp.callback_query_handler(state=Fsm.accept)
async def callbacks(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    user_data = await state.get_data()
    if callback.data == "Да":
        await bot.send_message(callback.from_user.id, "Запись отправлена на мониторнг")
        del user_data['state1']
        db.post_sigh(user_data)
    if callback.data == "Нет":
        await bot.send_message(callback.from_user.id, "Отмена")
    await state.finish()


####################################Удалить########################################
@dp.message_handler(state=Fsm.delete)
async def bot_message(message: types.Message, state: FSMContext):
    if await cancel(message.text, message.from_user.id, state) is False:
        return
    if db.status(int(message.text)) is False:
        await bot.send_message(message.from_user.id, "Такой строки не найдено.\nВыход из панели Админа.")
        await state.finish()
        return
    await bot.send_message(message.from_user.id, "Запись была удалена.\nВыход из панели Админа.")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
