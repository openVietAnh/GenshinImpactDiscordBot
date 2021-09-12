from datetime import datetime

class Domain(object):
    def __init__(self):
        self.talent = {
            0: {
                "Freedom": ("Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Childe", "Main Phong"),
                "Prosperity": ("Keqing", "Ningguang", "Qiqi", "Main Nham", "Xiao"),
                "Transience": ("Main Lôi", "Yoimiya")
            },
            1: {
                "Resistance": ("Bennett", "Dilluc", "Eula", "Jean", "Mona", "Noelle", "Razor"),
                "Diligence": ("Chongyun", "Ganyu", "Hu Tao", "Kazuha", "Xiangling"),
                "Elegance": ("Ayaka", "Sara")
            },
            2: {
                "Ballad": ("Albedo", "Fischl", "Kaeya", "Lisa", "Rosaria", "Venti"),
                "Gold": ("Beidou", "Xingqiu", "Xinyan", "Yanfei", "Zhongli"),
                "Light": ("Raiden Shogun", "Sajuu")
            }
        }
        self.talent[3], self.talent[4], self.talent[5] = self.talent[0], self.talent[1], self.talent[2]
        
        self.weapon = {
            0: {
                "Decarabian": (""),
                "Guyun": (""),
                "Distant Sea": (""),
            },
            1: {
                "Boreal Wolf": (""),
                "Mist Veiled Elixir": (""),
                "Narukami": ("")
            },
            2: {
                "Dandelion Glaidator": (""),
                "Aerosiderite": (""),
                "Mask": ("")
            }
        }
        self.weapon[3], self.weapon[4], self.weapon[5] = self.weapon[0], self.weapon[1], self.weapon[2]

    def get_output(self, type):
        weekDays = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ Nhật"]
        day = datetime.now().weekday()
        if day == 6:
            return ["Nhà lữ hành, hôm nay là cuối tuần rồi! Vào Chủ Nhật bạn có thể farm mọi loại tài nguyên!"]
        else:
            messages = ["Hôm nay là " + weekDays[day] + " rồi nhà lữ hành, bạn có thể kiếm các loại tài nguyên sau:"]
            if type in ["talent", "book", "all"]:
                for key, value in self.talent[day]:
                    messages.append("Sách " + key + ": ", + ", ".join(value))
            if type in ["weapon", "all"]:
                for key, value in self.weapon[day]:
                    messages.append("Nguyên liệu " + key + ": ", + ", ".join(value))
            return messages

