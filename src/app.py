from aiogram.utils import executor
from handlers import dp

if __name__ == "__main__":
    print("Bot loaded successfully")
    executor.start_polling(dispatcher=dp)

