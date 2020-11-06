import user.authentication
import transactions.journal
import banking
import sys

def print_all_args():
    for x in sys.argv[1:]:
        print(x)

if __name__ == "__main__":
    print_all_args()
    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    banking.fvb.reconciliation.do_reconciliation()