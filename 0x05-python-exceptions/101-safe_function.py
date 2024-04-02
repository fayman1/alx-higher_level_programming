#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        q = fct(*args)
        return q
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
