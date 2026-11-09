from typing import Final, Literal, Optional, overload
from typing_extensions import Buffer, Sequence
import io

SOL_HCI: Final[int]
HCI_DATA_DIR: Final[int]
HCI_TIME_STAMP: Final[int]
HCI_FILTER: Final[int]
HCI_MAX_EVENT_SIZE: Final[int]
HCI_EVENT_HDR_SIZE: Final[int]

HCI: Final[int]
L2CAP: Final[int]
RFCOMM: Final[int]
SCO: Final[int]

# HCI constants

# HCI OGF values
OGF_LINK_CTL: Final[int]
OGF_LINK_POLICY: Final[int]
OGF_HOST_CTL: Final[int]
OGF_INFO_PARAM: Final[int]
OGF_STATUS_PARAM: Final[int]
OGF_TESTING_CMD: Final[int]
OGF_VENDOR_CMD: Final[int]

# HCI OCF values
OCF_INQUIRY: Final[int]
OCF_INQUIRY_CANCEL: Final[int]
OCF_PERIODIC_INQUIRY: Final[int]
OCF_EXIT_PERIODIC_INQUIRY: Final[int]
OCF_CREATE_CONN: Final[int]
CREATE_CONN_CP_SIZE: Final[int]
ACL_PTYPE_MASK: Final[int]
OCF_DISCONNECT: Final[int]
OCF_ADD_SCO: Final[int]
OCF_ACCEPT_CONN_REQ: Final[int]
OCF_REJECT_CONN_REQ: Final[int]
OCF_LINK_KEY_REPLY: Final[int]
OCF_LINK_KEY_NEG_REPLY: Final[int]
OCF_PIN_CODE_REPLY: Final[int]
OCF_PIN_CODE_NEG_REPLY: Final[int]
OCF_SET_CONN_PTYPE: Final[int]
OCF_AUTH_REQUESTED: Final[int]
OCF_SET_CONN_ENCRYPT: Final[int]
OCF_REMOTE_NAME_FREQ: Final[int]
OCF_READ_REMOTE_FEATURES: Final[int]
OCF_READ_REMOTE_EXT_FEATURES: Final[int]
OCF_READ_REMOTE_VERISON: Final[int]
OCF_READ_CLOCK_OFFSET: Final[int]
OCF_READ_CLOCK: Final[int]
OCF_IO_CAPABILITY_REPLY: Final[int]
OCF_USER_CONFIRM_REPLY: Final[int]
OCF_HOLD_MODE: Final[int]
OCF_SNIFF_MODE: Final[int]
OCF_EXIT_SNIFF_MODE: Final[int]
OCF_PARK_MODE: Final[int]
OCF_EXIT_PARK_MODE: Final[int]
OCF_QOS_SETUP: Final[int]
OCF_ROLE_DISCOVERY: Final[int]
OCF_SWITCH_ROLE: Final[int]
OCF_READ_LINK_POLICY: Final[int]
OCF_WRITE_LINK_POLICY: Final[int]
OCF_RESET: Final[int]
OCF_SET_EVENT_MASK: Final[int]
OCF_SET_EVENT_FLT: Final[int]
OCF_CHANGE_LOCAL_NAME: Final[int]
OCF_READ_LOCAL_NAME: Final[int]
OCF_WRITE_CA_TIMEOUT: Final[int]
OCF_WRITE_PG_TIMEOUT: Final[int]
OCF_READ_PAGE_TIMEOUT: Final[int]
OCF_WRITE_PAGE_TIMEOUT: Final[int]
OCF_READ_SCAN_ENABLE: Final[int]
OCF_WRITE_SCAN_ENABLE: Final[int]
OCF_READ_PAGE_ACTIVITY: Final[int]
OCF_WRITE_PAGE_ACTIVITY: Final[int]
OCF_READ_INQ_ACTIVITY: Final[int]
OCF_WRITE_INQ_ACTIVITY: Final[int]
OCF_READ_AUTH_ENABLE: Final[int]
OCF_WRITE_AUTH_ENABLE: Final[int]
OCF_READ_ENCRYPT_MODE: Final[int]
OCF_WRITE_ENCRYPT_MODE: Final[int]
OCF_READ_CLASS_OF_DEV: Final[int]
OCF_WRITE_CLASS_OF_DEV: Final[int]
OCF_READ_VOICE_SETTING: Final[int]
OCF_WRITE_VOICE_SETTING: Final[int]
OCF_READ_TRANSMIT_POWER_LEVEL: Final[int]
OCF_HOST_BUFFER_SIZE: Final[int]
OCF_READ_LINK_SUPERVISION_TIMEOUT: Final[int]
OCF_WRITE_LINK_SUPERVISION_TIMEOUT: Final[int]
OCF_READ_CURRENT_IAC_LAP: Final[int]
OCF_WRITE_CURRENT_IAC_LAP: Final[int]
OCF_READ_INQUIRY_MODE: Final[int]
OCF_WRITE_INQUIRY_MODE: Final[int]
OCF_READ_AFH_MODE: Final[int]
OCF_WRITE_AFH_MODE: Final[int]
OCF_WRITE_EXT_INQUIRY_RESPONSE: Final[int]
OCF_WRITE_SIMPLE_PAIRING_MODE: Final[int]
OCF_READ_LOCAL_VERSION: Final[int]
OCF_READ_LOCAL_FEATURES: Final[int]
OCF_READ_BUFFER_SIZE: Final[int]
OCF_READ_BD_ADDR: Final[int]
OCF_READ_FAILED_CONTACT_COUNTER: Final[int]
OCF_RESET_FAILED_CONTACT_COUNTER: Final[int]
OCF_GET_LINK_QUALITY: Final[int]
OCF_READ_RSSI: Final[int]
OCF_READ_AFH_MAP: Final[int]

