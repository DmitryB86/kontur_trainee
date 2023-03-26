import random


def building_number_generator(already_placed):
    new_number = 1
    while True:
        while new_number in already_placed:
            new_number += 1
        yield new_number
        already_placed.add(new_number)


def split_address(address_str: str):
    street_name = address_str.rstrip('0123456789')
    building_number = int(address_str[len(street_name):])
    return street_name, building_number


def fill_planted_buildings(planted_buildings, addresses):
    for adr in addresses:
        street_name, building_number = split_address(adr)
        buildings = planted_buildings.setdefault(street_name, set())
        buildings.add(building_number)


def generator_assigment(planted_buildings):
    street_to_generator = {}
    for address, buildings in planted_buildings.items():
        street_to_generator[address] = building_number_generator(buildings)
    return street_to_generator


def do_work(in_streets, street_to_buildings):
    for address in in_streets:
        number_generator = street_to_buildings.setdefault(address, building_number_generator(set()))
        print(next(number_generator))


def main(day_1, streets):
    planted_buildings = {}
    fill_planted_buildings(planted_buildings, day_1)
    street_generators = generator_assigment(planted_buildings)
    do_work(streets, street_generators)


if __name__ == '__main__':
    n = int(input())
    day_1 = []
    for _ in range(n):
        day_1.append(input())
    m = int(input())
    streets_to_plant = []
    for _ in range(m):
        streets_to_plant.append(input())
    main(day_1, streets_to_plant)

    day_1 = (
        'mira1', 'mira32', 'lenina5', 'mira2', 'tver3', 'mira12', 'mira33', 'lenina15', 'mira21', 'tver33',
        'mira81', 'mira832', 'lenina85', 'mira82', 'tver83', 'mira812', 'mira833', 'lenina815', 'mira821', 'tver833',
        'mira91', 'mira932', 'lenina95', 'mira92', 'tver93', 'mira912', 'mira933', 'lenina915', 'mira921', 'tver933',
         'tvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertve98999',
        'tvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertve9',
        'tvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertve91',
        'tvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertvertve99',
    )

    streets = (
        'mira', 'mara', 'lenina', 'bakunina', 'tver', 'kim', 'mira', 'mara', 'lenina', 'orlova', 'petrova', 'sokolova',
        'ivanova', 'golubeva', 'polozova', 'vano', 'golub', 'poloz', 'main', 'train', 'strob'
    )
    streets_to_plant = (random.choice(streets) for _ in range(1_000_000))

    day_1 = ('mira32', 'turgeneva4', 'mira1')
    streets_to_plant = ('mira', 'turgeneva',  'turgeneva', 'turgeneva', 'turgeneva', 'lenina')

    main(day_1, streets_to_plant)
