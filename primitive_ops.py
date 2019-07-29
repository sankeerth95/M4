import my_compile as cmp
import parsing_form as pf
import data_types as dt

def emit_is_eax_equal_to(val: str)->str:
    asm = ''
    asm += cmp.emit('cmpl $'+val+', %eax')
    asm += cmp.emit('xorl %eax, %eax')
    asm += cmp.emit('sete %al')
    asm += cmp.emit('sall $'+dt.bool_shift+', %eax')
    asm += cmp.emit('orl $'+dt.bool_tag+', %ax')
    return asm


def add1(expr: str)->str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += cmp.emit('addl $'+dt.immediate_rep('1') + ', %eax')
    return asm

def subl(expr: str) -> str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += cmp.emit('subl $'+dt.immediate_rep('1') + ', %eax')
    return asm

def is_int(expr: str)-> str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += cmp.emit('andl $'+dt.fixnum_mask+', %eax')
    asm += emit_is_eax_equal_to('0')
    return asm


def is_bool(expr: str) -> str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += cmp.emit('andl $'+dt.bool_mask+', %eax')
    asm += emit_is_eax_equal_to(str(dt.bool_tag))
    return asm


def is_char(expr: str) -> str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += cmp.emit('andl $'+dt.char_mask+', %eax')
    asm += emit_is_eax_equal_to(str(dt.char_mask))
    return asm

def is_zero(expr: str)->str:
    asm = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0])
    asm += emit_is_eax_equal_to('0')
    return asm

