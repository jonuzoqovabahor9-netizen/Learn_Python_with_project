import logging

logging.basicConfig(
    filename = "firstlog.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logging.info("Dastur ishga tushdi.")
logging.warning("Noto'g'ri qiymat kiritildi.")
logging.error("Fayl xatoo")