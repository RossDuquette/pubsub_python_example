from pubsub_python.subscriber import Subscriber

sub_test = Subscriber("test")
sub_empty = Subscriber("empty")
sub_all = Subscriber("*")

while True:
    if sub_test.recv():
        print(f"test recv: {sub_test.get_string()}")
    if sub_empty.recv():
        print(f"empty recv: {sub_empty.get_string()}")
    if sub_all.recv():
        print(f"all ({sub_all.get_recv_topic()}): {sub_all.get_string()}")
