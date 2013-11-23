import winsound, sys
import random
import os.path

class female_body:
    # еще надо полупрозрачность, добавляет эротичности
    # и еще надо возможность приспустить/приподнять одежду
    parts = ["left butt", "right butt", "left nipple", "right nipple", "left breast", "right breast",
             "left hip", "right hip", "left foot", "right foot"]
    areas = {"butt": ["left butt", "right butt"], "pussy": ["left pussyleap", "right pussyleap"], 
             "hips": ["left hip", "right hip"], "feet": ["left foot", "right foot"],
             "breast": ["left breast", "right breast", "left nipple", "right nipple"]}
    clothes_cover = {"panties": ["pussy", "butt"], "bra": ["breasts"], "strings": ["pussy"], 
                     "skirt": ["pussy", "butt", "hips"], "top": ["breast", "back"],
                     "dress": ["breast", "butt", "hips", "back"], "stockings": []}
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

    def covered_parts(self):
        covered = []
        for clothes_item in self.clothes:
            covered += self.clothes_cover[clothes_item]
        return self.parts_and_areas(covered)

    def visible_parts(self):
        return set(self.parts) - set(self.covered_parts())
    #def look_erotic(self):
        # чем меньше надето обычной одежды, тем эротичнее
        # чем больше видимых аксессуаров, тем эротичнее


class slavegirl:
    # характеристики
    slut = 0 
    maso = 0 
    sub = 0 #
    exhib = 0 # 
    # состояние
    lust = 0
    pain = 0
    shame = 0
    
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
    visible = body.visible_parts()
    #body.spank
    #body.add_clothes
    #body.remove_clothes
    a = 1
    
    