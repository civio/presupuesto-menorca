import six

if six.PY2:
    from menorca_budget_loader import MenorcaBudgetLoader
else:
    from .menorca_budget_loader import MenorcaBudgetLoader
