import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/lab6/partc/button'

button = qwiic_button.QwiicButton()
button_presses_for_session = 0 

while True:
    if button.is_button_pressed() == True:
        button_presses_for_session += 1
        val = "the button has been pressed " + str(button_presses_for_session) + " times!"
        client.publish(topic, val)
    time.sleep(0.25)
