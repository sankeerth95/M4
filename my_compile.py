import os
import data_types as dt
import parsing_form as pf
import primitive_ops as p_ops

def emit(code_line: str)-> str:
    return(code_line + "\n")

# si: stack index
def compile_primitive_call(expr: str, si: int)->str:
    fn_mapping: dict = {
        'add1': p_ops.add1,
        'sub1': p_ops.sub1,
        'is_int': p_ops.is_int,
        'is_bool': p_ops.is_boolm,
        'is_char': p_ops.is_char,
        'is_zero': p_ops.is_zero,
        '+': p_ops.binary_add,
        '-': p_ops.binary_sub 
    }
    return fn_mapping[pf.primcall_op(expr)](expr, si)

def compile_expr(expr: str, si: int)->str:

    if pf.is_immediate(expr):
        return emit("movl $" + dt.immediate_rep(expr) + ", %eax")
    elif pf.is_primcall(expr):
        return compile_primitive_call(expr, si)
    else:
        return ''


def compile_program(program :str)-> str:
    asm: str = ""

    asm += emit(".text")
    asm += emit(".p2align 4,,15")
    asm += emit(".globl language_entry")
    asm += emit("language_entry:")

    asm += emit("pushl %esi")
    asm += emit("pushl %edi")
    asm += emit("pushl %edx")

    asm += compile_expr(program, -dt.wordsize)

    asm += emit("popl %edx")
    asm += emit("popl %edi")
    asm += emit("popl %esi")

    asm += emit("ret")
    return asm

def compile_to_binary(program :str)->int:
    with open("/tmp/compiled.s", "w") as f:
        f.write(compile_program(program))
    return os.system("gcc -fomit-frame-pointer -m32 rts.c /tmp/compiled.s")


def compile_and_run(program: str)->None:
    compile_to_binary(program)
    os.system('./a.out > output.txt')
    with open('output.txt', "r") as fp:
        print(fp.read())
    os.remove('output.txt')
    os.remove('./a.out')
