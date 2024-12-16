import matplotlib.pyplot as plt

massimo_input = 1000
input_valori = range(1, massimo_input +1)
quadrati = [x ** 2 for x in input_valori]

plt.style.use("ggplot")

fig, ax = plt.subplots()
ax.scatter(input_valori,quadrati, s = 30, c = quadrati, cmap = plt.cm.plasma)

# impostare titolo del grafico e assi
ax.set_title("Quadrati dei numeri", fontsize = 24)
ax.set_xlabel("Valore", fontsize = 14)
ax.set_ylabel("Quadrati", fontsize = 14)
ax.tick_params(labelsize = 14)

ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style = "plain")

counter = 3
# plt.show()
plt.savefig(f"img/figura_quadrati{counter}.png", bbox_inches = "tight")