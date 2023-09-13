#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions.
#
import random

def create_expense():
    """
    Create the expenses
    :return:
    """
    expense_type = ["water", "heating", "electricity", "gas", "other"]
    apartament_number = random.randint(1, 30)
    amount = random.randint(1, 1000)
    expenses = {
        'Apartament' : apartament_number,
        'Type' : expense_type[random.randint(0, 4)],
        'Amount' : amount

    }
    return expenses

def generate_random_expenses():
    """
    Generate random expenses
    :return:
    """
    list_of_expenses = []
    for i in range (0, 10):
        expenses = create_expense()
        list_of_expenses.append(expenses)
    return list_of_expenses

def valid_expense(apartament_number, type, amount):
    """
    Validate the expenses
    :param apartament_number:
    :param type:
    :param amount:
    :return:
    """
    if apartament_number < 0:
        raise ValueError("Apartament number must be positive")
    if type not in ["water", "heating", "electricity", "gas", "other"]:
        raise ValueError("Invalid type")
    if amount < 0:
        raise ValueError("Amount must be positive")

    return True

def add_expense(all_expenses, apartament_number, type, amount):
    """
    Add the expenses
    :param all_expenses:
    :param apartament_number:
    :param type:
    :param amount:
    :return:
    """
    new_expense = {
        'Apartament' : apartament_number,
        'Type' : type,
        'Amount' : amount
    }
    if new_expense in all_expenses:
        raise ValueError("Expense already exists")

    if valid_expense(apartament_number, type, amount):
        all_expenses.append(new_expense)

def remove_apartament(all_expenses, apartament_number):
    """
    Remove the expenses by apartament
    :param all_expenses:
    :param apartament_number:
    :return:
    """
    for expense in all_expenses:
        if valid_expense(apartament_number, expense['Type'], expense['Amount']):
            try:
                if expense['Apartament'] == apartament_number:
                    all_expenses.remove(expense)
            except ValueError:
                pass

def remove_apartaments_between(all_expenses, start_apartament, finish_apartament):
    """
    Remove the expenses by apartaments
    :param all_expenses:
    :param start_apartament:
    :param finish_apartament:
    :return:
    """
    if start_apartament < 0 or finish_apartament < 0:
        raise ValueError("Apartament number must be positive")
    for expense in all_expenses:
        if expense['Apartament'] >= start_apartament and expense['Apartament'] <= finish_apartament:
            all_expenses.remove(expense)

def remove_type(all_expenses, type):
    """
    Remove the expenses by type
    :param all_expenses:
    :param type:
    :return:
    """
    if type not in ["water", "heating", "electricity", "gas", "other"]:
        raise ValueError(": Invalid type")
    for expense in all_expenses:
        if expense['Type'] == type:
            all_expenses.remove(expense)

def replace(all_expenses, apartament_number, type, amount):
    """
    Replace the expenses by apartament
    :param all_expenses:
    :param apartament_number:
    :param type:
    :param amount:
    :return:
    """
    if valid_expense(apartament_number, type, amount):
        for expense in all_expenses:
            if expense['Apartament'] == apartament_number and expense['Type'] == type:
                expense['Amount'] = amount

def list_expense_apartament(all_expenses, apartament_number):
    """
    List the expenses by apartament
    :param all_expenses:
    :param apartament_number:
    :return:
    """
    list = []
    for expense in all_expenses:
        if valid_expense(apartament_number, expense['Type'], expense['Amount']):
            try:
                if expense['Apartament'] == apartament_number:
                    list.append(expense)
            except ValueError:
                pass
    return list

def list_expense_apartament_lower(all_expenses, value):
    """
    List the expenses by value
    :param all_expenses:
    :param value:
    :return:
    """
    list = []
    for expense in all_expenses:
        if expense['Amount'] < value:
            list.append(expense)
    return list

def list_expense_apartament_higher(all_expenses, value):
    """
    List the expenses by value
    :param all_expenses:
    :param value:
    :return:
    """
    list = []
    for expense in all_expenses:
        if expense['Amount'] > value:
            list.append(expense)
    return list

def list_expense_apartament_equal(all_expenses, value):
    """
    List the expenses by value
    :param all_expenses:
    :param value:
    :return:
    """
    list = []
    for expense in all_expenses:
        if expense['Amount'] == value:
            list.append(expense)
    return list

def filter_by_type(all_expenses, type):
    """
    Filter the expenses by type
    :param all_expenses:
    :param type:
    :return:
    """
    list = []
    for expense in all_expenses:
        if expense['Type'] == type:
            list.append(expense)
    return list

def filter_by_value(all_expenses, value):
    """
    Filter the expenses by value
    :param all_expenses:
    :param value:
    :return:
    """
    list = []
    for expense in all_expenses:
        if valid_expense(expense['Apartament'], expense['Type'], value):
            try:
                if expense['Amount'] <= value:
                    list.append(expense)
            except ValueError:
                pass
    return list

def undo(all_expenses, undo_list):
    """
    Undo the last operation
    :param all_expenses:
    :param undo_list:
    :return:
    """
    if len(undo_list) > 0:
        all_expenses = undo_list.pop()
    return all_expenses


