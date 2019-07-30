import re


def is_immediate(expr: str) -> bool:
    return (expr == 'true' or expr == 'false' or expr.isnumeric() or re.match('c.', expr))



def is_primcall(form: str) -> bool:
    return form.split()[0] == 'primcall'

def primcall_op(form: str)->str:
    return form.split()[1]

def args_list(form: str)->list[str]:
    return form.split()[2:]


def is_assignment(form: str)->str:
    return form.split()[0]=='let'
