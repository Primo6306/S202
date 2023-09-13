import threading
from pymongo import MongoClient
import pandas as pd
from createThread import sensor_verification
import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


class main:
    client = MongoClient("mongodb://localhost:27017/")
    db = client.bancoiot
    collection = db["sensores"]
    engine = create_engine("mongodb://localhost:27017/")
    threads = []
    for i in range(3):
        thread = threading.Thread(target=sensor_verification, args=(i + 1, db))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    df = pandas.read_sql(
        "SELECT valorSensor FROM sensores ",
        engine,
    )
    df.plot(kind="bar", x="time", y="valorSensor")
    plt.show()
