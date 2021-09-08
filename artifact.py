import random

MAIN_STAT_VALUES = {
    "HP": [717, 920, 1123, 1326, 1530, 1733, 1936, 2139, 2342, 2545, 2749, 2952, 3155, 3358, 3561, 3764, 3967, 4171, 4374, 4577, 4780],
    "ATK": [47, 60, 73, 86, 100, 113, 126, 139, 152, 166, 179, 192, 205, 219, 232, 245, 258, 272, 285, 298, 311],
    "HP%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],
    "ATK%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],
    "DEF%": [8.7, 11.2, 13.7, 16.2, 18.6, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8, 53.3, 55.8, 58.3],
    "Physical DMG Bonus%": [8.7, 11.2, 13.7, 16.2, 16.2, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8, 53.3, 55.8, 58.3],
    "Elemental DMG Bonus%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],
    "Elemental Mastery": [28, 36, 44, 52, 60, 68, 76, 84, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179, 187],
    "Energy Recharge%": [.8, 10.0, 12.2, 14.4, 16.6, 18.8, 21.0, 23.2, 25.4, 27.6, 29.8, 32.0, 34.2, 36.4, 38.6, 40.8, 43.0, 45.2, 47.4, 49.6, 51.8],
    "Crit Rate%": [4.7, 6.0, 7.4, 8.7, 10.0, 11.4, 12.7, 14.0, 15.4, 16.7, 18.0, 19.3, 20.7, 22.0, 23.3, 24.7, 26.0, 27.3, 28.7, 30.0, 31.1],
    "Crit DMG%": [9.3, 11.9, 14.6, 17.2, 19.9, 22.5, 25.2, 27.8, 30.5, 33.1, 35.8, 38.4, 41.1, 43.7, 46.3, 49.0, 51.6, 54.3, 56.9, 59.6, 62.2],
    "Healing Bonus%": [5.4, 6.9, 8.4, 10.0, 11.5, 13.0, 14.5, 16.1, 17.6, 19.1, 20.6, 22.2, 23.7, 25.2, 26.7, 28.3, 29.8, 31.3, 32.8, 34.4, 35.9],
}

SANDS_MAIN_STAT = (("HP%", 0.2668), ("ATK%", 0.5334), ("DEF%", 0.8), ("Energy Recharge%", 0.9), ("Elemental Mastery", 1))
GOBLET_MAIN_STAT = (("HP%", 0.2125), ("ATK%", 0.425), ("DEF%", 0.625), ("Elemental Mastery", 0.65), 
                    ("Pyro DMG Bonus%", 0.70), ("Electro DMG Bonus%", 0.75), ("Cyro DMG Bonus%", 0.80), ("Hydro DMG Bonus%", 0.85), 
                    ("Anemo DMG Bonus%", 0.90), ("Geo DMG Bonus%", 0.95), ("Physical DMG Bonus%", 1))
CIRCLET_MAIN_STAT = (("HP%", 0.22), ("ATK%", 0.44), ("DEF%", 0.66), ("Crit Rate%", 0.76), ("Crit DMG%", 0.86), ("Healing Bonus%", 0.96), ("Elemental Mastery", 1))

SUB_STATS_VALUES = {
    "HP": [209.13, 239.00, 268.88, 298.75],
    "ATK": [13.62, 15.56, 17.51, 19.45],
    "DEF": [16.20, 18.52, 20.83, 23.15],
    "HP%": [4.08, 4.66, 5.25, 5.83],
    "ATK%": [4.08, 4.66, 5.25, 5.83],
    "DEF%": [5.10, 5.83, 6.56, 7.29],
    "Elemental Mastery": [16.32, 18.65, 20.98, 23.31],
    "Energy Recharge%": [4.53, 5.18, 5.83, 6.48],
    "Crit Rate%": [2.72, 3.11, 3.50, 3.89],
    "Crit DMG%": [5.44, 6.22, 6.99, 7.77], 
}

