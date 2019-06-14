import zmq
import json
import random
import time
from uuid import uuid4
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--device_id", help="Device ID that must send the weather data",
                    action="store")
args = parser.parse_args()

device_id = ""
if args.device_id:
    device_id = args.device_id
    print("Device ID is set up for {device_id}!".format(device_id=device_id))

context = zmq.Context()

sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5600")


def send_message(topic, id, timestamp, payload):
    # Message [prefix][message]
    message = "{topic} #{id} at {timestamp} --> {payload}  ".format(topic=topic, id=id, timestamp=timestamp,
                                                                    payload=payload)
    sock.send_string(message)


if device_id != "":
    while True:
        file_read = open("messages.txt", "r")
        message = file_read.readline()
        file_read.close()

        if not message:
            continue

        message_id = str(uuid4())
        now = int(time.time())

        payload = json.dumps({"message_id": message_id, "createdAt": now, "message": message})
        send_message(device_id, message_id, now, payload)

        file_write = open("messages.txt", "w")
        file_write.write("")
        file_write.close()
        message = ""

        time.sleep(1)

