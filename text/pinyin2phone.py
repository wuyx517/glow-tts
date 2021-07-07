
class Pinyin2Phone:
    """
    将拼音转换为音标
    """
    def __init__(self, file):
        pin2phone = {}
        with open(file, 'r') as f:
            map_info = f.readlines()
        for unit_map in map_info:
            map_sp = unit_map.strip().split(' ', 1)
            pin2phone[map_sp[0]] = map_sp[1]
        self.pin2phone = pin2phone

    def __len__(self):
        return len(self.pin2phone)

    def lookup(self, pinyin):
        return [self.pin2phone[pinyin]]

    def make_phone_set(self):
        phone_set = []
        for phone_list in self.pin2phone.values():
            for unit_phone in phone_list.split(' '):
                if '@{}'.format(unit_phone) not in phone_set:
                    phone_set.append('@{}'.format(unit_phone))
        return phone_set


if __name__ == '__main__':
    test = Pinyin2Phone('data/pinyin-lexicon-r.txt')
    test.make_phone_set()