# HCI events
EVT_INQUIRY_COMPLETE: Final[int]
EVT_INQUIRY_RESULT: Final[int]
EVT_CONN_COMPLETE: Final[int]
EVT_CONN_COMPLETE_SIZE: Final[int]
EVT_CONN_REQUEST: Final[int]
EVT_CONN_REQUEST_SIZE: Final[int]
EVT_DISCONN_COMPLETE: Final[int]
EVT_DISCONN_COMPLETE_SIZE: Final[int]
EVT_AUTH_COMPLETE: Final[int]
EVT_AUTH_COMPLETE_SIZE: Final[int]
EVT_REMOTE_NAME_REQ_COMPLETE: Final[int]
EVT_REMOTE_NAME_REQ_COMPLETE_SIZE: Final[int]
EVT_ENCRYPT_CHANGE: Final[int]
EVT_ENCRYPT_CHANGE_SIZE: Final[int]
EVT_READ_REMOTE_FEATURES_COMPLETE: Final[int]
EVT_READ_REMOTE_FEATURES_COMPLETE_SIZE: Final[int]
EVT_READ_REMOTE_VERSION_COMPLETE: Final[int]
EVT_READ_REMOTE_VERSION_COMPLETE_SIZE: Final[int]
EVT_QOS_SETUP_COMPLETE: Final[int]
EVT_QOS_SETUP_COMPLETE_SIZE: Final[int]
EVT_CMD_COMPLETE: Final[int]
EVT_CMD_COMPLETE_SIZE: Final[int]
EVT_CMD_STATUS: Final[int]
EVT_CMD_STATUS_SIZE: Final[int]
EVT_ROLE_CHANGE: Final[int]
EVT_ROLE_CHANGE_SIZE: Final[int]
EVT_NUM_COMP_PKTS: Final[int]
EVT_NUM_COMP_PKTS_SIZE: Final[int]
EVT_MODE_CHANGE: Final[int]
EVT_MOE_CHANGE_SIZE: Final[int]
EVT_PIN_CODE_REQ: Final[int]
EVT_PIN_CODE_REQ_SIZE: Final[int]
EVT_LINK_KEY_REQ: Final[int]
EVT_LINK_KEY_REQ_SIZE: Final[int]
EVT_LINK_KEY_NOTIFY: Final[int]
EVT_LINK_KEY_NOTIFY_SIZE: Final[int]
EVT_MAX_SLOTS_CHANGE: Final[int]
EVT_READ_CLOCK_OFFSET_COMPLETE: Final[int]
EVT_READ_CLOCK_OFFSET_COMPLETE_SIZE: Final[int]
EVT_CONN_PTYPE_CHANGED: Final[int]
EVT_CONN_PTYPE_CHANGED_SIZE: Final[int]
EVT_QOS_VIOLATION: Final[int]
EVT_QOS_VIOLATION_SIZE: Final[int]
EVT_PSCAN_REP_MODE_CHANGE: Final[int]
EVT_FLOW_SPEC_COMPLETE: Final[int]
EVT_FLOW_SPEC_MODIFY_COMPLETE: Final[int]
EVT_INQUIRY_RESULT_WITH_RSSI: Final[int]
EVT_REMOTE_REMOTE_EXT_FEATURES_COMPLETE: Final[int]
EVT_EXTENDED_INQUIRY_RESULT: Final[int]
HAVE_EVT_EXTENDED_INQUIRY_RESULT: Final[int]
EVT_DISCONNECT_LOGICAL_LINK_COMPLETE: Final[int]
EVT_IO_CAPABILITY_REQUEST: Final[int]
EVT_IO_CAPABILITY_RESPONSE: Final[int]
EVT_USER_CONFIRM_REQUEST: Final[int]
EVT_SIMPLE_PAIRING_COMPLETE: Final[int]
EVT_TESTING: Final[int]
EVT_VENDOR: Final[int]
EVT_STACK_INTERNAL: Final[int]
EVT_STACK_INTERNAL_SIZE: Final[int]
EVT_SI_DEVICE: Final[int]
EVT_SI_DEVICE_SIZE: Final[int]
EVT_SI_SECURITY: Final[int]
EVT_NUMBER_COMPLETED_BLOCKS: Final[int]

