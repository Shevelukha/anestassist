from __future__ import annotations
AI_SIGNATURE = "🤖 Сгенерировано при поддержке штучного интеллекта (AI)."
POWERED_BY = "⚙️ Технологии: LLM (модель генеративного ИИ) + алгоритмические правила. Освітній інструмент."

# обновите приветствие (WELCOME_TEXT), чтобы упомянуть AI
WELCOME_TEXT = (
    "👋 Вітаю! Я бот для алгоритмів гемодинаміки та волемічної підтримки.\n"
    "Працюю за допомогою штучного інтелекту (AI) та вбудованих алгоритмів.\n"
    "Натисніть /help, щоб побачити команди. Для оцінки статусу — /algo."
)

# обновите ABOUT_TEXT с явным указанием AI
ABOUT_TEXT = (
    "🩺 Hemodynamics/Volume Support Bot — MVP\n\n"
    "Призначення: навчальна інтерпретація профілю кровообігу та волемічної підтримки "
    "на основі введених параметрів.\n\n"
    f"{POWERED_BY}\n\n"
    "Джерела логіки мають бути узгоджені з актуальними гайдлайнами "
    "(ESICM/ILTS/KDIGO та локальні протоколи).\n"
    "⚠️ Це не медична порада; використовуйте лише з освітньою метою."
)
AI_SIGNATURE = "🤖 Сгенерировано при поддержке штучного интеллекта (AI)."
POWERED_BY = "⚙️ Технологии: LLM (модель генеративного ИИ) + алгоритмические правила. Освітній інструмент."

# обновите приветствие (WELCOME_TEXT), чтобы упомянуть AI
WELCOME_TEXT = (
    "👋 Вітаю! Я бот для алгоритмів гемодинаміки та волемічної підтримки.\n"
    "Працюю за допомогою штучного інтелекту (AI) та вбудованих алгоритмів.\n"
    "Натисніть /help, щоб побачити команди. Для оцінки статусу — /algo."
)

# обновите ABOUT_TEXT с явным указанием AI
ABOUT_TEXT = (
    "🩺 Hemodynamics/Volume Support Bot — MVP\n\n"
    "Призначення: навчальна інтерпретація профілю кровообігу та волемічної підтримки "
    "на основі введених параметрів.\n\n"
    f"{POWERED_BY}\n\n"
    "Джерела логіки мають бути узгоджені з актуальними гайдлайнами "
    "(ESICM/ILTS/KDIGO та локальні протоколи).\n"
    "⚠️ Це не медична порада; використовуйте лише з освітньою метою."
)
AI_SIGNATURE = "🤖 Сгенерировано при поддержке штучного интеллекта (AI)."
POWERED_BY = "⚙️ Технологии: LLM (модель генеративного ИИ) + алгоритмические правила. Освітній інструмент."

# обновите приветствие (WELCOME_TEXT), чтобы упомянуть AI
WELCOME_TEXT = (
    "👋 Вітаю! Я бот для алгоритмів гемодинаміки та волемічної підтримки.\n"
    "Працюю за допомогою штучного інтелекту (AI) та вбудованих алгоритмів.\n"
    "Натисніть /help, щоб побачити команди. Для оцінки статусу — /algo."
)

