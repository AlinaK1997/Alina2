import matplotlib.pyplot as plt

from passagiata_aleatoria import PassegiataALeatoria
# creare l'ogetto Passegiata Aleatoria

pa = PassegiataALeatoria(5000)

pa.fare_passegiata()

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.scatter(pa.x, pa.y, s = 20, c = pa.x, cmap = plt.cm.plasma)
plt.show()