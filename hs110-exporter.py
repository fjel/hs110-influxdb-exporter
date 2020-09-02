#!/usr/bin/python3
import asyncio
import os
from influxdb import InfluxDBClient
from time import sleep
from kasa import SmartPlug
import datetime

device_ip = os.environ.get('DEVICE_IP')
influx_ip = os.environ.get('INFLUX_IP')
influx_db = os.environ.get('INFLUX_DB')
influx_port = int(os.environ.get('INFLUX_PORT', 8086))
sleep_time = int(os.environ.get('SLEEP_TIME', 30))
 
client = InfluxDBClient(host=influx_ip, port=influx_port)
client.switch_database(influx_db)


async def connect():
    device = SmartPlug(device_ip)
    await device.update()
    if not device.has_emeter:
        raise SmartDeviceException("Device has no emeter")
    return device


async def getAndSend(device):
    power = await device.get_emeter_realtime()
    watt = power['power'] 
    voltage = power['voltage']
    client.write_points([{
        "measurement": "power",
        "tags": {
            "device_ip": device_ip
        },
        "fields": {
            "current_power": watt,
            "current_voltage": voltage
        }
    }])


async def main():
    dev = await connect()
    while dev:
        await getAndSend(dev)
        await asyncio.sleep(sleep_time)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
