"""Functions to calculate values related to exchanging money between currencies."""

def exchange_money(budget, exchange_rate):
    """
    Calculate the value of the budget exchanged into the target currency.
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate the amount of money left after exchanging budget.
    
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the value of an amount of bills in a selected denomination.
    
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate the number of bills exchangeable in the selected denomination.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the value that is not exchangeable with the selected denomination.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate exchangeable value of budget to target currency in one denomination.
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_rate = exchange_rate * (1 + spread / 100)
    value_with_spread = exchange_money(budget, spread_rate)
    exchangeable_bills = get_number_of_bills(value_with_spread, denomination)
    return get_value_of_bills(denomination, exchangeable_bills)