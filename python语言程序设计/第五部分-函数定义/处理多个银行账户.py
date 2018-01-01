def addInterest(balances,rate):
    for i in range(len(balances)):
        balances[i] = balances[i]*(1+rate)
    return balances
def test():
    amounts = [2000,100,3500,745]
    rate = 0.05
    amounts = addInterest(amounts,rate)
    print(amounts)
test()