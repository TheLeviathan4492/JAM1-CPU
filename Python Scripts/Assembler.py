import sys

instruction_set = {
  'nop': '00',

  'mov a, #': '01, ##',
  'mov b, #': '02, ##',
  'mov c, #': '03, ##',
  'mov d, #': '04, ##',
  'mov tl, #': '05, ##',
  'mov th, #': '06, ##', 

  'mov a, b': '07',
  'mov a, c': '08',
  'mov a, d': '09',
  'mov b, a': '0A',
  'mov b, c': '0B',
  'mov b, d': '0C',
  'mov c, a': '0D',
  'mov c, b': '0E',
  'mov c, d': '0F',
  'mov d, a': '10',
  'mov d, b': '11',
  'mov d, c': '12',

  'mov tl, a': '13',
  'mov tl, b': '14',
  'mov tl, c': '15',
  'mov tl, d': '16',
  'mov th, a': '17',
  'mov th, b': '18',
  'mov th, c': '19',
  'mov th, d': '1A',
  'mov a, tl': '1B',
  'mov b, tl': '1C',
  'mov c, tl': '1D',
  'mov d, tl': '1E',
  'mov a, th': '1F',
  'mov b, th': '20',
  'mov c, th': '21',
  'mov d, th': '22',

  'mov ra, tx': '23',
  'mov tx, ra': '24',
  'mov sp, tx': '25',
  'mov tx, sp': '26',
  'mov si, tx': '27',
  'mov tx, si': '28',
  'mov di, tx': '29',
  'mov tx, di': '2A',
  'mov di, si': '2B',
  'mov si, di': '2C',

  'dec ra': '30',
  'dec sp': '31',
  'dec si': '32',
  'dec di': '33',
  'inc sp': '34',
  'inc si': '35',
  'inc di': '36',

  'out lcd, a': '37',

  'mov a, [si]': '40',
  'mov b, [si]': '41',
  'mov c, [si]': '42',
  'mov d, [si]': '43',
  'mov a, [di]': '44',
  'mov b, [di]': '45',
  'mov c, [di]': '46',
  'mov d, [di]': '47',
  'mov a, [tx]': '48',
  'mov b, [tx]': '49',
  'mov c, [tx]': '4A',
  'mov d, [tx]': '4B',

  'mov [si], a': '4C',
  'mov [si], b': '4D',
  'mov [si], c': '4E',
  'mov [si], d': '4F',
  'mov [di], a': '50',
  'mov [di], b': '51',
  'mov [di], c': '52',
  'mov [di], d': '53',
  'mov [tx], a': '54',
  'mov [tx], b': '55',
  'mov [tx], c': '56',
  'mov [tx], d': '57',

  'call tx': '58, 00',
  'ret': '59, 00',

  'jmp tx': '5F, 60',

  'jo tx': '5F, 61',
  'jno tx': '5F, 62',

  'js tx': '5F, 63',
  'jns tx': '5F, 64',

  'jz tx': '5F, 65',
  'jnz tx': '5F, 66',
  'je tx': '5F, 65',
  'jne tx': '5F, 66',

  'jc tx': '5F, 67',
  'jnae tx': '5F, 67',
  'jb tx': '5F, 67',
  'jnc tx': '5F, 68',
  'jae tx': '5F, 68',
  'jnb tx': '5F, 68',
  'jbe tx': '5F, 69',
  'jna tx': '5F, 69',
  'ja tx': '5F, 6A',
  'jnbe tx': '5F, 6A',

  'jl tx': '5F, 6B',
  'jnge tx': '5F, 6B',
  'jge tx': '5F, 6C',
  'jnl tx': '5F, 6C',
  'jle tx': '5F, 6D',
  'jng tx': '5F, 6D',
  'jg tx': '5F, 6E',
  'jnle tx': '5F, 6E',

  'jlc tx': '5F, 6F',
  'jnlc tx': '5F, 70',

  'jmp di': '5F, 71',

  'push a': '72',
  'push b': '73',
  'push c': '74',
  'push d': '75',
  'push tl': '76',
  'push th': '77',

  'pop a': '78',
  'pop b': '79',
  'pop c': '7A',
  'pop d': '7B',
  'pop tl': '7C',
  'pop th': '7D',

  'clc': '7F',

  'shl a': '80',
  'shl b': '81',
  'shl c': '82',
  'shl d': '83',
  'shr a': '84',
  'shr b': '85',
  'shr c': '86',
  'shr d': '87',

  'add a, b': '88',
  'add a, c': '89',
  'add a, d': '8A',
  'add b, a': '8B',
  'add b, c': '8C',
  'add b, d': '8D',
  'add c, a': '8E',
  'add c, b': '8F',
  'add c, d': '90',
  'add d, a': '91',
  'add d, b': '92',
  'add d, c': '93',

  'addc a, b': '94',
  'addc a, c': '95',
  'addc a, d': '96',
  'addc b, a': '97',
  'addc b, c': '98',
  'addc b, d': '99',
  'addc c, a': '9A',
  'addc c, b': '9B',
  'addc c, d': '9C',
  'addc d, a': '9D',
  'addc d, b': '9E',
  'addc d, c': '9F',

  'sub a, b': 'A0',
  'sub a, c': 'A1',
  'sub a, d': 'A2',
  'sub b, a': 'A3',
  'sub b, c': 'A4',
  'sub b, d': 'A5',
  'sub c, a': 'A6',
  'sub c, b': 'A7',
  'sub c, d': 'A8',
  'sub d, a': 'A9',
  'sub d, b': 'AA',
  'sub d, c': 'AB',

  'subb a, b': 'AC',
  'subb a, c': 'AD',
  'subb a, d': 'AE',
  'subb b, a': 'AF',
  'subb b, c': 'B0',
  'subb b, d': 'B1',
  'subb c, a': 'B2',
  'subb c, b': 'B3',
  'subb c, d': 'B4',
  'subb d, a': 'B5',
  'subb d, b': 'B6',
  'subb d, c': 'B7',

  'inc a': 'B8',
  'inc b': 'B9',
  'inc c': 'BA',
  'inc d': 'BB',

  'incc a': 'BC',
  'incc b': 'BD',
  'incc c': 'BE',
  'incc d': 'BF',

  'dec a': 'C0',
  'dec b': 'C1',
  'dec c': 'C2',
  'dec d': 'C3',

  'and a, b': 'C4',
  'and a, c': 'C5',
  'and a, d': 'C6',
  'and b, a': 'C7',
  'and b, c': 'C8',
  'and b, d': 'C9',
  'and c, a': 'CA',
  'and c, b': 'CB',
  'and c, d': 'CC',
  'and d, a': 'CD',
  'and d, b': 'CE',
  'and d, c': 'CF',

  'or a, b': 'D0',
  'or a, c': 'D1',
  'or a, d': 'D2',
  'or b, a': 'D3',
  'or b, c': 'D4',
  'or b, d': 'D5',
  'or c, a': 'D6',
  'or c, b': 'D7',
  'or c, d': 'D8',
  'or d, a': 'D9',
  'or d, b': 'DA',
  'or d, c': 'DB',

  'xor a, a': 'DC',
  'xor a, b': 'DD',
  'xor a, c': 'DE',
  'xor a, d': 'DF',
  'xor b, a': 'E0',
  'xor b, b': 'E1',
  'xor b, c': 'E2',
  'xor b, d': 'E3',
  'xor c, a': 'E4',
  'xor c, b': 'E5',
  'xor c, c': 'E6',
  'xor c, d': 'E7',
  'xor d, a': 'E8',
  'xor d, b': 'E9',
  'xor d, c': 'EA',
  'xor d, d': 'EB',

  'not a': 'EC',
  'not b': 'ED',
  'not c': 'EE',
  'not d': 'EF',

  'cmp a, b': 'F0',
  'cmp a, c': 'F1',
  'cmp a, d': 'F2',
  'cmp b, a': 'F3',
  'cmp b, c': 'F4',
  'cmp b, d': 'F5',
  'cmp c, a': 'F6',
  'cmp c, b': 'F7',
  'cmp c, d': 'F8',
  'cmp d, a': 'F9',
  'cmp d, b': 'FA',
  'cmp d, c': 'FB',

  'test a': 'FC',
  'test b': 'FD',
  'test c': 'FE',
  'test d': 'FF'
}

