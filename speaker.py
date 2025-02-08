from pubsub_python.publisher import Publisher

from time import sleep

pub_test = Publisher("test")
pub_empty = Publisher("empty")

for i in range(10):
    pub_test.send_string(f"From speaker test: {i}")
    pub_empty.send_empty()
    sleep(0.1)
