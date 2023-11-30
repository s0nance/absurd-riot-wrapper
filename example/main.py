from absurdriotwrapper import AbsurdRiotWrapper

riot_wrapper = AbsurdRiotWrapper('lol-you-thought')

my_region = 'euw1'

me = riot_wrapper.account.by_riot_id(my_region, "Hisatsuka", "GTR")

# CET ENDPOINT FONCTIONNE PAS ISSOU
print(me.json())