# HCI packet types
HCI_COMMAND_PKT: Final[int]
HCI_ACLDATA_PKT: Final[int]
HCI_SCODATA_PKT: Final[int]
HCI_EVENT_PKT: Final[int]
HCI_UNKNOWN_PKT: Final[int]

# socket options
SO_DEBUG: Final[int]
SO_ACCEPTCONN: Final[int]
SO_REUSEADDR: Final[int]
SO_KEEPALIVE: Final[int]
SO_DONTROUTE: Final[int]
SO_BROADCAST: Final[int]
SO_USELOOPBACK: Final[int]
SO_LINGER: Final[int]
SO_OOBINLINE: Final[int]
SO_REUSEPORT: Final[int]
SO_SNDBUF: Final[int]
SO_RCVBUF: Final[int]
SO_SNDLOWAT: Final[int]
SO_RCVLOWAT: Final[int]
SO_SNDTIMEO: Final[int]
SO_RCVTIMEO: Final[int]
SO_ERROR: Final[int]
SO_TYPE: Final[int]
# max number of connections for "listen"
SOMAXCONN: Final[int]

# Flags for send, recv
MSG_OOB: Final[int]
MSG_PEEK: Final[int]
MSG_DONTROUTE: Final[int]
MSG_DONTWAIT: Final[int]
MSG_EOR: Final[int]
MSG_TRUNC: Final[int]
MSG_CTRUNC: Final[int]
MSG_WAITALL: Final[int]
MSG_BTAG: Final[int]
MSG_ETAG: Final[int]

# Size of inquiry info
INQUIRY_INFO_WITH_RSSI_SIZE: Final[int]
EXTENDED_INQUIRY_INFO_SIZE: Final[int]

