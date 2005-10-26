#!/usr/bin/env python
# -*- coding: windows-1251 -*-
# Copyright (C) 2005 Kiseliov Roman
__rev_id__ = """$Id$"""


from pyExcelerator import *

w = Workbook()
ws = w.add_sheet('F')

i = 0
for n in sorted(ExcelMagic.std_func_by_name):
    ws.write(i, 0, n)
    ws.write(i, 3, Formula(n + "($A$1)"))
    i += 1

w.save('formula_names.xls')