psuedo_instructions = {
  'mov ab, #': ['mov a, #', 'mov b, #'],
  'mov ab, cd': ['mov a, c', 'mov b, d'],
  'mov ab, tx': ['mov a, tl', 'mov b, th'],

  'mov cd, #': ['mov c, #', 'mov d, #'],
  'mov cd, ab': ['mov c, a', 'mov d, b'],
  'mov cd, tx': ['mov c, tl', 'mov d, th'],

  'mov tx, #': ['mov tl, #', 'mov th, #'],
  'mov tx, ab': ['mov tl, a', 'mov th, b'],
  'mov tx, cd': ['mov tl, c', 'mov th, d'],

  'add ab, cd': ['add a, c', 'addc b, d'],
  'add cd, ab': ['add c, a', 'addc d, b'],

  'add ab, c': ['add a, c', 'incc b'],
  'add ab, d': ['add a, d', 'incc b'],
  'add cd, a': ['add c, a', 'incc d'],
  'add cd, b': ['add c, b', 'incc d'],

  'push tx': ['push tl', 'push th'],
  'pop tx': ['pop th', 'pop tl']
}

def get_file():
  if len(sys.argv) != 2:
    print("add file")
    sys.exit(1)
  file_name = r'C:\JAM-1 Files\Assembly Code\\' + sys.argv[1]
  file_name = file_name[:28] + file_name[29:]
  return file_name

