import winsound, sys
import random
import os.path

# сарафан: поднять подол - lift up, спустить бретельку, оголив левую или правую грудь
# расстегнуть блузку (поднимает эротичность), распахнуть блузку

class clothes_element:
    def covered_parts(self):
        return []
    def do(self, s):
        raise "clothes_element.do"
    def __str__(self):
        return self.__class__.__name__
class panties:
    covered = set(["pussy", "butt", "labonza"])
    def covered_parts(self):
        return list(self.covered)
        

class female_body: 
    # одеть/раздеть
    # поставить в позу setpose 
    # эротичное прикоснование touch: рукой, стеком: эротично
    # мастурбировать stimulate: киску, анус, грудь, попу
    # отшлепать spank - рукой, стеком, плеткой, линейкой, стеблями от цветов
    # аксессуары add_device/remove_device - зажимы (с разным зажатием), прищепки, на грудь и киску, анальная пробка
    # ошейник с поводком, 
    # действия с губами: поцеловать, кляп, засунуть пальчик
    # связывание - невозможность пошевелить частями тела - руки, ноги

    parts = ["left butt", "right butt", "left nipple", "right nipple", "left breast", "right breast",
             "left hip", "right hip", "left foot", "right foot", "labonza" ]
    areas = {"butt": ["left butt", "right butt"], "pussy": ["left pussyleap", "right pussyleap"], 
             "hips": ["left hip", "right hip"], "feet": ["left foot", "right foot"],
             "breast": ["left breast", "right breast", "left nipple", "right nipple"]}
    clothes_cover = {"panties": ["pussy", "butt", "labonza"], 
                     "bra": ["breasts"], 
                     "strings": ["pussy"], 
                     "skirt": ["pussy", "butt", "hips"], 
                     "top": ["breast", "back"],
                     "dress": ["breast", "butt", "hips", "back"], 
                     "stockings": []}
    clothes = set([])

    def dress_up(self, added_clothes):
        self.clothes = self.clothes | set(added_clothes)
    def undress(self, removed_clothes):
        self.clothes = self.clothes - set(removed_clothes)
    def parts_and_areas(self, parts_or_areas):
        everything = []
        for item in parts_or_areas:
            everything.append(item)
            if item in self.areas:
                everything += self.areas[item]
        return everything

    #def spank(self):


    def covered_parts(self):
        covered = []
        for clothes_item in self.clothes:
            covered += self.clothes_cover[clothes_item]
        return self.parts_and_areas(covered)

    def visible_parts(self):
        return set(self.parts) - set(self.covered_parts())


class slavegirl:
    # характеристики
    slut = 0 
    maso = 0 
    sub = 0 #
    exhib = 0 # 
    # состояние
    romance = 0
    lust = 0
    pain = 0
    shame = 0
    
    #def look_erotic(self):
        # чем меньше надето обычной одежды, тем эротичнее
        # чем больше видимых аксессуаров, тем эротичнее

    def spank(self, target, strength):
        file = './wav/spank_%s%d.wav' % (strength, 1);       
        #while ~os.path.isfile(file):
        #    file = 'wav/spank_%s%d.wav' % (strength, random.randrange(1, 10));       
        winsound.PlaySound(file, winsound.SND_FILENAME)

    #def mirror(self):
    #def stimulate(self):

def main1():
    random.seed(1)
    girl = slavegirl()
    #girl.spank(1, 'A')

    body = female_body()
    body.dress_up(["dress"])
    #visible = body.visible_parts()
    #body.spank
    #body.add_clothes
    #body.remove_clothes
    a = 1
    
    # сессия: 
    