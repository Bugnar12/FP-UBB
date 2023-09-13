#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy

import functions

def commands():
    commands_ap ={
        'add' : add_expense,
        'remove_apartament' : remove_apartament,
        'remove_apartaments_between' : remove_apartaments_between,
        'remove_type' : remove_type,
        'replace' : replace,
        'list' : display_expenses,
        'list_apartament' : list_expense_apartament,
        'list_sign' : list_expense_apartament_lower_equal_greater,
        'filter_type' : filter_type,
        'filter_value' : filter_value,
        'undo' : undo
    }
    return commands_ap

def add_expense(all_expenses, params : int, apartament_log):
    if len(params) != 3:
        print("Add has 3 parameters")
        return
    apartament_number = int(params[0])
    type = params[1]
    amount = int(params[2])
    functions.add_expense(all_expenses, apartament_number, type, amount)
    apartament_log.append(copy.deepcopy(all_expenses))
    print("Expense added")

def display_expenses(all_expenses, params : int, apartament_log):
    if len(params) != 0:
        print("Display has no other input")
        return
    list = copy.deepcopy(all_expenses)
    list.sort(key = lambda x: x['Apartament'])
    for expense in list:
        print(expense)
    print("Expenses displayed")

def remove_apartament(all_expenses, params : int, apartament_log):
    if len(params) != 1:
        print("Remove_apartament has 1 parameter")
        return
    apartament_number = int(params[0])
    functions.remove_apartament(all_expenses, apartament_number)
    apartament_log.append(copy.deepcopy(all_expenses))
    print("Expenses removed by apartament")

def remove_apartaments_between(all_expenses, params : int, apartament_log):
    if len(params) != 2:
        print("Choose an interval of 2 apartaments")
        return
    start_apartament = int(params[0])
    finish_apartament = int(params[1])
    functions.remove_apartaments_between(all_expenses, start_apartament, finish_apartament)
    apartament_log.append(copy.deepcopy(all_expenses))
    print("Expenses removed by interval")

def remove_type(all_expenses, params : int, apartament_log):
    if len(params) != 1:
        print("Remove_type has 1 parameter")
        return
    type = params[0]
    functions.remove_type(all_expenses, type)
    apartament_log.append(copy.deepcopy(all_expenses))
    print("Expenses removed by type")

def replace(all_expenses, params : int, apartament_log):
    if len(params) != 3:
        print("Replace has 3 parameters")
        return
    apartament_number = int(params[0])
    type = params[1]
    amount = int(params[2])
    functions.replace(all_expenses, apartament_number, type, amount)
    apartament_log.append(copy.deepcopy(all_expenses))
    print("Expense replaced")

def list_expense_apartament(all_expenses, params : int, apartament_log):
    if len(params) != 1:
        print("List_apartament has 1 parameter")
        return
    apartament_number = int(params[0])
    list = functions.list_expense_apartament(all_expenses, apartament_number)
    apartament_log.append(copy.deepcopy(all_expenses))
    for expense in list:
        print(expense)
    print("Expenses displayed")

def list_expense_apartament_lower_equal_greater(all_expenses, params : int, apartament_log):
    if len(params) != 2:
        print("List_apartament has 2 parameters")
        return
    sign = params[0]
    value = int(params[1])
    if sign == "<":
        list1 = functions.list_expense_apartament_lower(all_expenses, value)
        apartament_log.append(copy.deepcopy(all_expenses))
        for expense in list1:
            print(expense)
    if sign == "=":
        list2 = functions.list_expense_apartament_equal(all_expenses, value)
        apartament_log.append(copy.deepcopy(all_expenses))
        for expense in list2:
            print(expense)
    if sign == ">":
        list3 = functions.list_expense_apartament_higher(all_expenses, value)
        apartament_log.append(copy.deepcopy(all_expenses))
        for expense in list3:
            print(expense)
    print("Expenses displayed")

def filter_type(all_expenses, params, apartament_log):
    if len(params) != 1:
        print("Filter_type has 1 parameter")
        return
    type = params[0]
    list = functions.filter_by_type(all_expenses, type)
    apartament_log.append(copy.deepcopy(all_expenses))
    for expense in list:
        print(expense)
    print("Expenses filtered by type")

def filter_value(all_expenses, params, apartament_log):
    if len(params) != 1:
        print("Filter_value has 1 parameter")
        return
    value = int(params[0])
    list = functions.filter_by_value(all_expenses, value)
    apartament_log.append(copy.deepcopy(all_expenses))
    for expense in list:
        print(expense)
    print("Expenses filtered by value")

def undo(all_expenses, params, apartament_log):
    if len(params) != 0:
        print("Undo has no parameters")
        return
    if len(apartament_log) == 0:
        print("Nothing to undo")
        return
    else:
        apartament_log.pop()
        all_expenses.clear()
        all_expenses.extend(apartament_log[-1])
        print("Undo successful")




def printings():
    print("Available commands:")
    print("add <apartament> <type> <amount>")
    print("remove_apartament <apartament>")
    print("remove_apartaments_between <apartament> <apartament>")
    print("remove_type <type>")
    print("replace <apartament> <type> <amount>")
    print("list")
    print("list_apartament <apartament>")
    print("list_sign <sign> <value>")
    print("filter_type <type>")
    print("filter_value <value>")
    print("undo")
    print("exit")



def run():
    printings()
    all_expenses = functions.generate_random_expenses()
    apartament_log = []
    apartament_log.append(copy.deepcopy(all_expenses))
    while True:
        commands_ap = commands()
        command = input(">>")
        command = command.strip()
        if command == "":
            print("Invalid command")
            continue
        if command == "exit":
            return
        parts = command.split()
        command_name = parts[0]
        params = parts[1:]
        if command_name in commands_ap:
            try:
                commands_ap[command_name](all_expenses, params ,apartament_log)
            except ValueError as ve:
                print("Value not valid", ve)
        else:
            print("Invalid command! Try another")
            printings()



