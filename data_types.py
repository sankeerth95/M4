import re

fixnum_shift = 2
fixnum_mask = 3
ptr_mask = 7
ptr_mask_inv = int('fffffff8', base=16)

pair_tag = 1
vec_tag = 2
str_tag = 3
sym_tag = 5
closure_tag = 6

int_mask = int('ffffffff', base=16)
char_mask = 255
char_shift = 8
char_tag = 7

bool_mask = 255
bool_shift = 8
bool_tag = 15


wordsize = 4



def get_type(x: str)->str:
    if x == 'true' or x == 'false':
        return 'boolean'
    elif x.isnumeric():
        return 'int'
    elif re.match('c.', x):
        return 'char'
    else:
        return ''

def immediate_rep(x: str)->str:
    datatype = get_type(x)
    if datatype == 'int':
        return str(int_mask &(int(x) << fixnum_shift))
    elif datatype == 'char':
        return str(char_tag | (ord(x[1]) << char_shift))
    elif datatype == 'boolean':
        return str(bool_tag | ( int(x=='true') << bool_shift))

    return '77'
