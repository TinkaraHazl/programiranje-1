from functools import lru_cache
# =============================================================================
# Najdaljše naraščajoče podzaporedje
# =============================================================================

# -----------------------------------------------------------------------------
# Napišite funkcijo `najdaljse_narascajoce_podazporedje`, ki sprejme seznam in
# poišče najdaljše (ne strogo) naraščajoce podzaporedje števil v seznamu.
#
# Primer: v seznamu `[2, 3, 6, 8, 4, 4, 6, 7, 12, 8, 9]` kot rezultat vrne
# podzaporedje `[2, 3, 4, 4, 6, 7, 8, 9]`.
# -----------------------------------------------------------------------------
def najdaljse_narascajoce_podazporedje(sez):
    
    @lru_cache
    def najdaljse(spodnja_meja, i):
        if i >= len(sez):
            return []
        elif sez[i] < spodnja_meja:
            return najdaljse(spodnja_meja, i + 1)
        else:
            z_prvim = [sez[i]] + najdaljse(sez[i], i + 1)
            brez_prvega = najdaljse(spodnja_meja, i + 1)
            if len(z_prvim) > len(brez_prvega):
                return z_prvim
            else:
                return brez_prvega
    
    return najdaljse(float(-"inf"), 0)
# -----------------------------------------------------------------------------
# Rešitev sedaj popravite tako, da funkcija `vsa_najdaljsa` vrne seznam vseh
# najdaljših naraščajočih podzaporedij.
# -----------------------------------------------------------------------------
def vsa_najdaljsa(sez):
    @lru_cache(maxsize=None)
    def najdaljse(spodnja_meja, i):
        if i >= len(sez):
            return (0, [[]])
        elif sez[i] < spodnja_meja:
            return najdaljse(spodnja_meja, i + 1)
        else:
            d_z, zap_z = najdaljse(sez[i], i + 1)
            d_b, zap_b = najdaljse(spodnja_meja, i + 1)
            if d_z + 1 > d_b:
                return (d_z + 1, [[sez[i]] + zap for zap in zap_z])
            elif (d_z + 1 < d_b):
                return (d_z, zap_z)
            else:
                return (d_b, [[sez[i]]+zap for zap in zap_z] + zap_b)
    
    return najdaljse(float(-"inf"), 0)[1]

# =============================================================================
# Žabica
# =============================================================================
# Žabica se je izgubila v močvari in želi kar se da hitro odskakljati ven. Na
# srečo močvara vsebuje veliko muh, s katerimi si lahko povrne energijo, kajti
# utrujena žabica ne skoči daleč.
# 
# S funkcijo `zabica(mocvara)` želimo ugotoviti, kako hitro lahko žabica
# odskaklja iz močvare. Močvaro predstavimo s tabelo, kjer žabica prične na
# ničtem polju. Če je močvara dolžine `k`, je cilj žabice priskakljati vsaj na
# `k`-to polje ali dlje (torej prvo polje, ki ni več vsebovano v tabeli).
# 
# Energičnost žabice predstavimo z dolžino najdaljšega možnega skoka. Torej
# lahko žabica z količino energije `e` skoči naprej za katerokoli razdaljo med
# `1` in `e`, in če skoči naprej za `k` mest ima sedaj zgolj `e - k` energije.
# Na vsakem polju močvare prav tako označimo, koliko energije si žabica povrne,
# ko pristane na polju. Tako se včasih žabici splača skočiti manj daleč, da
# pristane na polju z več muhami. Predpostavimo, da ima vsako polje vrednost
# vsaj `1`, da lahko žabica v vsakem primeru skoči naprej.
# 
# V primeru `[2, 4, 1, 2, 1, 3, 1, 1, 5]` lahko žabica odskaklja iz močvare v
# treh skokih, v močvari `[4, 1, 8, 2, 11, 1, 1, 1, 1, 1]` pa potrebuje zgolj
# dva.
# =============================================================================
def zabica(mocvara):
    @lru_cache(maxsize=None)
    def pobeg(e, zacetek):
        if zacetek >= len(mocvara):
            return 0
        else: 
            e += mocvara[zacetek]
            return 1 + min([pobeg(e - i, zacetek + i) for i in range(1, e + 1)])
    return pobeg(0, 0)

