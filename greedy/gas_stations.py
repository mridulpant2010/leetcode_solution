
def gas_stations(gas,cost):
    start_index=0
    current_gas=0    
    total_gas = sum(gas)
    total_cost = sum(cost)
    if total_gas<total_cost:
        return -1
    
    for i in range(len(gas)):
        current_gas+=gas[i]-cost[i]
        if current_gas<0:
            start_index=i+1
            current_gas=0
    return start_index

if __name__ == "__main__":
    gas = [1,
        