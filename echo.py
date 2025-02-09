from pubsub_python.publisher import Publisher
from pubsub_python.subscriber import Subscriber

sub_yell = Subscriber("yell")
pub_echo = Publisher("echo")

while True:
    if sub_yell.recv():
        pub_echo.send_string(sub_yell.get_string())