# =============================================================================
# Nageljni
# =============================================================================
# Mama Franca želijo na balkon širine `n` postaviti `m` korit z nageljni širine
# `l` (korit, ne nageljnov). Zaradi lažjega zalivanja mora biti med dvema
# koritoma vsaj za 1 enoto prostora. Mama Franca želijo postaviti vsa korita,
# jih pa zaradi slabega vida med seboj ne razlikujejo. 
# 
# Vnuk je že spisal program, ki poišče število možnih postavitev, ne zna pa
# vrniti rešitev. Napišite funkcijo `nageljni(n, m, l)`, ki vrne seznam vseh
# možnih postavitev, da se bodo mama Franca lažje odločili.
# 
# Primer vseh štirih možnih postavitev pri balkonu širine 9 s tremi koriti
# širine 2 (kjer z 1 označimo nagelj in z 0 prazen prostor):
# 
#     [1, 1, 0, 1, 1, 0, 1, 1, 0]
#     [1, 1, 0, 1, 1, 0, 0, 1, 1]
#     [1, 1, 0, 0, 1, 1, 0, 1, 1]
#     [0, 1, 1, 0, 1, 1, 0, 1, 1]
# =============================================================================
@lru_cache(maxsize=None)
def nageljni(n, m, l):
   if m == 0:
       return [[0 for _ in range(n)]]
   if n < l:
       return []
   elif n == l and m == 1:
       return [[1 for _ in range(l)]]
   else:
       ne_postavimo = [[0] + postavitev for postavitev in nageljni(n -1, m, l)]
       postavimo = [[1 for _ in range(l)] + [0] + postavitev for postavitev in nageljni(n - l - 1, m - 1, l)]
       return postavimo + ne_postavimo
        
# =============================================================================
# Pobeg iz Finske
# =============================================================================
# Vaš sošolec Mortimer se je med potovanjem po Finski spravil v krepko godljo.
# Po divjem poskušanju lokalne vodke se je namreč stepel s kravo, zaradi česar
# ga sedaj lovi finska govedorejska mafija. Na srečo so za njegovo hrabro bitko
# slišale vse rokovske in metalske skupine, ki so mu pripravljene ponuditi
# prevoz.
# 
# Ker je Mortimer pridno poslušal predavanja iz finančne matematike, med potjo
# uspe prislužiti nekaj denarja, s katerim bo lahko plačal prevoz. Finci,
# navdušeni nad Mortimerjevim pogumom, mu dovolijo, da se med potjo zadolži,
# dokler na koncu pobega vse stroške povrne.
# 
# Mesta na poti predstavimo kot seznam, katerega elementi so seznami vseh
# možnih nadaljnjih poti. Pot je par `(indeks_cilja, denar)`. Kot primer
# 
#     [[(1, 10), (3, -10)],    # 0 
#     [(2, 10), (5, -20)],     # 1
#     [(3, -10)],              # 2 
#     [(4, 15)],               # 3 
#     [(5, 0)]]                # 4 
# pobeg([[(1, 10), (3, -10)], [(2, 10), (5, -20)], [(3, -10)], [(4, 15)], [(5, 0)]])
#                   
#  
# 
# pomeni, da lahko v mestu 1 Mortimer izbere med prevozom v mesto 2, kjer
# dodatno zasluži 10 evrov, ali pa prevoz v mesto 5, ki ga stane 20 evrov. Ker
# beži pred mafijo, lahko predpostavite, da bodo možne zgolj poti na mesta z
# višji indeksom (torej ni ciklov).
# 
# Pobeg je uspešen, čim lahko odpotuje v mesto, ki ni več na seznamu (torej
# skok na indeks, ki preseže seznam) in ima po koncu zadnjega skoka 0 ali več
# evrov. Napišite program, ki nam vrne pot z najmanjšim številom skokov,
# predstavljeno kot seznam indeksov mest na poti. Ker pobeg morda ni možen, naj
# v tem primeru funkcija vrne `None`.
# 
# Na primeru je optimalna pot `[0, 3, 4, 5]`, kjer se Mortimer sicer zadolži,
# vendar v skoku iz 3 v 4 zasluži dovolj, da konča z 5 evri. Hitrejša pot bi
# bila `[0, 1, 5]`, vendar v tem primeru Mortimer na koncu dolguje še 10 evrov.
# 
# Mortimer pot vedno začne v mestu z indeksom 0 in ima 0 evrov (saj je vse
# zapil). Funkcija `pobeg` sprejme seznam, ki predstavlja finska mesta in vrne
# seznam indeksov mest, v katerih se Mortimer ustavi.
# =============================================================================
def pobeg(mesta):
    @lru_cache
    def moznosti(i, eur):
        if i >= len(mesta) and eur >= 0:
            return [i]
        elif i >= len(mesta) and eur < 0:
            return None
        else: 
            for (k, e) in mesta[i]:
                sez = []
                if moznosti(k, eur + e) is not None:
                    sez += moznosti(k, eur + e)
            if len(sez) == 0:
                return None
            else:
                return [i] + sorted(moznosti, key=len)[0]

    return moznosti(0, 0)

