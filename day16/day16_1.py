import json
# packet
#   packet['version']
#   packet['type_id']
#   packet['length_type_id']
#   packet['header_len']
#   packet['data_len']


BASE_HEADER_LEN = 6
SUBPACKET_LEN = 0
NUM_OF_SUBPACKETS = 1
MIN_PKT_SIZE = 7
DATA_STREAM = ""

def read_n_bits(n): # pops n bits from DATA_STREAM
    global DATA_STREAM
    data = int(DATA_STREAM[:n], 2)
    DATA_STREAM = DATA_STREAM[n:]
    return data


def extract_header(packet):
    packet['version'] = read_n_bits(3)
    packet['type_id'] = read_n_bits(3)
    packet['length_type_id'] = -1
    if packet['type_id'] != 4:
        packet['length_type_id'] = read_n_bits(1)

    header_len = BASE_HEADER_LEN
    if packet['length_type_id'] != -1:
        header_len += 1
    packet['header_len'] = header_len

    return packet


def read_literal_value():
    global DATA_STREAM
    data = ''
    data_len = 0
    is_last_number = '1'

    while is_last_number == '1':
        is_last_number, number = DATA_STREAM[0], DATA_STREAM[1:5]
        data += number
        data_len += 5
        DATA_STREAM = DATA_STREAM[5:]

    return data_len, int(data, 2)


def extract_subpackets(packet):
    global DATA_STREAM
    packet['subpackets'] = []

    if packet['length_type_id'] == SUBPACKET_LEN: # next 15 bits are the len of the subpacket
        subpacket_len = read_n_bits(15) # TODO: we currently don't use the len
        while subpacket_len > 0 and len(DATA_STREAM) > MIN_PKT_SIZE:
            subpacket = extract_packet()
            packet['subpackets'].append(subpacket)
            subpacket_len -= subpacket['total_len']

    elif packet['length_type_id'] == NUM_OF_SUBPACKETS:
        n_subpackets = read_n_bits(11) # next 11 bits are the number of subpackets
        for _ in range(n_subpackets):
            packet['subpackets'].append(extract_packet())

    return packet


def extract_data(packet):
    packet['data_len'] = 0

    if packet['type_id'] == 4:
        assert packet['length_type_id'] == -1
        packet['data_len'], packet['data'] = read_literal_value()
        return packet

    # IS OPERATION

    # calculate data_len
    for subpacket in packet['subpackets']:
        packet['data_len'] += subpacket['total_len']

    return packet


def ignore_padding(packet):
    global DATA_STREAM
    packet_len = packet['header_len'] + packet['data_len']
    padding = 4 - packet_len % 4

    read_n_bits(padding)

    # packet['total_len'] = raw_packet_len + padding
    # print(DATA_STREAM[total_packet_len:], ' | ', DATA_STREAM[:total_packet_len])
    # return packet

def extract_packet():
    packet = {}
    packet = extract_header(packet)
    packet = extract_subpackets(packet)
    packet = extract_data(packet)
    packet['total_len'] = packet['header_len'] + packet['data_len']

    # print(json.dumps(packet, indent=4))
    return packet


def extract_packets():
    global DATA_STREAM
    packets = []
    while len(DATA_STREAM) > MIN_PKT_SIZE:
        packet = extract_packet()
        packets.append(packet)

    ignore_padding(packets[-1])
    return packets


def hex_to_stream(hex_data):
    data_stream = ''
    for char in hex_data:
        data_stream += '{0:04b}'.format(int(char, 16))
    return data_stream


def sum_versions(packet):
    s = packet['version']
    for subpacket in packet['subpackets']:
        s += sum_versions(subpacket)
    return s


hex_data = input()
DATA_STREAM = hex_to_stream(hex_data) # trim leading '0b'
packets = extract_packets()

sum_v = 0
for packet in packets:
    print(json.dumps(packet, indent=4))
    sum_v += sum_versions(packet)
print(sum_v)