# Protocol level and nubers, usable for [gs]etsockopt
SOL_SOCKET: Final[int]
SOL_L2CAP: Final[int]
SOL_RFCOMM: Final[int]
SOL_SCO: Final[int]
SCO_OPTIONS: Final[int]
L2CAP_OPTIONS: Final[int]

# special channels to bind()
HCI_CHANNEL_CONTROL: Final[int]
HCI_CHANNEL_USER: Final[int]
HCI_DEV_NONE: Final[int]

# ioctl
HCIDEVUP: Final[int]
HCIDEVDOWN: Final[int]
HCIDEVRESET: Final[int]
HCIDEVRESTAT: Final[int]
HCIGETDEVLIST: Final[int]
HCIGETDEVINFO: Final[int]
HCIGETCONNLIST: Final[int]
HCIGETCONNINFO: Final[int]
HCISETRAW: Final[int]
HCISETSCAN: Final[int]
HCISETAUTH: Final[int]
HCISETENCRYPT: Final[int]
HCISETPTYPE: Final[int]
HCISETLINKPOL: Final[int]
HCISETLINKMODE: Final[int]
HCISETACLMTU: Final[int]
HCISETSCOMTU: Final[int]
HCIINQUIRY: Final[int]

ACL_LINK: Final[int]
SCO_LINK: Final[int]

# RFCOMM
RFCOMM_LM: Final[int]
RFCOMM_LM_MASTER: Final[int]
RFCOMM_LM_AUTH: Final[int]
RFCOMM_LM_ENCRYPT: Final[int]
RFCOMM_LM_TRUSTED: Final[int]
RFCOMM_LM_RELIABLE: Final[int]
RFCOMM_LM_SECURE: Final[int]

# L2CAP
L2CAP_LM: Final[int]
L2CAP_LM_MASTER: Final[int]
L2CAP_LM_AUTH: Final[int]
L2CAP_LM_ENCRYPT: Final[int]
L2CAP_LM_TRUSTED: Final[int]
L2CAP_LM_RELIABLE: Final[int]
L2CAP_LM_SECURE: Final[int]

L2CAP_COMMAND_REJ: Final[int]
L2CAP_CONN_REQ: Final[int]
L2CAP_CONN_RSP: Final[int]
L2CAP_CONF_REQ: Final[int]
L2CAP_CONF_RSP: Final[int]
L2CAP_DISCONN_REQ: Final[int]
L2CAP_DISCONN_RSP: Final[int]
L2CAP_ECHO_REQ: Final[int]
L2CAP_ECHO_RSP: Final[int]
L2CAP_INFO_REQ: Final[int]
L2CAP_INFO_RSP: Final[int]

L2CAP_MODE_BASIC: Final[int]
L2CAP_MODE_RETRANS: Final[int]
L2CAP_MODE_FLOWCTL: Final[int]
L2CAP_MODE_ERTM: Final[int]
L2CAP_MODE_STREAMING: Final[int]

BT_SECURITY: Final[int]
BT_SECURITY_SDP: Final[int]
BT_SECURITY_LOW: Final[int]
BT_SECURITY_MEDIUM: Final[int]
BT_SECURITY_HIGH: Final[int]

BT_DEFER_SETUP: Final[int]

SOL_BLUETOOTH: Final[int]

class error(OSError): ...

type sockaddrarg = tuple[int] | tuple[int, int] | tuple[str, int] | tuple[str];

type makesockaddr_t = int | tuple[str, int] | str;

