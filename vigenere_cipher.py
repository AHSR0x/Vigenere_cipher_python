_start=65
_end=90

_list_char=list()
for i in range (65,91,1):
    _list_char.append(chr(i))

_matran=list()
for i in range (0,26,1):
    _list_temp=list()
    for j in range(i,26,1):
        _list_temp.append(_list_char[j])
    for k in range(0,i,1):
        _list_temp.append(_list_char[k])
    _matran.append(_list_temp)
for i in range (0,26,1):
    print _matran[i]

_string_1 = "frequentlyreferredtoasAttilatheHunwastheruleroftheHunsfrom434untilhisdeathin453HewasleaderoftheHunnicEmpirewhichstretchedfromtheUralRivertotheRhineRiverandfromtheDanubeRivertotheBalticSea"
_string_2 = "ncejbiunyeicylvwpdzwssTmbtltallBhtnylaljcurmjoymppHnuwmlbs434llmppmtsjmstabv453SephwsynjvphmxmpHavfivXuaiklaocpnjrklxhsejnjofmppUkhpYcikirhaljChovwRbomcagkjyizzycWhrzmeXqnekmwehxIesnviJct"
_string_1 = _string_1.upper()
_string_2 = _string_2.upper()
_flag = ""
for i in range(len(_string_1)):
    for j in range(26):
        if _matran[ord(_string_1[i])-65][j] ==_string_2[i]:
            _flag+=chr(j+65)

print _flag