class Artifact(object):
    def __init__(self, type, level):
        self.type = type
        self.level = level
        self.get_main_stat(type, int(level))
        self.get_sub_stats(type, int(level))

    def get_main_stat(self, type, level):
        if type == "flower":
            self.main_stat = ("HP", MAIN_STAT_VALUES["HP"][level])
        elif type == "plume":
            self.main_stat = ("ATK", MAIN_STAT_VALUES["ATK"][level])
        elif type == "sands":
            rand = random.random()
            for i in range(len(SANDS_MAIN_STAT)):
                if rand < SANDS_MAIN_STAT[i][1]:
                    main_stat = SANDS_MAIN_STAT[i][0]
                    break
            self.main_stat = (main_stat, MAIN_STAT_VALUES[main_stat][level])
        elif type == "goblet":
            rand = random.random()
            for i in range(len(GOBLET_MAIN_STAT)):
                if rand < GOBLET_MAIN_STAT[i][1]:
                    main_stat = GOBLET_MAIN_STAT[i][0]
                    break
            if main_stat not in ["HP%", "ATK%", "DEF%", "Elemental Mastery", "Physical DMG Bonus%"]:
                key = "Elemental DMG Bonus%"
            else:
                key = main_stat
            self.main_stat = (main_stat, MAIN_STAT_VALUES[key][level])
        else:
            rand = random.random()
            for i in range(len(CIRCLET_MAIN_STAT)):
                if rand < CIRCLET_MAIN_STAT[i][1]:
                    main_stat = CIRCLET_MAIN_STAT[i][0]
                    break
            self.main_stat = (main_stat, MAIN_STAT_VALUES[main_stat][level])

    def get_sub_stats(self, type, level):
        self.sub_stats = {}
        rand = random.random()
        subs_stats_num = 4 if rand < 0.2 else 3
        if type == "flower" or type == "plume":
            sub_stats = (("ATK" if type == "flower" else "HP", 0.1579), ("DEF", 0.3518), ("HP%", 0.4211), ("ATK%", 0.5264), ("DEF%", 0.6317), 
                        ("Energy Recharge%", 0.737), ("Elemental Mastery", 0.8423), ("Crit Rate%", 0.9212), ("Crit DMG%", 1))
        else:
            if self.main_stat == "Energy Recharge%":
                sub_stats = (("HP", 0.15), ("ATK", 0.30), ("DEF", 0.45), ("HP%", 0.55), ("ATK%", 0.65), ("DEF%", 0.75), 
                        ("Elemental Mastery", 0.85), 
                        ("Crit Rate%", 0.925), ("Crit DMG%", 1))
            elif self.main_stat[0].endswith("DMG Bonus%") or self.main_stat[0] == "Healing Bonus%":
                sub_stats = (("HP", 0.1364), ("ATK", 0.2728), ("DEF", 0.4092), ("HP%", 0.5001), ("ATK%", 0.591), ("DEF%", 0.6819), 
                        ("Energy Recharge%", 0.7728), ("Elemental Mastery", 0.8637), ("Crit Rate%", 0.9319), ("Crit DMG%", 1))
            elif self.main_stat[0].startswith("Crit"):
                sub_stats = (("HP", 0.1463), ("ATK", 0.2926), ("DEF", 0.4389), ("HP%", 0.5365), ("ATK%", 0.6341), ("DEF%", 0.7371), 
                        ("Energy Recharge%", 0.8293), ("Elemental Mastery", 0.9269), 
                        ("Crit Rate%" if self.main_stat[0] == "Crit DMG%" else "Crit DMG%", 1))
            else:
                sub_stats = (("HP", 0.15), ("ATK", 0.30), ("DEF", 0.45), ("ATK%" if self.main_stat[0] == "HP%" else "HP%", 0.55), 
                            ("DEF%" if self.main_stat[0] == "ATK%" else "ATK%", 0.65), 
                            ("Energy Recharge%", 0.75), 
                            ("Elemental Mastery" if self.main_stat[0] == "DEF%" else "DEF%", 0.85), 
                            ("Crit Rate%", 0.925), ("Crit DMG%", 1))
        for i in range(subs_stats_num):
            found = False
            while not found:
                rand = random.random()
                for j in range(len(sub_stats)):
                    if rand < sub_stats[j][1]:
                        if sub_stats[j][0] not in self.sub_stats.keys():
                            self.sub_stats[sub_stats[j][0]] = random.choice(SUB_STATS_VALUES[sub_stats[j][0]])
                            found = True
                        break
        if level >= 4:
            if subs_stats_num == 3:
                found = False
                while not found:
                    rand = random.random()
                    for j in range(len(sub_stats)):
                        if rand < sub_stats[j][1]:
                            if sub_stats[j][0] not in self.sub_stats.keys():
                                self.sub_stats[sub_stats[j][0]] = random.choice(SUB_STATS_VALUES[sub_stats[j][0]])
                                found = True
                            break
            else:
                upgrade_stat = random.choice(list(self.sub_stats.keys()))
                self.sub_stats[upgrade_stat] += random.choice(SUB_STATS_VALUES[upgrade_stat])
        if level >= 8:
                upgrade_stat = random.choice(list(self.sub_stats.keys()))
                self.sub_stats[upgrade_stat] += random.choice(SUB_STATS_VALUES[upgrade_stat])
        if level >= 12:
                upgrade_stat = random.choice(list(self.sub_stats.keys()))
                self.sub_stats[upgrade_stat] += random.choice(SUB_STATS_VALUES[upgrade_stat])
        if level >= 16:
                upgrade_stat = random.choice(list(self.sub_stats.keys()))
                self.sub_stats[upgrade_stat] += random.choice(SUB_STATS_VALUES[upgrade_stat])
        if level == 20:
                upgrade_stat = random.choice(list(self.sub_stats.keys()))
                self.sub_stats[upgrade_stat] += random.choice(SUB_STATS_VALUES[upgrade_stat])

    def get_info(self):
        output = [self.type.upper() + " +" + str(self.level)]
        output.append(self.main_stat[0] + " +" + str(self.main_stat[1]))
        for key, value in self.sub_stats.items():
            output.append("    " + key + " +" + str(round(value, 2)))
            if key.endswith("%"):
                output[-1] += "%"
        return output