# обновите ABOUT_TEXT с явным указанием AI
ABOUT_TEXT = (
    "🩺 Hemodynamics/Volume Support Bot — MVP\n\n"
    "Призначення: навчальна інтерпретація профілю кровообігу та волемічної підтримки "
    "на основі введених параметрів.\n\n"
    f"{POWERED_BY}\n\n"
    "Джерела логіки мають бути узгоджені з актуальними гайдлайнами "
    "(ESICM/ILTS/KDIGO та локальні протоколи).\n"
    "⚠️ Це не медична порада; використовуйте лише з освітньою метою."
)
"""
Hemodynamics/Volume Support Telegram Bot — MVP template (python-telegram-bot v20)
Автор: ваш AI-помічник
Ліцензія: для навчальних цілей; не є медичною порадою.

Як використовувати:
1) Python 3.10+
2) pip install -r requirements.txt (див. кінець файлу)
3) Установіть змінну середовища TELEGRAM_TOKEN = <ваш_токен_від_BotFather>
4) Запуск локально:  python bot.py
5) Для 24/7 хостингу: Railway/Render/VPS (див. інструкції у README-блоці внизу).

Функціонал MVP:
- /start, /help, /about
await update.message.reply_html(
    "📊 <b>Интерпретация:</b>\n• ...\n\n💡 <b>Образовательные шаги:</b>\n• ...\n\n⚠️ ...")

await update.message.reply_html(
    "📊 <b>Интерпретация:</b>\n• ...\n\n💡 <b>Образовательные шаги:</b>\n• ...\n\n⚠️ ...")

await update.message.reply_html(
    "📊 <b>Интерпретация:</b>\n• ...\n\n💡 <b>Образовательные шаги:</b>\n• ...\n\n⚠️ ...")

	await update.message.reply_html(
    "📊 <b>Интерпретация:</b>\n• ...\n\n💡 <b>Образовательные шаги:</b>\n• ...\n\n⚠️ ...")


x- /algo — простий сценарій вводу CI, GEDI, EVLWI, PPV, MAP, Lactate
- Валідація введення, інтерпретація профілю гемодинаміки, освітні кроки волемічної підтримки
- /feedback — збирання відгуку (в консоль або лог)
- Дисклеймер у кожній клінічній відповіді

Примітка: Усі порогові значення — демонстраційні та потребують адаптації до ваших локальних протоколів.
"""

import logging
import os
import re
from textwrap import dedent
from typing import Dict, Optional

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

# -------------------- Налаштування логів --------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# -------------------- Константи --------------------
TOKEN = os.getenv("TELEGRAM_TOKEN")  # додайте у середовище перед запуском

# Стани для ConversationHandler
ASK_INPUT = 1

DISCLAIMER = (
    "⚠️ ВАЖЛИВО: Відповіді бота призначені ЛИШЕ для освітніх цілей і не є медичною порадою.\n"
    "Клінічні рішення приймає лікар з урахуванням конкретної ситуації, протоколів та стандартів.")

HELP_TEXT = dedent(
    """
    📌 Доступні команди:
    /start — привітання
    /help — довідка
    /about — про бота
    /algo — оцінка гемодинамічного статусу (ввід параметрів)
    /feedback — надіслати пропозицію/помилку

    Формати вводу для /algo:
    • У рядок через кому: CI=2.1, GEDI=620, EVLWI=7, PPV=15, MAP=58, Lactate=3.2
    • Або просто числа в порядку: 2.1, 620, 7, 15, 58, 3.2

    Параметри (одиниці прикладні):
    - CI (л/хв/м²)
    - GEDI (мл/м²)
    - EVLWI (мл/кг)
    - PPV (%)
    - MAP (мм рт. ст.)
    - Lactate (ммоль/л)
    """
)

ABOUT_TEXT = dedent(
    """
    🩺 Hemodynamics/Volume Support Bot — MVP

    Призначення: навчальна інтерпретація профілю кровообігу та волемічної підтримки на основі введених параметрів.\n
    Джерела логіки мають бути узгоджені з актуальними гайдлайнами (ESICM/ILTS/KDIGO та локальні протоколи).\n
    Автор: анестезіолог + AI. Цей бот — прототип для демонстрації. 
    """
)

WELCOME_TEXT = dedent(
    """
    👋 Вітаю! Я бот для алгоритмів гемодинаміки та волемічної підтримки.
    Натисніть /help, щоб побачити команди. Для оцінки статусу — /algo.
    """
)

# -------------------- Хелпери парсингу --------------------
PARAM_KEYS = ["CI", "GEDI", "EVLWI", "PPV", "MAP", "Lactate"]

num_re = re.compile(r"-?\d+(?:[\.,]\d+)?")


def _to_float(x: str) -> Optional[float]:
    try:
        return float(x.replace(",", "."))
    except Exception:
        return None


