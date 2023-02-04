import numpy as np
import re


class SWEEncoder_ja:
    def __init__(self, bpe, emoji):
        self.bpe = [[b] if (b == ',' or ',' not in b) else b.split(',') for b in bpe]
        self.swe = {}
        for idx, b in enumerate(self.bpe):
            for wd in b:
                self.swe[wd] = idx
        self.emoji = emoji
        self.maxlen = np.max([len(w) for w in self.swe.keys()])

    def __len__(self):
        return len(self.bpe)

    def encode(self, text, clean=False):
        def checkkigou(x):
            e = x.encode()
            if len(x) == 1 and len(e) == 2:
                c = (int(e[0]) << 8) + int(e[1])
                if (c >= 0xc2a1 and c <= 0xc2bf) or (c >= 0xc780 and c <= 0xc783) or \
                   (c >= 0xcab9 and c <= 0xcbbf) or (c >= 0xcc80 and c <= 0xcda2):
                    return True
             return False 

        def checku2e(x):
            e = x.encode()
            if len(x) == 1 and len(e) == 3:
                c = (int(e[0]) << 16) + (int(e[1]) << 8) + int(e[2])
                if c >= 0xe28080 and c <= 0xe2b07f:
                    return True
            return False

        pos = 0
        result = []
        while pos < len(text):
            end = min(len(text), pos+self.maxlen+1) if text[pos] == '<' else pos+3
            kouho = []
        for e in range(end, pos, -1):
            wd = text[pos:e]
            if wd in self.swe:
                if wd[0] == '<' and len(wd) > 2:
                    kouho = [(self.swe[wd], e)]
                    break
                else:
                    kouho.append((self.swe[wd], e))
        if len(kouho) > 0:
            wp,  e = sorted(kouho, key=lambda x: x[0])[0]
            result.append(wp)
            pos = e
        else:
            end = pos+1
            wd = text[pos:end]
            if checkkigou(wd):
                result.append(self.swe['<KIGOU>'])
            elif checku2e(wd):
                result.append(self.swe['<U2000U2BFF>'])
            else:
                for i in wd.encode('utf-8'):
                    result.append(self.swe['<|byte%d|>' % i])
            pos = end
        return result