class btsocket:
    """
    A BlutoothSocket object represents one endpoint of a bluetooth connection.

    Args:
        proto: The Bluetooth protocol to use. Must be oen of HCI, L2CAP,
            RFCOMM (default), or SCO. to  SCO sockets have not been tested.
        
    Note:
        Methods do not accept keyword arguments.
    """

    def __init__(self, proto: Optional[int] = None) -> None:
        ...

    def __repr__(self) -> str:
        ...

    # tp_getset

    @property
    def timeout(self) -> Optional[float]:
        """the socket timeout"""

    # tp_members

    @property
    def family(self) -> int:
        """the socket family"""

    @property
    def type(self) -> int:
        """the socket type"""

    @property
    def proto(self) -> int:
        """the socket protocol"""

    # tp_methods

    def accept(self) -> tuple[btsocket, makesockaddr_t]:
        """
        Wait for an incoming connection.
        
        Returns:
            A tuple containing:
                socket: New socket representing the connection.
                address:
                    - L2CAP: A `(host, psm)` tuple
                    - RFCOMM: A `(host, channel)` tuple
                    - SCO: A `host` string
        """
        ...

    def bind(self, addr: sockaddrarg, /) -> None:
        """
        Bind the socket to a local address. `address` must always be a tuple.

        Args:
            address: The address to bind to.
        """
        ...

    def close(self) -> None:
        """Close the socket. It cannot be used after this call."""
        ...

    def connect(self, address: sockaddrarg, /) -> None:
        """
        Connect the socket to a remote address.

        Args:
            address: For L2CAP, `(host, psm)`; for RFCOMM, `(host, channel)`;
                for SCO, the address is just the host.
        """
        ...

    def connect_ex(self, address: sockaddrarg, /) -> int:
        """
        This is like connect(address), but returns an error code (the errno value)
        instead of raising an exception when an error occurs.

        Returns:
            The error code (errno value).
        """
        ...

    def dup(self) -> btsocket:
        """
        Return a new socket object connected to the same system resource.
        """
        ...

    def fileno(self) -> int:
        """
        Return the integer file descriptor of the socket.
        """
        ...

    def getpeername(self) -> makesockaddr_t:
        """
        Return the address of the remote endpoint. For HCI sockets, the address is a
        device number (0, 1, 2, etc). For L2CAP sockets, the address is a
        (host, psm) tuple. For RFCOMM sockets, the address is a (host, channel) tuple.
        For SCO sockets, the address is just the host.
        """
        ...

    def getsockid(self) -> int:
        """Gets socket id."""
        ...

    def getsockname(self) -> makesockaddr_t:
        """Return the address of the local endpoint."""
        ...

    @overload
    def getsockopt(self, level: int, option: int, buffersize: Literal[0] = 0, /) -> int:
        """
        Get a socket option. See the Unix manual page for level and option.
        If a nonzero buffersize argument is given, the return value is a
        string of that length; otherwise it is an integer.

        Args:
            level: The protocol level of the option.
            option: The option to get.
            buffersize: Maximum buffer size. If zero or omitted, return
                the option as an integer. Otherwise, return its
                value as a string.

        Returns:
            The socket option value as an integer or string.
        """
        ...

    @overload
    def getsockopt(self, level: int, option: int, buffersize: int, /) -> str | int: ...

    def listen(self, backlog: int, /) -> None:
        """
        Enable a server to accept connections.

        Args:
            backlog: The number of unaccepted connection that the system
                will allow before refusing new connections. Must be at
                least 1.
        """
        ...

    def makefile(self, mode: str = "r", buffersize: int = -1, /) -> io.IOBase:
        """
        Return a regular file object corresponding to the socket.

        Args:
            mode: File access mode. Defaults to "r".
            buffersize: Buffer size. Defaults to -1.

        Returns:
            A file object associated with the socket.
        """
        ...

    def recv(self, buffersize: int, flags: int = 0, /) -> bytes:
        """
        Receive up to `buffersize` bytes from the socket. When no data
        is available, block until at least one byte is available or
        the remote end is closed. When the remote end is closed and
        all data is read, return the empty string.

        Args:
            buffersize: Maximum buffer size to read.
            flags: Optional flags (defaults to 0). See the Unix manual.

        Returns:
            A buffer up to `buffersize` bytes.
        """
        ...

    def recvfrom(self, buffersize: int, flags: int = 0, /) -> tuple[bytes, int | tuple[str, int] | str]:
        """
        Like `recv(buffersize, flags)` but also returns the sender's address info.
        
        Args:
            buffersize: Maximum buffer size to read.
            flags: Optional flags (defaults to 0). See the Unix manual.

        Returns:
            A tuple containing:
                data: A buffer up to `buffersize` bytes.
                address info: The sender's address.
        """
        ...

    def send(self, data: str | Buffer, flags: int = 0, /) -> int:
        """
        Sends a data string to the socket.

        Args:
            data: The data to send.
            flags: Optional flags (defaults to 0). See the Unix manual.

        Returns:
            The number of bytes sent; this may be less than `len(data)`
            if the network is busy.
        """
        ...

    def sendall(self, data: str | Buffer, flags: int = 0, /) -> None:
        """
        Sends a data string to the socket. This calls `send()`
        repeatedly until all data is sent. If an error occurs,
        it's impossible to tell how much data has been sent.

        Args:
            data: The data to send.
            flags: Optional flags (defaults to 0). See the Unix manual.
        """
        ...

    @overload
    def sendto(self, data: str | Buffer, addr: int | tuple[str, int] | str, /) -> int:
        """
        Like `send(data, flags)` but allows specifying the destination address.
        For IP sockets, the address is a pair: `(hostaddr, port)`.

        Args:
            data: The data to send.
            flags: Optional flags (defaults to 0). See the Unix manual.
            addr: The destination address.

        Returns:
            The number of bytes sent.
        """
        ...

    @overload
    def sendto(self, data: str | Buffer, flags: int, addr: int | tuple[int, str] | str, /) -> int:
        ...

    def setblocking(self, flag: bool, /) -> None:
        """
        Set the socket to blocking (flag is true) or non-blocking (false).

        Args:
            flag: Whether to block.
        """
        ...

    def settimeout(self, timeout: float | None, /) -> None:
        """
        Set a timeout on socket operations.

        Args:
            timeout: A float, in seconds, or None. Setting a timeout
                of None disables the timeout feature and is equivalent
                to setblocking(1). Setting a timeout of zero is the
                same as setblocking(0).
        """
        ...

    def gettimeout(self) -> float | None:
        """
        Returns the timeout associated with socket operations.

        Returns:
            The timeout in floating seconds. `None` indicates
            that timeouts on socket operations are disabled.
        """
        ...

    def setsockopt(self, level: int, option: int, value: int | str, /) -> None:
        """
        Set a socket option.

        Args:
            level: See the Unix manual.
            option: See the Unix manual.
            value: The option value, either an integer or string.
        """
        ...

    #remove?
    def setl2capsecurity(self, level: int, /) -> None:
        """
        Sets socket security.

        Args:
            level: One of `BT_SECURITY_SDP`, `BT_SECURITY_LOW`,
                `BT_SECURITY_MEDIUM`, or `BT_SECURITY_HIGH`.
        """
        ...

    def shutdown(self, flag: int, /) -> None:
        """
        Shut down the reading side of the socket (flag == 0), the writing side
        of the socket (flag == 1), or both ends (flag == 2).

        Args:
            flag: Which end(s) of the socket to shut down.
        """

    # tp_getset
    

