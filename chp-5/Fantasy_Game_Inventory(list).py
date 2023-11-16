def addToInventory(inv, addedItems):
    for item in addedItems:
        inv.setdefault(item, 0)
        inv[item] += 1
    return inv  

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inv, dragonLoot)
print(inventory) 
