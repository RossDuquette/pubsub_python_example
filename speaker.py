from pubsub_python.publisher import Publisher

from time import sleep

pub_test = Publisher("test")
pub_test2 = Publisher("test2")

for i in range(10):
    pub_test.send_string(f"From speaker test: {i}")
    pub_test2.send_string(f"From speaker test2: {i}")
    sleep(0.1)
