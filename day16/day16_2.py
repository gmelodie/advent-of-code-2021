import json
# packet
#   packet['version']
#   packet['type_id']
#   packet['length_type_id']
#   packet['header_len']
#   packet['data_len']

def sum_operation(packet):
    value = 0
    for subpacket in packet['subpackets']:
        value += subpacket['data']
    return value


def product_operation(packet):
    value = 1
    for subpacket in packet['subpackets']:
        value *= subpacket['data']
    return value


def min_operation(packet):
    values = []
    for subpacket in packet['subpackets']:
        values.append(subpacket['data'])
    return min(values)


def max_operation(packet):
    values = []
    for subpacket in packet['subpackets']:
        values.append(subpacket['data'])
    return max(values)


def gt_operation(packet):
    value = 0
    if packet['subpackets'][0]['data'] > packet['subpackets'][1]['data']:
        value = 1
    return value


def lt_operation(packet):
    value = 0
    if packet['subpackets'][0]['data'] < packet['subpackets'][1]['data']:
        value = 1
    return value


def eq_operation(packet):
    value = 0
    if packet['subpackets'][0]['data'] == packet['subpackets'][1]['data']:
        value = 1
    return value


OPERATIONS = {
    0: sum_operation,
    1: product_operation,
    2: min_operation,
    3: max_operation,
    5: gt_operation,
    6: lt_operation,
    7: eq_operation,
}

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
    packet['data_len'] = 0

    if packet['length_type_id'] == SUBPACKET_LEN: # next 15 bits are the len of the subpacket
        packet['header_len'] += 15
        subpacket_len = read_n_bits(15)
        while subpacket_len > 0 and int(DATA_STREAM[:subpacket_len], 2) != 0:
            subpacket = extract_packet()
            packet['subpackets'].append(subpacket)
            subpacket_len -= subpacket['total_len']

    elif packet['length_type_id'] == NUM_OF_SUBPACKETS:
        packet['header_len'] += 11
        n_subpackets = read_n_bits(11) # next 11 bits are the number of subpackets
        for _ in range(n_subpackets):
            packet['subpackets'].append(extract_packet())

    # calculate data_len
    for subpacket in packet['subpackets']:
        packet['data_len'] += subpacket['total_len']

    return packet


def extract_data(packet):
    if packet['type_id'] == 4:
        assert packet['length_type_id'] == -1
        packet['data_len'], packet['data'] = read_literal_value()
        return packet

    # IS OPERATION
    operation = packet['type_id']
    assert len(packet['subpackets']) > 0
    assert packet['length_type_id'] != -1
    assert 'data' not in packet
    packet['data'] = OPERATIONS[operation](packet)

    return packet


def extract_packet():
    packet = {}
    packet = extract_header(packet)
    packet = extract_subpackets(packet)
    packet = extract_data(packet)
    packet['total_len'] = packet['header_len'] + packet['data_len']

    print(json.dumps(packet, indent=4))
    return packet


def extract_packets():
    global DATA_STREAM
    packets = []
    while len(DATA_STREAM) > MIN_PKT_SIZE:
        packet = extract_packet()
        packets.append(packet)

    return packets


def hex_to_stream(hex_data):
    data_stream = ''
    for char in hex_data:
        data_stream += '{0:04b}'.format(int(char, 16))
    return data_stream


while hex_data := input():
    DATA_STREAM = hex_to_stream(hex_data) # trim leading '0b'
    packets = extract_packets()

    # print(json.dumps(packets[0], indent=4))
    # print(packets[0]['data'])

