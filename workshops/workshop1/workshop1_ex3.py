def tax(income):
    """
    Return the taxes owed for a given income.

    Parameters
    ----------
    income
        Gross income

    Returns
    ----------
        Tax owed
    """

    if income <= 300000:
        tax = 0
    elif 300000 < income <= 700000:
        tax = (income - 300000) * 0.2
    else:
        tax = (700000 - 300000) * 0.2 + (income - 700000) * 0.35

    return tax


import numpy as np

incomes = np.linspace(0, 1200000, 13)


taxes_loop = []


for income in incomes:
    taxes = tax(income)
    taxes_loop.append(taxes)
    net_income = income - taxes

    print(
        f'Gross income: {income:10.0f};     '
        f'Taxes: {taxes:10.0f};     '
        f'Net income {net_income:10.0f}'
    )
