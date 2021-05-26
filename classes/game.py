import math
import random


def get_xp_strings(xp, max_xp):
    xp_string = str(xp) + "/" + str(max_xp)
    current_xp = ""
    xp_length = len(str(max_xp)) * 2 + 1

    if len(xp_string) < xp_length:
        decreased = xp_length - len(xp_string)

        while decreased > 0:
            current_xp += " "
            decreased -= 1

        current_xp += xp_string

    else:
        current_xp = xp_string

    return current_xp


def clear_name(name):
    checked_name = ""
    for c in name:
        if c != '_':
            checked_name += c
        else:
            checked_name += ' '
    return checked_name


def savable_string(string):
    final_string = ""
    for c in string:
        if c != ' ':
            final_string += c
        else:
            final_string += '_'
    return final_string


def tokenize(string):
    tokenized = string.split()
    return tokenized


def is_number(param_to_check):
    i = 0
    chars = list(param_to_check)

    for char in chars:
        if i == 0 and char == '-' and len(param_to_check) > 1:
            i += 1
        elif not char.isdigit():
            return False
        i += 1

    return True


def check_data_items(line_to_check):
    item_types = {"healing", "mana", "elixir", "attack"}
    tempo = tokenize(line_to_check)

    if len(tempo) != 5:
        return -1, "Data", "There should be only 4 fields of data"

    is_type_correct = False

    for t in item_types:
        if tempo[1] == t:
            is_type_correct = True

    if not is_type_correct:
        return -1, "Type", tempo[1]

    if not tempo[2].isdigit():
        return -1, "Value", tempo[2]

    if not tempo[3].isdigit():
        return -1, "Quantity", tempo[3]

    if not (tempo[4] == "Yes" or tempo[4] == "No"):
        return -1, "AOE", tempo[4]

    if tempo[4] == "Yes":
        return tempo[0], tempo[1], int(tempo[2]), int(tempo[3]), True

    return tempo[0], tempo[1], int(tempo[2]), int(tempo[3]), False


def check_data_spells(line_to_check):
    spell_natures = {"light", "fire", "lightning", "force", "ice", "water", "earth", "utility", "black"}
    tempo = tokenize(line_to_check)

    if len(tempo) != 5:
        return -1, "Data", "There should be only 4 fields of data"

    is_nature_correct = False

    for n in spell_natures:
        if tempo[3] == n:
            is_nature_correct = True

    if not tempo[1].isdigit():
        return -1, "Mana", tempo[1]

    if not tempo[2].isdigit():
        return -1, "Damage", tempo[2]

    if not is_nature_correct:
        return -1, "Nature", tempo[3]

    if not (tempo[4] == "Yes" or tempo[4] == "No"):
        return -1, "AOE", tempo[4]

    if tempo[4] == "Yes":
        return tempo[0], int(tempo[1]), int(tempo[2]), tempo[3], True

    return tempo[0], int(tempo[1]), int(tempo[2]), tempo[3], False


def check_data_monsters(line_to_check):
    species = {"Goblin", "Beast", "Undead"}
    tempo = tokenize(line_to_check)

    if len(tempo) != 6:
        return -1, "Data", "There should be only 4 fields of data"

    is_species_correct = False

    for s in species:
        if tempo[5] == s:
            is_species_correct = True

    if not tempo[1].isdigit():
        return -1, "HP", tempo[1]

    if not tempo[2].isdigit():
        return -1, "Attack", tempo[2]

    if not tempo[3].isdigit():
        return -1, "Defense", tempo[3]

    if not tempo[4].isdigit():
        return -1, "XP", tempo[4]

    if not is_species_correct:
        return -1, "Species", tempo[5]

    return tempo[0], int(tempo[1]), int(tempo[2]), int(tempo[3]), int(tempo[4]), tempo[5]


def load_data():
    file_items = open("dataToLoad/availableData/Items.txt", 'r', encoding='utf-8')
    all_items = []
    count = 0
    for line in file_items:
        count += 1
        if not count == 1:
            check = check_data_items(line)
            if check[0] != -1:
                new_item = Item(check[0], check[1], check[2], check[4])
                all_items.append({"item": new_item, "quantity": check[3]})
            else:
                print("Line: " + str(count) + "\tIncorrect " + str(check[1]) + ": " + str(check[2]))
    file_items.close()

    file_spells = open("dataToLoad/availableData/Magic.txt", 'r', encoding='utf-8')
    all_spells = []
    count = 0
    for line in file_spells:
        count += 1
        if not count == 1:
            check = check_data_spells(line)
            if check[0] != -1:
                new_spell = Spell(check[0], check[1], check[2], check[3], check[4])
                all_spells.append(new_spell)
            else:
                print("Line: " + str(count) + "\tIncorrect " + str(check[1]) + ": " + str(check[2]))
    file_spells.close()

    file_monsters = open("dataToLoad/availableData/Monsters.txt", 'r', encoding='utf-8')
    all_monsters = []
    count = 0
    for line in file_monsters:
        count += 1
        if not count == 1:
            check = check_data_monsters(line)
            if check[0] != -1:
                new_monster = Monster(check[0], check[1], check[2], check[3], check[4], check[5])
                all_monsters.append(new_monster)
            else:
                print("Line: " + str(count) + "\tIncorrect " + str(check[1]) + ": " + str(check[2]))
    file_monsters.close()

    return all_items, all_spells, all_monsters


