from phue import Bridge
import time

bridge_ip_address = '192.168.1.3'

def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('name')
    return light_names_list

def film_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 7000
        lights[light].saturation = 100

def danger_mode():
    lights = access_lights(bridge_ip_address)
    while True:
        time.sleep(1)
        for light in lights:
            lights[light].on = True
            lights[light].hue = 180
            lights[light].saturation = 100
        time.sleep(1)
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].saturation = 100


danger_mode()