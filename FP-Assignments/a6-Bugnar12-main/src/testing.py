from src.functions import *
#In this module test all the functions in the src.functions

def test_create_expense():
    """
    Test the create_expense function
    :return:
    """
    expense = create_expense()
    assert expense['Apartament'] >= 1 and expense['Apartament'] <= 30
    assert expense['Type'] in ["water", "heating", "electricity", "gas", "other"]
    assert expense['Amount'] >= 1 and expense['Amount'] <= 1000

def test_random_expenses():
    expenses_random = generate_random_expenses()
    assert len(expenses_random) == 10

def test_add_expense():
    """
    Test the add_expense function
    :return:
    """
    all_expenses = []
    add_expense(all_expenses, 1, "water", 100)
    assert len(all_expenses) == 1
    assert all_expenses[0]['Apartament'] == 1
    assert all_expenses[0]['Type'] == "water"
    assert all_expenses[0]['Amount'] == 100
    add_expense(all_expenses, 2, "heating", 200)
    assert len(all_expenses) == 2
    assert all_expenses[1]['Apartament'] == 2
    assert all_expenses[1]['Type'] == "heating"
    assert all_expenses[1]['Amount'] == 200
    add_expense(all_expenses, 3, "electricity", 300)
    assert len(all_expenses) == 3
    assert all_expenses[2]['Apartament'] == 3
    assert all_expenses[2]['Type'] == "electricity"
    assert all_expenses[2]['Amount'] == 300
    add_expense(all_expenses, 4, "gas", 400)
    assert len(all_expenses) == 4
    assert all_expenses[3]['Apartament'] == 4
    assert all_expenses[3]['Type'] == "gas"
    assert all_expenses[3]['Amount'] == 400
    add_expense(all_expenses, 5, "other", 500)
    assert len(all_expenses) == 5
    assert all_expenses[4]['Apartament'] == 5
    assert all_expenses[4]['Type'] == "other"
    assert all_expenses[4]['Amount'] == 500


def test_remove_apratament():
    """
    Test the remove_apratament function
    :return:
    """
    all_expenses = []
    add_expense(all_expenses, 1, "water", 100)
    add_expense(all_expenses, 2, "heating", 200)
    add_expense(all_expenses, 3, "electricity", 300)
    add_expense(all_expenses, 4, "gas", 400)
    add_expense(all_expenses, 5, "other", 500)
    assert len(all_expenses) == 5
    remove_apartament(all_expenses, 1)
    assert len(all_expenses) == 4

def test_remove_type():
    """
    Test the remove_type function
    :return:
    """
    all_expenses = []
    add_expense(all_expenses, 1, "water", 100)
    add_expense(all_expenses, 2, "heating", 200)
    add_expense(all_expenses, 3, "electricity", 300)
    add_expense(all_expenses, 4, "gas", 400)
    add_expense(all_expenses, 5, "other", 500)
    assert len(all_expenses) == 5
    remove_type(all_expenses, "water")
    assert len(all_expenses) == 4
    assert all_expenses[0]['Apartament'] == 2
    assert all_expenses[0]['Type'] == "heating"
    assert all_expenses[0]['Amount'] == 200
    assert all_expenses[1]['Apartament'] == 3
    assert all_expenses[1]['Type'] == "electricity"
    assert all_expenses[1]['Amount'] == 300
    assert all_expenses[2]['Apartament'] == 4
    assert all_expenses[2]['Type'] == "gas"
    assert all_expenses[2]['Amount'] == 400
    assert all_expenses[3]['Apartament'] == 5
    assert all_expenses[3]['Type'] == "other"
    assert all_expenses[3]['Amount'] == 500
    remove_type(all_expenses, "heating")
    assert len(all_expenses) == 3
    assert all_expenses[0]['Apartament'] == 3
    assert all_expenses[0]['Type'] == "electricity"
    assert all_expenses[0]['Amount'] == 300
    assert all_expenses[1]['Apartament'] == 4
    assert all_expenses[1]['Type'] == "gas"
    assert all_expenses[1]['Amount'] == 400
    assert all_expenses[2]['Apartament'] == 5
    assert all_expenses[2]['Type'] == "other"
    assert all_expenses[2]['Amount'] == 500
    remove_type(all_expenses, "electricity")
    assert len(all_expenses) == 2
    assert all_expenses[0]['Apartament']

def test_remove_expenses_between_apartaments():
    """
    Test the remove_expenses_between_apartaments function
    :return:
    """
    all_expenses = []
    add_expense(all_expenses, 1, "water", 100)
    add_expense(all_expenses, 2, "heating", 200)
    add_expense(all_expenses, 3, "electricity", 300)
    add_expense(all_expenses, 4, "gas", 400)
    add_expense(all_expenses, 5, "other", 500)
    assert len(all_expenses) == 5
    remove_apartaments_between(all_expenses, 1, 3)
    assert len(all_expenses) == 3

def test_replace():
    """
    Test the replace function
    :return:
    """
    all_expenses = []
    add_expense(all_expenses, 1, "water", 100)
    add_expense(all_expenses, 2, "heating", 200)
    add_expense(all_expenses, 3, "electricity", 300)
    add_expense(all_expenses, 4, "gas", 400)
    add_expense(all_expenses, 5, "other", 500)
    assert len(all_expenses) == 5
    replace(all_expenses, 1, "water", 1000)
    assert len(all_expenses) == 5
    assert all_expenses[0]['Apartament'] == 1
    assert all_expenses[0]['Type'] == "water"
    assert all_expenses[0]['Amount'] == 1000
    assert all_expenses[1]['Apartament'] == 2
    assert all_expenses[1]['Type'] == "heating"
    assert all_expenses[1]['Amount'] == 200
    assert all_expenses[2]['Apartament'] == 3
    assert all_expenses[2]['Type'] == "electricity"
    assert all_expenses[2]['Amount'] == 300
    assert all_expenses[3]['Apartament'] == 4
    assert all_expenses[3]['Type'] == "gas"
    assert all_expenses[3]['Amount'] == 400
    assert all_expenses[4]['Apartament'] == 5
    assert all_expenses[4]['Type'] == "other"
    assert all_expenses[4]['Amount'] == 500
    replace(all_expenses, 2, "heating", 2000)
    assert len(all_expenses) == 5

def run_tests():
    """
    Run all tests
    :return:
    """
    test_add_expense()
    test_remove_type()
    test_remove_expenses_between_apartaments()
    test_replace()
    print("All tests passed")

run_tests()