import json
bank = {
        'users' : [ 'ram', 'rishav', 'hari' ],
        'acc_no' : [ 1001, 1002, 1003 ],
        'bal' : [ 10000, 20000, 35000 ],
        'password' : [ 'redhat', 'python', 'aws' ],
        }

f = open('bank.db','w+')
        json.dump(bank,f)
        f.close
