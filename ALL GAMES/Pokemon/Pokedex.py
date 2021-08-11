import pypokedex

while True:

    print("Please Type In a Pokemon : ")
    pokename = input()

    p = pypokedex.get(name=pokename)

    print('Name - '+p.name)
    print(f'dex - {p.dex}')

    print(f'HP - {p.base_stats.hp}')
    print(f'Attack - {p.base_stats.attack}')
    print(f'Defense - {p.base_stats.defense}')
    print(f'Special Attack - {p.base_stats.sp_atk}')
    print(f'Special Defense - {p.base_stats.sp_def}')

    print(f'Height - {p.height*10}')
    print(f'Weight - {p.weight/10}')

    print(f'Types - {p.types}')
