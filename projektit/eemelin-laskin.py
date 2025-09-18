import numpy as np

r=6371
print("Anna kaikki koordinaatit seuraavasti: 40.741895, -73.989308 ")
koord1 = input("Anna koordinaatit ensimmäiselle sijainnille pilkulla erotettuna: ")
koord2 = input("Anna koordinaatit toiselle sijainnille pilkulla erotettuna: ")
sade = int(input("Anna säde kokonaislukuna (maan säde on 6371 km): "))

# Muutetaan input oikeiksi vektoreiksi
v1temp = koord1.split(",")
v2temp = koord2.split(",")

v1 = []
v2 = []

for n in range(len(v1temp)):
    v1.append(float(v1temp[n]))

for n in range(len(v2temp)):
    v2.append(float(v2temp[n]))

theta2 = v2[1]
theta1 = v1[1]

phi1 = np.linalg.norm(v1[0] - 90)
phi2 = np.linalg.norm(v2[0] - 90)

theta1 = theta1 * np.pi / 180
theta2 = theta2 * np.pi / 180
phi1 = phi1 * np.pi / 180
phi2 = phi2 * np.pi / 180

e1 = [np.sin(phi1)*np.cos(theta1), np.sin(phi1)*np.sin(theta1), np.cos(phi1)]
e1testi = [np.sin(theta1)*np.cos(phi1), np.sin(theta1)*np.sin(phi1), np.cos(theta1)]
e2 = [np.sin(phi2)*np.cos(theta2), np.sin(phi2)*np.sin(theta2), np.cos(phi2)]

beta = np.arccos(np.dot(e1,e2) / (np.linalg.norm(e1) * np.linalg.norm(e2)))
print(f"Etäisyys {beta*sade:.2f} km")