def monsters_attack(players, enemies):
    report = "\n"
    for foe in enemies:
        if foe.get_hp() > 0:
            damage = foe.get_damage()
            while True:
                choice_target = random.randrange(0, len(players))
                defender = players[choice_target]
                if defender.get_hp() > 0:
                    break
            defender.take_damage(damage)
            report += foe.name + " dealt " + str(damage) + " force damage to " + defender.name + "\n"
        else:
            report += "Due to " + foe.name + "'s death, he is unable to move.\n"

    return report


class Person:
    def __init__(self, name, hp, mp, attack, defense, ap, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.magic = []
        self.ap = ap
        self.items = items

    def get_attack_damage(self):
        return random.randrange(math.ceil(self.attack * 0.5), math.ceil(self.attack * 1.5))

    def get_spell_damage(self, spell):
        return spell.spell_damage() * self.ap

    def take_damage(self, damage):
        self.hp -= math.ceil(damage - self.defense)
        if self.hp < 0:
            self.hp = 0
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def restore_mp(self, amount):
        self.mp += amount
        if self.mp > self.max_mp:
            self.mp = self.max_mp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def take_mana(self, cost):
        self.mp -= cost
        if self.get_mp() < 0:
            self.mp = 0

    def set_spell_book(self, spells):
        self.magic = spells

    def spells_toString(self):
        i = 1
        string_spells = "Spells:"

        for spell in self.magic:
            string_spells += "\n" + str(i) + ":\t" + str(spell.name) + "\tvalue: " + str(spell.damage) + \
                             "\tcost: " + str(spell.cost)
            i += 1

        return string_spells

    def generate_spell_book(self, list_spells):
        num = math.ceil(len(list_spells) * self.ap)
        self.magic = random.sample(list_spells, num)

    def items_toString(self):
        i = 1
        string_items = "Items:"

        for item in self.items:
            string_items += "\n" + str(i) + ":\t" + str(item["item"].name) + " - " + str(item["item"].description) \
                            + "(x" + str(item["quantity"]) + ")"
            i += 1

        return string_items

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4
        current_hp = get_xp_strings(self.hp, self.max_hp)

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = f""
        current_mp = get_xp_strings(self.mp, self.max_mp)

        if self.max_mp > 0:
            bar_ticks = (self.mp / self.max_mp) * 100 / 10

        else:
            bar_ticks = 10

        while bar_ticks > 0:
            mp_bar += "█"
            bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        return self.name, current_hp, hp_bar, current_mp, mp_bar

    def save_player(self):
        res = "Player: " + savable_string(self.name) + "\t" + str(self.max_hp) + "\t" + str(self.hp) + "\t" + \
              str(self.max_mp) + "\t" + str(self.mp) + "\t" + str(self.attack) + "\t" + str(self.defense) + "\t" \
              + str(self.ap)
        for spell in self.magic:
            res += "\n" + savable_string(spell.name) + "\t" + str(spell.cost) + "\t" + str(spell.damage) + "\t" + \
                   spell.nature + "\t" + str(spell.aoe)
        return res


class Monster:
    def __init__(self, name, hp, attack, defense, lvl, species):
        self.name = clear_name(name)
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.lvl = lvl
        self.species = species

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_lvl(self):
        return self.lvl

    def get_damage(self):
        return random.randrange(math.ceil(self.attack * 0.5), math.ceil(self.attack * 1.5))

    def take_damage(self, dmg, dmg_type):
        damage = (dmg - self.defense)

        if damage < 0:
            damage = 0

        if dmg_type == "fire" and self.lvl == "Beast":
            damage += damage

        if dmg_type == "force" and self.lvl == "Undead":
            damage += damage

        if dmg_type == "lightning" and self.lvl == "Goblin":
            damage += damage
        self.hp -= math.ceil(damage)
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2
        current_hp = get_xp_strings(self.hp, self.max_hp)

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "
        return self.name, current_hp, hp_bar

    def save_monster(self):
        res = "Monster: " + savable_string(self.name) + "\t" + str(self.max_hp) + "\t" + str(self.hp) + "\t" + \
              str(self.attack) + "\t" + str(self.defense) + "\t" + str(self.lvl) + "\t" + self.species
        return res


class Spell:
    def __init__(self, name, cost, damage, nature, is_aoe):
        self.name = clear_name(name)
        self.cost = cost
        self.damage = damage
        self.nature = nature
        self.aoe = is_aoe

    def spell_damage(self):
        return random.randrange(math.ceil(self.damage * 0.9), math.ceil(self.damage * 1.1))


class Item:
    def __init__(self, name, category, prop, is_aoe):
        self.name = clear_name(name)
        self.category = category
        self.prop = prop
        self.description = self.create_description()
        self.aoe = is_aoe

    def create_description(self):
        cat = self.category
        if cat == "healing":
            desc = "Heals for " + str(self.prop)
            return desc

        elif cat == "mana":
            desc = "Regain " + str(self.prop) + " mana"
            return desc

        elif cat == "elixir":
            desc = "Restore " + str(self.prop) + " hp and mp"
            return desc

        elif cat == "attack":
            desc = "Deals " + str(self.prop) + " damage"
            return desc

    def save_item(self):
        res = "Item: " + savable_string(self.name) + "\t" + self.category + "\t" + str(self.prop) + "\t" + str(self.aoe)
        return res
