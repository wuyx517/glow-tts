""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict, pinyin2phone
import utils

hps = utils.get_hparams()

_pad = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
# 判定是否为中文
if getattr(hps.data, "language", None) == "Mandarin":
    py2ph = pinyin2phone.Pinyin2Phone(hps.data.Mandarin_path)
    symbols = [_pad] + list(_punctuation) + py2ph.make_phone_set()
else:
    symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
