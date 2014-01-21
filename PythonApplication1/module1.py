import winsound, sys
import random
import os.path

from threading import Thread
from time import sleep
from queue import Queue


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
    excitement = 0
    
    #def look_erotic(self):
        # чем меньше надето обычной одежды, тем эротичнее
        # чем больше видимых аксессуаров, тем эротичнее
    sound_queue = Queue()
    def __init__(self, slavename):
        self.name = slavename
        t = Thread(target=self.worker)
        t.daemon = False
        t.start()
    def __enter__(self):
        return self
    def __exit__(self):
        byebye = {0: "Thank you, mistress", 1: "Mistress, may I call you tomorrow?"}
        print(self.name, ': ', byebye[random.randrange(0, 1)])
        sound_queue.task_done()
        return self

    def worker(self):
        # как менять громкость?
        # как определить сколько времени идет играется звук
        while True:
            try:
                item = sound_queue.get_nowait()
            except:
                if self.pain > 5:
                    file = '../wav/breath_a1.wav'  
                    winsound.PlaySound(file, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def spank(self, target, strength):
        strength_code = {0: "A", 1: "A", 2: "A", 3: "A", 4: "B", 5: "B", 6: "B", 7: "B", 
                         8: "C", 9: "C", 10: "C"}
        file = '../wav/spank_%s%d.wav' % (strength_code[strength], random.randrange(1, 3));       
        winsound.PlaySound(file, winsound.SND_FILENAME)

        self.pain = min(100, self.pain + strength)

        pain_reaction = (self.pain / 20 + strength / 2) / 3
        pain_reaction = min(10, pain_reaction * 3 + random.randrange(0, 3))
        pain_text = {0: "Mmmm!", 1: "More!", 2: "Please, harder!", 3: "Mmmm!", 
                     4: "Ouch!", 5: "Ou!", 6: "Ufff!!", 7: "Ummm, it was realy hard", 
                     8: "Mistress, it is too much for mee", 9: "It really hearts!", 10: "No, please, stop it!!!"}

        print(self.name, ': ', pain_text[int(pain_reaction)])
    def timestep(self, dt):
        self.excitement = 0.98 * self.excitement / dt
        

    #def mirror(self):
    #def stimulate(self):
girl = slavegirl('Tanya')



def spank_command(cmd):
    body_part = cmd[1]
    if len(cmd) >= 3:
        strength = int(cmd[2])
    else:
        strength = 5
        
    strength_text = {0: "weakly", 1: "weakly", 2: "weakly", 3: "weakly", 4: "sensibly", 5: "sensibly", 6: "sensibly", 7: "sensibly", 
                     8: "heavily", 9: "heavily", 10: "heavily"}
    st = strength_text[strength]
    print('[Mistress spanks slavegirls %s %s]' % (body_part, st))

    girl.spank(body_part, strength)

    return

def main1():
    random.seed(1)

    while 1:
        s = input()
        cmd = s.split(' ')
        if cmd[0] == 'spank':
            spank_command(cmd)
        elif cmd[0] == 'stop':
            girl.end_session()
            break
        elif cmd[0] == 'stim':
            print('[Mistress stimulates slavegirls charms]')
        elif cmd[0] == 'fondle':
            print('[Mistress use her hand to take a tender care of the slavegirl]')
        elif cmd[0] == 'kiss':
            print('[Mistress kisses the slavegirl]')
        else:
            print('[Mistress is doing something with the slavegirl]')
    
    # сессия: 
    