def find_instruction_size(instruction):
  instruction_size = 0
  if instruction in instruction_set:
    if ',' in instruction_set[instruction]:
      instruction_size = 2
    else:
      instruction_size = 1
  return instruction_size
  

def write_program_rom(data, file):
  line_counter = 0
  program_file = open(file, "w")
  program_file.write('v3.0 hex words addressed' + '\n')
  program_file.write('0000: ')
  for n in range(len(data)):
    if (((n + 1) % 16) == 0):
      line_counter += 1
      hex_line_counter = hex(line_counter)[2:]
      hex_line_counter = hex_line_counter.zfill(3) + '0: '
      program_file.write(data[n] + '\n')
      if hex_line_counter != '8000: ':
        program_file.write(hex_line_counter)
    else:
      program_file.write(data[n] + ' ')
  program_file.close()


def remove_spaces(line_data):
  new_line_data = []
  for line in line_data:
    if not line.isspace():
      new_line_data.append(line)
  return new_line_data


def create_line_list(file, line_data):
  file_label = open(file, 'r')
  line_data = file_label.readlines()
  file_label.close()
  return line_data


def include_library(line_data):
  for index, line in enumerate(line_data):
    if '.include' in line:
      file_name = r'C:\JAM-1 Files\Libraries\\' + line[9:].strip()
      file_name = file_name[:24] + file_name[25:]
      file_label = open(file_name, 'r')
      library_line_data = file_label.readlines()
      line_data[index:index+1] = library_line_data
      file_label.close()
  return line_data


def remove_comments(line_data):
  for line_index, line in enumerate(line_data):
    for char_index, char in enumerate(line):
      if char == ';':
        line_data[line_index] = line[:char_index] + '\n'
  return line_data


def order_segments(line_data):
  new_line_data = []
  segment_list = []
  segment_line = []
  segment_dict = {}
  for index, line in enumerate(line_data):
    if line.startswith('.segment'):
      segment_list.append(line[9:].strip())
      segment_line.append(index)
  for index, segment in enumerate(segment_list):
    if index == (len(segment_list) - 1):
      segment_line_data = line_data[(segment_line[index] + 1):]
    else:
      segment_line_data = line_data[(segment_line[index] + 1):(segment_line[index+1])]
    segment_dict[segment] = segment_line_data
  new_line_data.extend(segment_dict['Code'])
  segment_list.remove('Code')
  for segment in segment_list:
    new_line_data.extend(segment_dict[segment])
  return new_line_data

def replace_data_bytes(line_data):
  data_byte_data = []
  for line in line_data:
    if line.strip()[0:2] == 'db':
      data_bytes = line[5:]
      data_byte_data.append(str(data_bytes))
  return data_byte_data


def split_data_bytes(data_byte_data):
  for index, byte in enumerate(data_byte_data):
    parts = byte.split(',')
    split_portion = [part.strip() for part in parts]
    data_byte_data[index] = split_portion

  for portion_index, portion in enumerate(data_byte_data):
    for byte_index, byte in enumerate(portion):
      if str(byte).startswith("'") and str(byte).endswith("'"):
        ascii_list = [str(ord(char)) for char in byte.strip("'")]
        data_byte_data[portion_index][byte_index:byte_index+1] = ascii_list

  for portion_index, portion in enumerate(data_byte_data):
    for byte_index, byte in enumerate(portion):
      hex_byte = hex(int(byte))[2:].upper().zfill(2)
      data_byte_data[portion_index][byte_index] = hex_byte
  
  return data_byte_data


def replace_constants(line_data):
  constant_values = []
  for index, line in enumerate(line_data):
    stripped_line = line.strip()
    if (not stripped_line in instruction_set) and (not stripped_line in psuedo_instructions) and (line[0].isspace()) and (stripped_line[0:2] != 'db'):
      split_line = line.split(',')
      constant = split_line[1].strip()
      constant_values.append(constant)
      line_data[index] = split_line[0] + ', #'
  return [line_data, constant_values]


