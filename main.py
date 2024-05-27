from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from aiogram import F
from states import UserStates
from keyboardhelp import keyboards

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("privet! Z '[j-,jn", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    await message.answer("ty v bases")


@dp.message(F.text == "My pari", StateFilter(UserStates.BASE))
async def moi_pari(message: types.Message):
    await message.answer("yours pari:")


@dp.message(F.text == "Create pari", StateFilter(UserStates.BASE))
async def create_pari(message: types.Message):
    await message.answer("-")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


