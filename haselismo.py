#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import re
import urllib

def cleanwikimarkup(text):
    text = re.sub(r'(?im)\'\'+', r'', text)
    text = re.sub(r'(?im)\[\[[^\[\]]+?\|([^\[\]]+?)\]\]', r'\1', text)
    text = re.sub(r'(?im)\[\[([^\[\]]+?)\]\]', r'\1', text)
    text = re.sub(r'(?im)\[http[^\[\] ]+? ([^\]]+?)\]', r'\1', text)
    return text

def main():
    url = 'https://es.wikiquote.org/wiki/Pablo_Hasél?action=raw'
    raw = urllib.urlopen(url).read()
    frases = re.findall(r'(?im)^\* *(«[^\n«»]{10,}»)', raw)
    frases2 = []
    for frase in frases:
        frases2.append(cleanwikimarkup(frase))
    frases = frases2
    #print('\n'.join(frases2))
    print(random.choice(frases2))

if __name__ == '__main__':
    main()