def split_psuedo_constants(const_instructions, const_data):
  const_address_offset = 0
  for index, item in enumerate(const_instructions):
    const_instruction = item.strip()
    adjusted_index = index + const_address_offset
    if const_instruction in psuedo_instructions:
      constant = str(const_data[adjusted_index])
      split_constants = []
      if constant.isdigit():
        split_constants = [str(int(constant)&255), str((int(constant)>>8)&255)]
      else:
        split_constants = [constant + 'L', constant + 'H']
      const_data[adjusted_index:adjusted_index+1] = split_constants
      const_address_offset += 1

  return const_data
        

def split_psuedo_instructions(line_data, constant_data):
  const_instructions = []
  for line in line_data:
    if '#' in line:
        const_instructions.append(line)
  for index, code_line in enumerate(line_data):
    new_lines = []
    line = code_line.strip()
    if line in psuedo_instructions:
      for split_instruction in psuedo_instructions[line]:
        new_lines.append('  '+split_instruction)
      line_data[index:index+1] = new_lines 
  constant_data = split_psuedo_constants(const_instructions, constant_data)
  return [line_data, constant_data]

def add_in_labels(line_data, constant_data, data_byte_data):
  new_line_data = []
  labels_list = []
  address_counter = 0
  split_labels_list = []
  db_counter = 0

  for code_line in line_data:
    line = code_line.strip()
    if (not line in instruction_set) and (not line[0:2] == 'db'):
      labels_list.append([line[:(len(line)-1)], address_counter])

    elif (line[0:2] == 'db'):
      address_counter += len(data_byte_data[db_counter])
      db_counter += 1
      new_line_data.append(line)
    
    else:
      address_counter += find_instruction_size(line)
      new_line_data.append(line)

  line_data = new_line_data
    
  for label, label_addr in labels_list:
    split_labels_list.append([label + 'L', label_addr&255])
    split_labels_list.append([label + 'H', (label_addr>>8)&255])
    
  labels_list = split_labels_list
  for const_index, constant in enumerate(constant_data):
    for label, label_addr in labels_list:
      if constant == label:
        constant_data[const_index] = label_addr
        
  return [line_data, constant_data]



def create_rom_data(line_data):
  rom_data = []
  for instruction in line_data:
    if instruction[0:2] == 'db':
      rom_data.append('DB')
    else:
      opcode = instruction_set[instruction]
      if ',' in opcode:
        parts = opcode.split(',')
        split_opcodes = [part.strip() for part in parts]
        rom_data.extend(split_opcodes)
      else:
        rom_data.append(opcode)
  return rom_data


def pad_rom_data(rom_data):
  total_byte_count = len(rom_data)
  for n in range((2**15) - total_byte_count):
    rom_data.append('00')
  return rom_data
      
    
def reinsert_constants(rom_data, constants_data):
  const_counter = 0
  for address, data_byte in enumerate(rom_data):
    if data_byte == '##':
      constant = constants_data[const_counter]
      const_byte = hex(int(constant))[2:].upper().zfill(2)
      rom_data[address] = const_byte
      const_counter += 1
  return rom_data


def reinsert_data_bytes(rom_data, data_byte_data):
  db_counter = 0
  for address, opcode in enumerate(rom_data):
    if opcode == 'DB':
      data_byte = data_byte_data[db_counter]
      rom_data[address:address+1] = data_byte
      db_counter += 1
  return rom_data

def assemble(file):
  file_label = open(file, 'r')
  code_lines = file_label.readlines()
  file_label.close()

  code_lines = include_library(code_lines)
  code_lines = remove_comments(code_lines)
  code_lines = remove_spaces(code_lines)
  code_lines = order_segments(code_lines)

  data_byte_list = replace_data_bytes(code_lines)
  data_byte_list = split_data_bytes(data_byte_list)

  code_lines, constants_list = replace_constants(code_lines)
  code_lines, constants_list = split_psuedo_instructions(code_lines, constants_list)
  code_lines, constants_list = add_in_labels(code_lines, constants_list, data_byte_list)

  rom_bytes_list = create_rom_data(code_lines)

  rom_bytes_list = reinsert_constants(rom_bytes_list, constants_list)
  rom_bytes_list = reinsert_data_bytes(rom_bytes_list, data_byte_list)

  rom_bytes_list = pad_rom_data(rom_bytes_list)
  rom_file_name =  r'C:\JAM-1 Files\program_rom.txt'
  write_program_rom(rom_bytes_list, rom_file_name)

assemble(get_file())