import logging
logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(levelname)s:%(module)s-%(lineno)d-%(message)s",
)
logging.info("这是一条日志")
logging.debug("这是调试信息")