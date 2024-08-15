alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']


def affair_meet(bob, alice, silvester):
    affair = []
    for i in alice:
        for j in silvester:
            for k in bob:
                if (i == j and i != k) and (i == j and j != k):
                    affair.append(i)
                if j == k or i == k:
                    affair.remove(k)              
    return set(affair)
