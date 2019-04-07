#  Logical operators in python AND, OR, NOT
has_high_income = True
has_good_credit = True
has_criminal_record = True
if has_good_credit and has_high_income and not has_criminal_record:
    print("Eligible for full loan")
elif has_high_income or has_good_credit:
    print("Eligible for half loan")
