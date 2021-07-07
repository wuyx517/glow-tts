import random


def csmsc(file):
    fw_train = open('csmsc_audio_train_filelist.txt', 'w')
    fw_val = open('csmsc_audio_val_filelist.txt', 'w')
    with open(file, 'r') as f:
        line_list = f.readlines()

    path_label_list = []
    i = 0
    for line in line_list[::2]:
        audio_id = line.split('\t')[0]
        audio_label = line_list[i + 1].strip()
        path_label_list.append('csmsc/{}.wav|{}\n'.format(audio_id, audio_label))
        i += 2
    random.shuffle(path_label_list)
    split_line = int(len(path_label_list) * 0.9)
    for path_label in path_label_list[:split_line]:
        fw_train.write(path_label)
    for path_label in path_label_list[split_line:]:
        fw_val.write(path_label)

    fw_train.close()
    fw_val.close()


if __name__ == '__main__':
    csmsc('/data/data/CSMSC/ProsodyLabeling/000001-010000.txt')

