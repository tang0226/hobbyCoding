import time
start = time.time()
def numberOfWays(n,coins):   
    table = [0] *(n+1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, n+1): 
            table[i] += table[i-coin]            
    return table

coins = [1,2,5,10,20,50,100,200] 

table = [0] *(201)
table[0] = 1
for coin in coins:
    for i in range(coin, 201):
        table[i] += table[i-coin]       
    print(coin,table)


#print(numberOfWays(200,coins))
print(table)
end = time.time() - start
print(end)
