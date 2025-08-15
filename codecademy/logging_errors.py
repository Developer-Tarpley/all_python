import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
        
def division():
  try:
    dividend = float(input("Enter the dividend: "))
    # logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    # logger.info(divisor)
  except ValueError:
    return logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
  if divisor == 0:
    return logger.error("Attempting to divide by 0!")
  else:
    return dividend/divisor
result = division()

if result == None:
  logger.warning("The result value is None!")
