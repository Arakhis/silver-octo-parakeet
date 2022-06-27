import random

times = ["Завтра", "Днем", "Утром", "В воскресенье", "На заре", "После работы"]
advices = ["ожидайте", "предостерегайтесь", "будьте готовы для"]
promises = ["завтрака", "переезда", "гостей", "перемен"]

gen_prom = []

while len(gen_prom) < 5:
	first = random.choice(times)
	second = random.choice(advices)
	third = random.choice(promises)
	term = (first + " " + second + " " + third)
	gen_prom.append(term)
	
print(gen_prom[0])
print(gen_prom[1])
print(gen_prom[2])
print(gen_prom[3])
print(gen_prom[4])