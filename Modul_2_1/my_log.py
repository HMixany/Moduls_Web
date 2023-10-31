import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",  # formatter — об'єкт, який відповідає за те, яким чином форматуватиметься
    level=logging.DEBUG,  # повідомлення, які там будуть поля та як буде виглядати кожен запис.
    handlers=[  # Ми визначили два обробника (handlers). Один виводить у консоль
        logging.FileHandler(
            "program.log"
        ),  # logging.StreamHandler(), а другий logging.FileHandler("program.log")
        logging.StreamHandler(),  # у файл program.log. handler — об'єкт,який відповідає за обробку кожного
    ],
)  # повідомлення; handler містить форматтер,рівень логування та інструкцію,
logging.warning("An example message.")  # що робити з повідомленням.
logging.warning("Another example message.")