def hci_devid(devaddr: str = ..., /) -> int: ...

def hci_get_route(devaddr: str = ..., /) -> int: ...

def hci_role(fd: int, devaddr: str, /) -> int: ...

def hci_read_clock(fd: int, handle: int, which: int, timeout: int, /) -> tuple[int, int]: ...

def hci_acl_conn_handle(fd: int, devaddr: str, /) -> int: ...

def hci_open_dev(device: int = -1, /) -> btsocket:
    """
    Opens and binds a new HCI socket.

    Args:
        device: integer device number

    Returns:
        A `btsocket` instance.
    """
    ...

def hci_close_dev(dev: int, /) -> None: ...

def hci_send_cmd(sock: btsocket, ogf: int, ocf: int, params: str = ..., /) -> int: ...

def hci_send_req(sock: btsocket, ogf: int, ocf: int, event: int, rlen: int, params: str | bytes = ..., timeout: int = 0) -> str: ...

def hci_inquiry(sock: btsocket, duration: int = 8, flush_cache: bool = True, lookup_class: bool = False, device_id: int = 0, iac: int = ...) -> list[str] | list[tuple[str, int]]: ...

def hci_read_remote_name(dd: btsocket, bdaddr: str, timeout: int = 5192) -> str:
    """
    Performs a remote name request to the specified bluetooth device.

    Args:
        dd: The HCI socket object to use.
        bdaddr: The bluetooth address of the remote device.
        timeout: Maximum amount of time, in milliseconds, to wait.

    Returns:
        The same of the device, or raises an error on failure.
    """
    ...

