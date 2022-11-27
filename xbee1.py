xbee = XBeeDevice("COM1", 9600)
xbee.open()

# Instantiate a remote XBee node.
remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))

# Send data using the remote object.
xbee.send_data(remote, "Hello XBee!")

#nl