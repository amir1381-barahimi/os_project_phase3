from multiprocessing import  Process, Queue, Value,Array
from time import sleep
from Car import Car


car_in_street=Car(-1)

def producer(queue, id,):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        id.value += 1
        sleep(0.5)
        queue.put(value)


def consumer(queue, street):
    global car_in_street

    print('Consumer: Running', flush=True)
    while True:

        item = queue.get()
        if street.value==0 or street.value == item.id:
            street.value = item.id
            car_in_street=item
            print('car id: ', item.id, 'sleep: ', item.time)
        else:
            sleep(car_in_street.time)
            consumer(queue,street)
        temp = street.value
        sleep(item.time)

        if temp != street.value:
            print('Process conflict!')
        street.value=0

