"""
q - quit
c - continue
s - step by step execution
PYTHONBREAKPOINT=0 python3 builtins/breakpoint.py - skip breakpoint
PYTHONBREAKPOINT=1 python3 builtins/breakpoint.py - ignore breakpoint
"""

for i in range(10):
    print(i)

    if i == 5:
        breakpoint()
