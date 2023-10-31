import logging

"""
handler буде обробляти повідомлення, тільки якщо його рівень дорівнює або вище мінімального рівня, 
вказаного для цього handler. Таким чином, ми можемо, наприклад, писати взагалі всі повідомлення логування в консоль 
і лише повідомлення вище ERROR — у файл. Для цього нам достатньо буде визначити два handler: один для консолі з рівнем 
DEBUG і ще один для логування у файл з рівнем ERROR
"""

# створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

# створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# створюємо форматтер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# додаємо зазначений форматтер до handler console_handler
console_handler.setFormatter(formatter)

# додаємо handler console_handler до логера
logger.addHandler(console_handler)

# Створюємо файловий handler для логера:
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# додаємо файловий handler fh до логера
logger.addHandler(file_handler)

# приклад виконання коду
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")

# ви у консолі побачите всі повідомлення на всіх рівнях, а у файлі app.log — тільки ERROR та CRITICAL
"""
Level	Numeric value
CRITICAL	50
ERROR	    40
WARNING  	30
INFO	    20
DEBUG	    10
NOTSET	     0
"""
