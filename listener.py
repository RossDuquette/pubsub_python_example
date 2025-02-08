from pubsub_python.subscriber import Subscriber

sub_test = Subscriber("test")
sub_test2 = Subscriber("test2")
sub_all = Subscriber("*")

while True:
    if sub_test.recv():
        print(f"test recv: {sub_test.get_string()}")
    if sub_test2.recv():
        print(f"test2 recv: {sub_test2.get_string()}")
    if sub_all.recv():
        print(f"all ({sub_all.get_recv_topic()}): {sub_all.get_string()}")
