import requests
import configuration
import data

#Запрос на создание заказа.
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order_body)

# Сохранение номера трека заказа.
def get_new_track():
    res = post_new_order(data.order_body)
    track = res.json()["track"]
    return track



# Запрос на получения заказа по треку.

def get_order_body(track):
    params_with_track= {"t": track} 
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER, 
                        params=params_with_track) 








