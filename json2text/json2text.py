#-----------------------------------------------------------------------------
# Copyright (c) 2022 Rui Xie xrdavies@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#-----------------------------------------------------------------------------

import json
import jsonmerge
from functools import reduce

__all__ = ['JSON2Text', 'Text2JSON']

def JSON2Text(jsonObj):
    if isinstance (jsonObj, str):
        return [('', jsonObj)]
    elif isinstance (jsonObj, dict):
        ret = []
        for key in jsonObj:
            ll = JSON2Text(jsonObj[key])
            def addprefix(x):
                (k, v) = x
                if len(k) == 0:
                    return (key, v)
                else:
                    return (key + '.' + k, v)
            ret = ret + list(map(addprefix, ll))
        return ret
    else:
        print("Error! type: ", type(jsonObj))
    pass

def Text2JSON(texts): # lines
    def line2json(line):
        key = line[0]
        text = line[1]
        if len(key) == 0:
            return text
        else:
            ret = {}
            words = key.split('.')
            words.reverse()
            for i, word in enumerate(words):
                if i == 0:
                    ret[word] = text
                else:
                    ret = {word: ret}
            return ret
    return reduce(lambda x, y: jsonmerge.merge(x,y), list(map(line2json, texts)), {})