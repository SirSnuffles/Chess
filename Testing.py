def insert(result, key, price, quantity):
    priceDict = result.get(key, {price: 0})
    if price not in priceDict:
    	result[key].update({price:quantity})
    	return result
    priceDict[price] += quantity
    result[key] = priceDict
    return result

def remove(result, key, price, quantity):
	priceDict = result.get(key, {price:0})
	if price not in priceDict:
		print("no offer availible!")
		return
	print(priceDict[price], quantity)
	if priceDict[price] < quantity:
		print("Error, not enough availible")
		return
	elif priceDict[price] == quantity:

		del result[key][price]
		return result
	priceDict[price] -= quantity
	result[key] = priceDict
	return result

result = {}
print(result) # {}
insert(result, "Foo", 1010, 10101010)
insert(result, "Bar", 0, 1)
insert(result, "Foo", 10101, 12)
insert(result, "Foo", 10101, 12)
insert(result, "Foo", 1010, 5)
insert(result, "Foo1", 1010, 5)
insert(result, "Foo1", 1010, 5)
insert(result, "Foo1", 102, 5)
print(result) # {'Foo': {1010: 10101015}, 'Bar': {0: 1}}
remove(result, "Foo1", 1022, 5)
# remove(result, "Foo1", 102, 5)
remove(result, "Foo", 10101, 6)
print(result)