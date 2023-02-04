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

        def checku2e(x):

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
