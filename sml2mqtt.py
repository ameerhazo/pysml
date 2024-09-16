from smllib import SmlStreamReader
import serial
import datetime
import time as t
import json as j
import sys
import paho.mqtt.client as client
import ssl

stream = SmlStreamReader()
stream.add(b'BytesFromSerialPort')
# sml_frame = stream.get_frame()
# if sml_frame is None:
#     print('Bytes missing')

# # Add more bytes, once it's a complete frame the SmlStreamReader will
# # return the frame instead of None
# stream.add(b'BytesFromSerialPort')
# sml_frame = stream.get_frame()

# # A quick Shortcut to extract all values without parsing the whole frame
# # In rare cases this might raise an InvalidBufferPos exception, then you have to use sml_frame.parse_frame()
# obis_values = sml_frame.get_obis()

# # return all values but slower
# parsed_msgs = sml_frame.parse_frame()
# for msg in parsed_msgs:
#     # prints a nice overview over the received values
#     print(msg.format_msg())

# # In the parsed message the obis values are typically found like this
# obis_values = parsed_msgs[1].message_body.val_list

# # The obis attribute of the SmlListEntry carries different obis representations as attributes
# list_entry = obis_values[0]
# print(list_entry.obis)            # 0100010800ff
# print(list_entry.obis.obis_code)  # 1-0:1.8.0*255
# print(list_entry.obis.obis_short) # 1.8.0


ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

ser.open()

count = 0
try:
    while True:

        # get data on the serial
        data = ser.read_all()
        # print(data)
        # stream.add(data)
        # sml_frame = stream.get_frame()

        # if sml_frame is None:
        #     print('Not full frame')
        # else:
        #     # obis_values = sml_frame.get_obis()
        #     parsed_msgs = sml_frame.parse_frame()
        #     for msg in parsed_msgs:
        #         print(msg.format_msg())

        if len(data) != 0:
            count = count + 1
            print(len(data))
            print(count)
            print(data)
            stream.add(data)
            sml_frame = stream.get_frame()

            if sml_frame is None:
                print('Not full frame')
            else:
                print('Full frame found')
                # obis_values = sml_frame.get_obis()
                parsed_msgs = sml_frame.parse_frame()
                for msg in parsed_msgs:
                    print(msg.format_msg())

except KeyboardInterrupt:
    ser.close()
    exit
    

