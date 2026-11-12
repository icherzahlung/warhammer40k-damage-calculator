print("Warhammer 40k Damage Calculator")

attacks = int(input("Attacks: "))
hit = int(input("Hit roll (e.g. 3 for 3+): "))
strength = int(input("Strength: "))
toughness = int(input("Target Toughness: "))
save = int(input("Target Save (e.g. 3 for 3+): "))
ap = int(input("AP (e.g. -1): "))
damage = int(input("Damage per wound: "))

# Шанс попадания
hit_chance = (7 - hit) / 6

# Шанс ранения
if strength >= toughness * 2:
    wound_chance = 5 / 6
elif strength > toughness:
    wound_chance = 4 / 6
elif strength == toughness:
    wound_chance = 3 / 6
elif strength * 2 <= toughness:
    wound_chance = 1 / 6
else:
    wound_chance = 2 / 6

# Спасбросок после AP
modified_save = save - ap

if modified_save > 6:
    failed_save_chance = 1
else:
    save_chance = (7 - modified_save) / 6
    failed_save_chance = 1 - save_chance

expected_damage = (
    attacks
    * hit_chance
    * wound_chance
    * failed_save_chance
    * damage
)

print(f"\nExpected damage: {expected_damage:.2f}")
