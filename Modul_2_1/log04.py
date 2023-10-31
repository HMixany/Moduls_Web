import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)
handler = RotatingFileHandler('application.log', maxBytes=1024 * 1, backupCount=3, encoding='utf-8')

logger = logging.getLogger('my_logger')
logger.addHandler(handler)

logger.info('Hello World! У попа була собака і він її любив')
logger.error("Вона з'їла кусок м'яса і він її убив")