from pubsub_python.publisher import Publisher
from pubsub_python.subscriber import Subscriber

from time import time

pub_yell = Publisher("yell")
sub_echo = Subscriber("echo")

start_time = time()
pub_yell.send_string("Hello world")
while True:
    if sub_echo.recv():
        end_time = time()
        break

print(f"Received echo after {end_time - start_time} seconds")