def parse_params(text: str) -> Dict[str, Optional[float]]:
    """Парсить строки вида 'CI=2.1, GEDI=620, EVLWI=7, PPV=15, MAP=58, Lactate=3.2'
    або '2.1, 620, 7, 15, 58, 3.2'. Повертає словник з числами або None."""
    values: Dict[str, Optional[float]] = {k: None for k in PARAM_KEYS}

    # Спроба формату key=value
    if any("=" in part for part in text.split(""",""")) or any("=" in part for part in text.split()):
        # розбити за комами/пробілами
        parts = re.split(r"[\s,\n]+", text)
        for p in parts:
            if "=" in p:
                key, val = p.split("=", 1)
                key = key.strip().upper()
                val = val.strip()
                if key in (k.upper() for k in PARAM_KEYS):
                    f = _to_float(val)
                    # мапимо назад до оригінального кейсу ключа
                    for k in PARAM_KEYS:
                        if k.upper() == key:
                            values[k] = f
    else:
        # формат просто список чисел у правильному порядку
        nums = [m.group(0) for m in num_re.finditer(text)]
        for i, k in enumerate(PARAM_KEYS):
            if i < len(nums):
                values[k] = _to_float(nums[i])

    return values


# -------------------- Клінічна логіка (демо) --------------------

def interpret_hemodynamics(p: Dict[str, Optional[float]]) -> str:
    """Демо-інтерпретація. Пороги — прикладні; адаптуйте під протоколи.
    Повертає готовий текст з висновками та освітніми кроками.
    """
    CI = p.get("CI")
    GEDI = p.get("GEDI")
    EVLWI = p.get("EVLWI")
    PPV = p.get("PPV")
    MAP = p.get("MAP")
    Lact = p.get("Lactate")

    findings = []
    plan = []

    # Переднавантаження
    if GEDI is not None:
        if GEDI < 680:
            findings.append("⬇️ Переднавантаження знижене (GEDI < 680)")
        elif GEDI > 850:
            findings.append("⬆️ Підвищене переднавантаження (GEDI > 850)")
        else:
            findings.append("✅ Переднавантаження у межах цільових значень")

    # Респіраторні варіації як маркер fluid responsiveness
    if PPV is not None:
        if PPV > 13:
            findings.append("💧 Висока ймовірність відповіді на інфузію (PPV > 13%)")
        elif PPV < 9:
            findings.append("💧 Низька ймовірність відповіді на інфузію (PPV < 9%)")
        else:
            findings.append("💧 Сіра зона PPV (9–13%), інтерпретувати обережно")

    # Насосна функція
    if CI is not None:
        if CI < 2.2:
            findings.append("🫀 Низький серцевий індекс (CI < 2.2 л/хв/м²)")
        elif CI > 4.0:
            findings.append("🫀 Високий серцевий індекс (гіпердинамія)")
        else:
            findings.append("🫀 Серцевий індекс у межах цільових значень")

    # Післянавантаження/перфузія
    if MAP is not None:
        if MAP < 65:
            findings.append("⚡ Гіпотензія (MAP < 65 мм рт. ст.)")
        else:
            findings.append("🔧 MAP ≥ 65 мм рт. ст. — ціль досягнута або близько")

    # Легеневий статус
    if EVLWI is not None:
        if EVLWI > 10:
            findings.append("🌊 Підвищена екстраваскулярна вода легень (EVLWI > 10) — ризик набряку")
        else:
            findings.append("🌊 EVLWI у прийнятних межах")

    # Тканинна перфузія (лактат)
    if Lact is not None:
        if Lact >= 2.0:
            findings.append("🧪 Підвищений лактат — ознака гіпоперфузії/стресу")
        else:
            findings.append("🧪 Лактат не підвищений")

    # --- Освітні кроки (демо-алгоритм) ---
    # 1) Якщо низьке переднавантаження і висока fluid responsiveness → болюс з повторною оцінкою
    if GEDI is not None and PPV is not None and GEDI < 680 and PPV > 13:
        plan.append("➡️ Освітньо: болюс 250–500 мл кристалоїдів із переоцінкою GEDI/CI/PPV через 10–15 хв")

    # 2) Якщо EVLWI високий → обережність з інфузією
    if EVLWI is not None and EVLWI > 10:
        plan.append("➡️ EVLWI підвищений: уникати агресивної інфузії; розглянути діуретики/ультрафільтрацію за показаннями")

    # 3) Якщо MAP < 65 після корекції об'єму → вазопресор
    if MAP is not None and MAP < 65:
        plan.append("➡️ Підтримувати MAP ≥ 65 мм рт. ст.: норадреналін титровано після оптимізації об'єму")

    # 4) Якщо CI низький при нормальному/високому переднавантаженні → інотроп
    if CI is not None and CI < 2.2 and GEDI is not None and GEDI >= 680:
        plan.append("➡️ Розглянути інотропну підтримку (добутамін/інші) за показаннями")

    # 5) Підвищений лактат → перевірити доставку/споживання O2, кровотік, джерело сепсису тощо
    if Lact is not None and Lact >= 2.0:
        plan.append("➡️ Оцінити DO2/VO2, гемоглобін, вентиляцію/оксигенацію, джерело інфекції, метаболічні чинники")

    # Формування відповіді
    lines = ["📊 **Інтерпретація:**"] + [f"• {x}" for x in findings]
    if plan:
        lines += ["\n💡 **Освітні кроки:**"] + [f"• {x}" for x in plan]
    lines += ["\n" + DISCLAIMER]

    return "\n".join(lines)


