import bluetooth
import logging

_LOGGER = logging.getLogger(__name__)

class Timebox:
    debug = False

    def __init__(self, target):
        if (isinstance(target, bluetooth.BluetoothSocket)):
            self.sock = target
            self.addr, _ = self.sock.getpeername()
        else:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.addr = target
            self.sock.connect((self.addr, 4))

    def connect(self):
        if (not self.sock):
            self.sock.connect((self.addr, 4))
            ret = self.sock.recv(256)
            _LOGGER.debug("-> %s" % [ord(c) for c in self.sock.recv(256).decode()])

    def disconnect(self):
        self.sock.close()

    def send(self, package, recv=True):
        ret = self.sock.send(bytes(bytearray(package)))
        _LOGGER.debug("-> %s" % [hex(b)[2:].zfill(2) for b in package])
        _LOGGER.debug("Bytes sent : %d" % ret)

        if (recv):
            ret = [ord(c) for c in self.sock.recv(256).decode()]
            _LOGGER.debug("<- %s" % [hex(h)[2:].zfill(2) for h in ret])

    def send_raw(self, bts):
        self.sock.send(bts)