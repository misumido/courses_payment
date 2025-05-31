# 💳 Телеграм-бот для оплаты курсов

Телеграм-бот для автоматизации продажи и оплаты онлайн-курсов с интеграцией платежных систем.

## 📋 Описание

Бот предназначен для автоматизации процесса продажи курсов через Telegram. Поддерживает регистрацию пользователей, выбор курсов, онлайн-оплату и выдачу доступа к материалам после успешной транзакции.

## ✨ Особенности

- Интеграция с платежными системами
- Автоматическая регистрация и управление пользователями
- Каталог курсов с описанием и ценами
- Система уведомлений об оплате
- Административная панель для управления курсами

## 🛠️ Технологии

- **Python 3.12** - основной язык разработки
- **aiogram** - асинхронная библиотека для Telegram Bot API
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite/PostgreSQL** - база данных

## 📦 Установка

```bash
# Клонирование репозитория
git clone https://github.com/misumido/courses_payment.git

# Переход в директорию проекта
cd courses_payment

# Создание виртуального окружения
python -m venv .venv

# Активация виртуального окружения
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

## 🚀 Запуск

```bash
# Запуск бота
python main.py
```

## ⚙️ Конфигурация

Создайте файл `.env` в корне проекта со следующими переменными:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite:///courses.db
PAYMENT_TOKEN=your_payment_provider_token
```

## 📚 Структура проекта

```
courses_payment/
├── database/
│   ├── __init__.py
│   ├── models.py          # Модели SQLAlchemy
│   └── userservice.py     # Сервисы для работы с БД
├── main.py               # Основной файл запуска бота
├── bot.py               # Конфигурация бота
├── buttons.py           # Клавиатуры и кнопки
├── states.py            # Состояния FSM
├── all_txt.py           # Текстовые сообщения
├── requirements.txt     # Зависимости
└── Dockerfile          # Контейнеризация
```

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).

## 📞 Контакты

- **Telegram**: [@medical_ninja](https://t.me/medical_ninja)
- **GitHub**: [@misumido](https://github.com/misumido)

---

⭐ Если проект был полезен, поставьте звездочку!