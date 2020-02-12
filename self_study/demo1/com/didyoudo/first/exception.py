import logging

logging.basicConfig(level=logging.INFO)

try:
    a = 10
    b = a / 0
except ZeroDivisionError as zderror:
    logging.error(f"division by zero: {zderror}")
    # print(f"division by zero: {zderror}")
else:
    # try执行完如果没有报错，就会执行else
    logging.info("its ok")
    # print("its ok")
finally:
    logging.info("its always ok")
