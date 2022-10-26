from Crypto.Util.number import bytes_to_long as b2l
key = "7876565434321123434565678788787656543432112343456567878878765654433211234"
cipher = "'I thought to see the fairies in the fields, but I saw only the evil elephants with their black backs. Woe! how that sight awed me! The elves danced all around and about while I heard voices calling clearly. Ah! how I tried to see--throw off the ugly cloud--but no blind eye of a mortal was permitted to spy them. So then came minstrels, having gold trumpets, harps and drums. These played very loudly beside me, breaking that spell. So the dream vanished, whereat I thanked Heaven. I shed many tears before the thin moon rose up, frail and faint as a sickle of straw. Now though the Enchanter gnash his teeth vainly, yet shall he return as the spring returns. Oh, wretched man! Hell gapes, Erebus now lies open. The mouths of Death wait on thy end.'"
sol = []
text1 = []
text = ""
j, k = 0, 0
i = 0
print(len(cipher))
while (i < len(cipher)):
    while (i < len(cipher) and cipher[i] != " "):
        text = text+cipher[i]
        i += 1
    if (text != ""):
        text1.insert(j, text)
        j += 1
    text = ""
    if (j == 8):
        sol.insert(k, text1)
        text1 = []
        j = 0
        k += 1
    i += 1
print(sol)
