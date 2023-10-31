import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(level=logging.INFO)
handler = TimedRotatingFileHandler('daily_log.log', when="midnight", interval=1, backupCount=7, encoding='utf-8')

logger = logging.getLogger('my_logger')
logger.addHandler(handler)

logger.info('Hello World! У попа була собака і він її любив')
logger.error("Вона з'їла кусок м'яса і він її убив")