def hci_filter_new() -> str: ...

def hci_filter_clear(filter: str | bytes, /) -> str: ...

def hci_filter_all_events(filter: str | bytes, /) -> str: ...

def hci_filter_all_ptypes(filter: str | bytes, /) -> str: ...

def hci_filter_clear_opcode(filter: str | bytes, /) -> str: ...

def hci_filter_set_ptype(filter: str | bytes, ptype: int, /) -> str: ...

def hci_filter_clear_ptype(filter: str | bytes, ptype: int, /) -> str: ...

def hci_filter_test_ptype(filter: str | bytes, ptype: int, /) -> str: ...

def hci_filter_set_event(filter: str | bytes, event: int, /) -> str: ...

def hci_filter_clear_event(filter: str | bytes, event: int, /) -> str: ...

def hci_filter_test_event(filter: str | bytes, event: int, /) -> str: ...

def hci_filter_set_opcode(filter: str | bytes, opcode: int, /) -> str: ...

def hci_filter_test_opcode(filter: str | bytes, opcode: int, /) -> str: ...

def cmd_opcode_pack(ogf: int, ocf: int, /) -> int: ...

def cmd_opcode_ogf(opcode: int, /) -> int: ...

def cmd_opcode_ocf(opcode: int, /) -> int: ...

def ba2str(addr: str | bytes, /) -> str:
    """
    Converts a packed bluetooth address to a human readable string.
    """

def str2ba(addr: str, /) -> bytes:
    """
    Converts a bluetooth address string into a packed bluetooth address.
    The string should be of the form "XX:XX:XX:XX:XX:XX".
    """
    ...

def hci_opcode_name(opcode: int, /) -> str: ...

def hci_event_name(event_num: int, /) -> str: ...

def fromfd(fd: int, family: int, type: int, proto: int = 0, /) -> btsocket: ...

def btohs(i: int, /) -> int:
    """
    Convert a 16-bit integer from bluetooth to host byte order.
    """
    ...

def btohl(i: int, /) -> int: 
    """
    Convert a 32-bit integer from bluetooth to host byte order.
    """
    ...

def htobs(i: int, /) -> int: 
    """
    Convert a 16-bit integer from host to bluetooth byte order.
    """
    ...

def htobl(i: int, /) -> int: 
    """
    Convert a 32-bit integer from host to bluetooth byte order.
    """
    ...

def getdefaulttimeout() -> float: 
    """
    Returns the default timeout in floating seconds for new socket objects.
    A value of `None` indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    ...

def setdefaulttimeout(timeout: float, /) -> None:
    """
    Set the default timeout in floating seconds for new socket objects.
    A value of `None` indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    ...

def sdp_advertise_service(sock: btsocket, name: str | bytes, service_id: str,
                          service_classe: Sequence[str], profiles: Sequence[tuple[str, int]],
                          provider: str | bytes, description: str | bytes, protocols: Sequence[str], /) -> None: ...

def sdp_stop_advertising(sock: btsocket, /) -> None: ...

def hci_le_add_white_list(sock: btsocket, addr: str, type: int, timeout: int, /) -> int: ...

def hci_le_read_white_list_size(sock: btsocket, timeout: int, /) -> int: ...

def hci_le_clear_white_list(sock: btsocket, timeout: int, /) -> int: ...
