import random
import threading
import time


def tempGenarator():
    return round(random.uniform(30, 40), 2)


def sensor_verification(sensor_id, db):
    while True:
        temperatura = tempGenarator()
        sensor = {
            "nomeSensor": f"Temp{sensor_id}",
            "valorSensor": temperatura,
            "unidadeMedida": "Cº",
            "sensorAlarmado": False,
        }

        db.sensores.update_one(
            {"nomeSensor": f"Temp{sensor_id}"}, {"$set": sensor}, upsert=True
        )

        if temperatura > 38:
            sensor["sensorAlarmado"] = True
            db.sensores.update_one({"nomeSensor": f"Temp{sensor_id}"}, {"$set": sensor})
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor_id}!")
            break

        time.sleep(40)
