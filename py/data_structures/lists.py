
shop_list = ['apple', 'mango', 'carrot', 'banana']
print('I have {0} items to purchase.'.format(len(shop_list)))
print('These items are: ')
for item in shop_list:
    print('\t' + item)

print('I also have to buy rice.')
shop_list.append('rice')
print('sort it now: ')
shop_list.sort()
print('Sorted list: {0}'.format(shop_list))
print('sort it in another day: ')
shop_list.sort(key=lambda item: item[1])
print(shop_list)

shop_list.sort(key=lambda item: len(item), reverse=True)
print(shop_list)

