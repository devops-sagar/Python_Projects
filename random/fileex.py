import os
import random

print(os.getcwd())

str = "Something has always existed. According to physics, there can never be true physical nothingness—though there can be times when existence resembles nothing, such as a vacuum (the state of minimum possible energy) (Phys.org). Creating a space where there are no quantum fluctuations requires an enormous amount of energy, and there would be a remnant of that energy in that space afterwards if the fluctuations were flushed out, plus an unstable environment (1veritasium). Even on computers, deleted data is not actually tossed away, by rather written over. The fact that there can never be nothingness means the universe, and anything possibly beyond it, is eternal, as something has always been around. Whatever we consider to be before the Big Bang—God, the universe in infinitesimal form, or both—one thing is certain: it was there."
x = str.split()
# print(x)

os.chdir(f"{os.getcwd()}/random")
print(os.getcwd())

# if(not os.path.isfile(".png")):
#     for i in range (0, 10):
#         with open (f"{random.choice(x)}.png", 'w') as f:
#             # f.write(f"file created numer:{i}")
#             pass

file = ".png"
for file in os.listdir(os.getcwd()):
    old = os.path.join(os.getcwd(), file)
    for i in range(0, 100):
        new_name = f"{i}"
    new = os.path.join(os.getcwd(), new_name)

    os.rename(old, new)