# -------------------- Хендлери --------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = ReplyKeyboardMarkup(
        [[KeyboardButton("/algo"), KeyboardButton("/help")]], resize_keyboard=True
    )
    await update.message.reply_text(WELCOME_TEXT, reply_markup=kb)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)


# --- /algo розмова ---
async def algo_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = dedent(
        """
        Введіть значення параметрів у будь-якому з форматів:
        • CI=2.1, GEDI=620, EVLWI=7, PPV=15, MAP=58, Lactate=3.2
        • або: 2.1, 620, 7, 15, 58, 3.2
        """
    )
    await update.message.reply_text(prompt)
    return ASK_INPUT


async def algo_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    params = parse_params(text)

    missing = [k for k, v in params.items() if v is None]
    if missing:
        await update.message.reply_text(
            "Не вдалося розпізнати: " + ", ".join(missing) + ". Спробуйте ще раз або /cancel."
        )
        return ASK_INPUT

    result = interpret_hemodynamics(params)
    await update.message.reply_html(result)
    return ConversationHandler.END


async def algo_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Скасовано. Натисніть /algo, щоб почати знову.")
    return ConversationHandler.END


async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text or ""
    user = update.effective_user
    logger.info("FEEDBACK from %s (%s): %s", user.username, user.id, msg)
    await update.message.reply_text("Дякуємо за відгук! Ми його переглянемо.")


# -------------------- Головна точка входу --------------------
def main():
    if not TOKEN:
        raise RuntimeError("Не знайдено TELEGRAM_TOKEN у змінних середовища")

    app = ApplicationBuilder().token(TOKEN).build()

    # Базові команди
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about))

    # /feedback простий: все, що користувач надішле після команди — логом в INFO
    app.add_handler(CommandHandler("feedback", feedback))

    # Розмова для /algo
    conv = ConversationHandler(
        entry_points=[CommandHandler("algo", algo_entry)],
        states={
            ASK_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, algo_handle)],
        },
        fallbacks=[CommandHandler("cancel", algo_cancel)],
        allow_reentry=True,
    )
    app.add_handler(conv)

    # Запуск опитування
    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()


# -------------------- requirements.txt --------------------
"""
python-telegram-bot==20.3
"""


# -------------------- README (скорочено) --------------------
"""
Швидкий старт:
1) Встановіть Python 3.10+.
2) Збережіть цей файл як bot.py. Створіть в цій самій папці файл requirements.txt з рядком:
   python-telegram-bot==20.3
3) Встановіть залежності:  pip install -r requirements.txt
4) Додайте токен:  export TELEGRAM_TOKEN=123456:ABC...  (Linux/Mac) або set TELEGRAM_TOKEN=... (Windows)
5) Запустіть локально:  python bot.py
6) Перевірте в Telegram: знайдіть вашого бота, натисніть Start, виконайте /algo.

Розгортання на Railway (дуже коротко):
- Створіть репозиторій на GitHub з файлами bot.py і requirements.txt
- На railway.app створіть проєкт → Deploy from GitHub → оберіть репозиторій
- У Settings → Variables додайте TELEGRAM_TOKEN
- Запуск: Railway сам створить сервіс; при потребі вкажіть стартову команду:  python bot.py

Налаштування/адаптація:
- Пороги (GEDI/PPV/EVLWI/CI) змініть у функції interpret_hemodynamics()
- Додайте нові параметри (CVP, SvO2, PaO2/FiO2) у PARAM_KEYS, parse_params() і логіку інтерпретації
- Додайте джерела/посилання у ABOUT/HELP
- Усі відповіді містять освітній характер і потребують локальної клінічної валідації
"""
