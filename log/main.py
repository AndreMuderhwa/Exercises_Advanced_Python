import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%d/%m/%Y %H:%M:%S'
# )

# import helper

try:
    a=[1,2,3]
    a[4]
except Exception as e:
    logging.error(e, exc_info=True)