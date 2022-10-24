animals_dict = {}

keep_track_of_areas = {}

while True:
    command = input().split('-')
    action = command[0]
    if action == 'EndDay':
        print(f'Animals:')
        for animal, food_area in animals_dict.items():
            print(f' {animal} -> {food_area[0]}g')
        print(f'Areas with hungry animals:')
        for area, num_animals in keep_track_of_areas.items():
            if len(num_animals) != 0:
                print(f'{area}: {len(num_animals)}')
        break

    elif action[:4:] == 'Add:':
        animal_already_in = False
        animal_name_add = action[5::]
        needed_food_quantity_add = int(command[1])
        area_add = command[2]
        if animal_name_add not in animals_dict.keys():
            animals_dict[animal_name_add] = [needed_food_quantity_add]
            animals_dict[animal_name_add].append(area_add)
        else:
            animals_dict[animal_name_add][0] += needed_food_quantity_add
            animal_already_in = True

        if area_add not in keep_track_of_areas:
            keep_track_of_areas[area_add] = [animal_name_add]

        elif area_add in keep_track_of_areas and not animal_already_in:
            keep_track_of_areas[area_add].append(animal_name_add)


    elif action[:5:] == 'Feed:':
        animal_name_feed = action[6::]
        food_feed = int(command[1])
        if animal_name_feed in animals_dict.keys():
            animals_dict[animal_name_feed][0] -= food_feed
        else:
            continue
        if animals_dict[animal_name_feed][0] <= 0:
            print(f'{animal_name_feed} was successfully fed')
            for key, value in keep_track_of_areas.items():
                if animal_name_feed in value:
                    value.remove(animal_name_feed)
            del animals_dict[animal_name_feed]
