#
# simple IDAPython script to send bytes from address, lenght to JuniEmu input server 
#
# *Important* IS_THUMB_MODE var must be set to 0 or 1 in the JuniEmu.py to indicate starting mode
#

import socket
import struct

buff = b""

code_start = 0x0010200
code_len = 0x100

for ptr in range(code_start, code_start + code_len):
	b = Byte(ptr)
	buff += struct.pack('B',b)

host = socket.gethostname()    
port = 5559  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(buff)
s.close()
