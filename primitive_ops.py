import my_compile as cmp
import parsing_form as pf
import data_types as dt

def add1(expr: str)->str:
    cmp.compile_expr(pf.arg1(expr))
    return cmp.emit('addl $'+dt.immediate_rep('1') + ', %eax')

def subl(expr: str) -> str:
    cmp.compile_expr(pf.arg1(expr))
    return cmp.emit('subl $'+dt.immediate_rep('1') + ', %eax')

