#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        x = None
    finally:
        print(f"Inside result: {x}")
    return x
