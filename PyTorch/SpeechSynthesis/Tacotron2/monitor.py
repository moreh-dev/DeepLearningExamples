import json
import socket 

reporter = None


class ReportClient:
    _socket = None

    def __init__(self, ip, port):
        if self._socket is None:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self._socket.connect((ip, port))

    def report(self, msg: dict):
        serialized_data = json.dumps(msg).encode()
        try:
            self._socket.sendall(serialized_data)
        except:
            pass


def connect(args):
    if args.enable_integration_test:
        global reporter
        if reporter is None:
            reporter = ReportClient(args.testserver_ip,
                                    args.testserver_port)


def notify(batch_idx, loss, items_per_sec, args):
    # Tell step & loss to the test server.
    if args.enable_integration_test:
        msg = {'step': batch_idx + 1, 'loss': loss, 'items_per_sec' : items_per_sec}
        reporter.report(msg)

