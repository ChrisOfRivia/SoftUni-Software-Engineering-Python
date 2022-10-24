n = int(input())

heroes = {}

for hero in range(n):
    information = input().split(' ')
    name = information[0]
    hp = int(information[1])
    mana = int(information[2])

    if hp > 100:
        hp = 100
    if mana > 200:
        mana = 200

    heroes[name] = [hp]
    heroes[name].append(mana)

while True:
    command = input().split(' - ')
    action = command[0]
    if action == 'End':
        for player, info in heroes.items():
            print(f'{player}')
            print(f'  HP: {info[0]}')
            print(f'  MP: {info[1]}')
        break

    elif action == 'CastSpell':
        hero_cast_spell = command[1]
        mana_needed_cast_spell = int(command[2])
        spell_name = command[3]
        if heroes[hero_cast_spell][1] >= mana_needed_cast_spell:
            heroes[hero_cast_spell][1] -= mana_needed_cast_spell
            print(f'{hero_cast_spell} has successfully cast {spell_name} and now has {heroes[hero_cast_spell][1]} MP!')
        else:
            print(f'{hero_cast_spell} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        hero_take_dmg = command[1]
        damage = int(command[2])
        attacker = command[3]

        if (heroes[hero_take_dmg][0] - damage) > 0:
            heroes[hero_take_dmg][0] -= damage
            print(f'{hero_take_dmg} was hit for {damage} HP by {attacker} and now has {heroes[hero_take_dmg][0]} HP left!')
        else:
            print(f'{hero_take_dmg} has been killed by {attacker}!')
            del heroes[hero_take_dmg]

    elif action == 'Recharge':
        hero_recharge = command[1]
        amount_recharge = int(command[2])
        amount_recharged = 0

        if (heroes[hero_recharge][1] + amount_recharge) > 200:
            while heroes[hero_recharge][1] < 200:
                heroes[hero_recharge][1] += 1
                amount_recharged += 1
            print(f'{hero_recharge} recharged for {amount_recharged} MP!')

        else:
            heroes[hero_recharge][1] += amount_recharge
            print(f'{hero_recharge} recharged for {amount_recharge} MP!')

    elif action == 'Heal':
        hero_heal = command[1]
        amount_heal = int(command[2])
        amount_healed = 0

        if (heroes[hero_heal][0] + amount_heal) > 100:
            while heroes[hero_heal][0] < 100:
                heroes[hero_heal][0] += 1
                amount_healed += 1
            print(f'{hero_heal} healed for {amount_healed} HP!')

        else:
            heroes[hero_heal][0] += amount_heal
            print(f'{hero_heal} healed for {amount_heal} HP!')

