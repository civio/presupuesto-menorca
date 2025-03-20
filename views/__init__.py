import six

if six.PY2:
    from guidedvisit import guidedvisit
else:
    from .guidedvisit import guidedvisit
