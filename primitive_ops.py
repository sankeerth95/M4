import my_compile as cmp
import parsing_form as pf
import data_types as dt

def emit_is_eax_equal_to(val: str)->str:
    asm: str = ''
    asm += cmp.emit('cmpl $'+val+', %eax')
    asm += cmp.emit('xorl %eax, %eax')
    asm += cmp.emit('sete %al')
    asm += cmp.emit('sall $'+dt.bool_shift+', %eax')
    asm += cmp.emit('orl $'+dt.bool_tag+', %ax')
    return asm


def add1(expr: str, si: int, env: str)->str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('addl $'+dt.immediate_rep('1') + ', %eax')
    return asm

def subl(expr: str, si: int, env: str) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('subl $'+dt.immediate_rep('1') + ', %eax')
    return asm

def is_int(expr: str, si: int, env: dict)-> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('andl $'+dt.fixnum_mask+', %eax')
    asm += emit_is_eax_equal_to('0')
    return asm


def is_bool(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env )
    asm += cmp.emit('andl $'+dt.bool_mask+', %eax')
    asm += emit_is_eax_equal_to(str(dt.bool_tag))
    return asm


def is_char(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('andl $'+dt.char_mask+', %eax')
    asm += emit_is_eax_equal_to(str(dt.char_mask))
    return asm

def is_zero(expr: str, si: int, env: dict)->str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += emit_is_eax_equal_to('0')
    return asm


def int_add(expr: str, si: int, env: dict)->str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('addl '+ si+'(%esp), %eax')
    return asm


def int_sub(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('subl ' + si+'(%esp), %eax')
    return asm


def int_mul(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('shrl $'+dt.fixnum_shift + ', %eax')
    asm += cmp.emit('imull ' + si+'(%esp), %eax')
    return asm


def int_eq(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('cmpl ' + si+'(%esp), %eax')
    asm += cmp.emit('xorl %eax, %eax')
    asm += cmp.emit('sete %al')
    asm += cmp.emit('sall $'+dt.bool_shift+', %eax')
    asm += cmp.emit('orl $'+dt.bool_tag+', %eax')
    return asm


def int_lt(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('cmpl ' + si+'(%esp), %eax')
    asm += cmp.emit('xorl %eax, %eax')
    asm += cmp.emit('setl %al')
    asm += cmp.emit('sall $'+dt.bool_shift+', %eax')
    asm += cmp.emit('orl $'+dt.bool_tag+', %eax')
    return asm


def char_eq(expr: str, si: int, env: dict) -> str:
    asm: str = ''
    asm += cmp.compile_expr(pf.args_list(expr)[0], si, env)
    asm += cmp.emit('movl %eax, '+si+'(%esp)')
    asm += cmp.compile_expr(pf.args_list(expr)[1], si-dt.wordsize, env)
    asm += cmp.emit('cmpl ' + si+'(%esp), %eax')
    asm += cmp.emit('xorl %eax, %eax')
    asm += cmp.emit('sete %al')
    asm += cmp.emit('sall $'+dt.bool_shift+', %eax')
    asm += cmp.emit('orl $'+dt.bool_tag+', %eax')
    return asm
