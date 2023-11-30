from absurdriotwrapper import AbsurdRiotWrapper
from absurdriotwrapper import AbsurdLolWrapper

lol_wrapper = AbsurdLolWrapper("your-api-key")

my_region = "euw1"

my_summoner = lol_wrapper.summoner.by_name(my_region, "Hisatsuka")

print(my_summoner.json())
