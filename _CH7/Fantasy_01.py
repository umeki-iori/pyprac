def display_inventory(inventory):
    amount_items = 0
    print('持ち物リスト:')
    for k, v in inventory.items():
        print(f'{v:<4} :  {k}')
        amount_items += v
    print(f'アイテムの総数: {amount_items}')

def add_to_inventory(inventory, added_items):
    drop_list = {}
    for drop_item in added_items:
        inventory.setdefault(drop_item, 0)
        drop_list.setdefault(drop_item, 0)
        inventory[drop_item] += 1
        drop_list[drop_item] += 1
    amount_dropitem = 0
    print('獲得したアイテム:')
    for k, v in drop_list.items():
        print(f'{k:<8} : {v}')
    print('')
    display_inventory(inventory)


player_item = {'ロープ': 1024, 'たいまつ': 6, '金貨': 42, '手裏剣': 1,'ルビー': 11, '矢': 12}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー', 'ゴリラ']

display_inventory(player_item)
print('')
add_to_inventory(player_item, dragon_loot)
