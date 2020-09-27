import inspect
from collections import OrderedDict


def rando_fn(abc, df = '123'):
	print(abc, df)

sig = inspect.signature(rando_fn)
print(sig.parameters.items())
