import re

def is_primcall(form: str) -> bool:
    return form.split()[0] == 'primcall'

def primcall_op(form: str)->str:
    return form.split()[1]

def primcall_args_list(str: expr)->list[str]:
    return expr.split()[2:]

def is_immediate(expr: str)-> bool:
    return (expr == 'true' or expr == 'false' or expr.isnumeric() or re.match('c.', expr) )

