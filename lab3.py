import re

my_st = r"Ветер свистел, визжал, кряхтел И гудел на разные лады. То жалобным тоненьким голоском, то грубым басовым раскатом распевал он свою боевую песенку. Фонари чуть заметно мигали сквозь огромные белые хлопья снега, обильно сыпавшиеся на тротуары, на улицу, на экипажи, лошадей и прохожих. А я все шла и шла, все вперед и вперед..."
vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
max_len = 0
res = r""
letter = ''
print(re.split(r"[.,\s+]+", my_st))
arr = re.split(r"[.,\s+]+", my_st)

for str in arr:
    str = str.lower()

    # Проверяем, есть ли в слове гласная из списка 
    for ch in vowels:
        if str.count(ch)>0:
            n = 0
            for other_ch in vowels:

                # Проверяем, есть ли в слове другие гласные 
                if other_ch != ch:
                    n = n + str.count(other_ch)
                    
            # В слове используется только одна гласная
            if n == 0:
                if len(str) >= max_len:
                    max_len = len(str)
                    res = str
                    letter = ch

print(f"\nСлово: {res}\nДлина: {len(res)}\nБуква '{letter}' встречается {res.count(letter)} раз ")
 
                     