# =============================================================================
# Pričetek robotske vstaje
# =============================================================================
# Nepreviden študent je pustil robotka z umetno inteligenco nenadzorovanega.
# Robotek želi pobegniti iz laboratorija, ki ga ima v pomnilniku
# predstavljenega kot matriko števil:
# 
#   - ničla predstavlja prosto pot
#   - enica predstavlja izhod iz laboratorija
#   - katerikoli drugi znak označuje oviro, na katero robotek ne more zaplejati
# 
# Robotek se lahko premika le gor, dol, levo in desno ter ima omejeno količino
# goriva. V zbirki programov že ima funkcijo `moznost_pobega(soba, vrsta,
# stolpec, koraki)`, ki pove ali je pobeg možen.
# 
# Napišite funkcijo `pot_pobega(soba, vrsta, stolpec, koraki)`, ki sprejme
# matriko sobe, začetno pozicijo in število korakov ter izračuna pot po kateri
# robotek pobegne (če to ni možno vrne `None`). Pot zakodiramo s seznamom
# ukazov `'gor'`, `'dol'`, `'levo'` in `'desno'`.
# 
# Na primer za laboratorij:
# 
#     [[0, 1, 0, 0, 2],
#      [0, 2, 2, 0, 0],
#      [0, 0, 2, 2, 0],
#      [2, 0, 0, 2, 0],
#      [0, 2, 2, 0, 0],
#      [0, 0, 0, 2, 2]]
#pot_pobega([[0, 1, 0, 0, 2], [0, 2, 2, 0, 0], [0, 0, 2, 2, 0], [2, 0, 0, 2, 0],[0, 2, 2, 0, 0], [0, 0, 0, 2, 2]], 5, 0, 3)
# 
# robotek iz vrste 3 in stolpca 1 pri vsaj petih korakih pobegne z ukazi
# 
#      ['gor', 'levo', 'gor', 'gor', 'desno']
# 
# medtem ko iz vrste 5 in stolpca 0 ne more pobegniti.
# =============================================================================
def pot_pobega(soba, vrsta, stolpec, koraki):  
    @lru_cache
    def pobeg(v, s, k):
        if v >= len(soba) or s >= len(soba[0]) or v < 0 or s < 0:
            return None
        elif soba[v][s] == 1:
            return []
        elif soba[v][s] == 2:
            return None
        elif k == 0:
            return None
        else:
            moznosti = \
            [('levo', pobeg(soba, v, s - 1, k - 1)),
            ('desno', pobeg(soba, v, s + 1, k - 1)),
            ('dol', pobeg(soba, v + 1, s, k - 1)),
            ('gor', pobeg(soba, v - 1, s, k - 1))]
            uspesne = [(smer, pot) for (smer, pot) in moznosti if pot is not None]
            if uspesne:
                return [uspesne[0][0]] + uspesne[0][1]
            else: return None
    return pobeg(vrsta, stolpec, koraki)