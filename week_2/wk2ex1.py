# Gemaakt door: Sander en Chris
# Klas: ITV1K

# Opgave 1: voorbeeld
e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)

# Opgave 2: [7, 1] maken
answer1 = e[1:2] + pi[1:2] 
print(answer1)

# Opgave 3: [1,1,2] maken
answer2 = e[-1:] + pi[1:2] + e[0:1]
print(answer2)

#opgave 4: [1,4,1,5,9]
answer3 = pi[1:]
print(answer3)

#opgave 5: [1,2,3,4,5]
answer4 = pi[1:2] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print(answer4)


# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"

# Opgave 6:  'hoi' maken
answer5 = s[0:2] + g[4]
print(answer5)

# Opgave 6:  'schoenen' maken
answer6 = s[4:8] + g[7:9] + g[7:9]
print(answer6)

# Opgave 7:  'anzeogeschool' maken
answer7 = h[1:5] + s[1:]
print(answer7)

# Opgave 8:  'gnagnahahahahaha' maken
answer8 = g[0:1] + h[2:3] + h[1:2] + g[0:1] + h[2:3] + h[1:2] + 5*(h[0:2])
print(answer8)

# Opgave 9:  'legonoego' maken
answer9 = s[-1:] + h[4] + s[2::5] + g[-4::-3] + s[-7::-1]
print(answer9[:-1])

#Opgave 10: 'leggings' maken
answer10 = s[9:10] + g[7::8] + g[0:1] + g[0:1] +g[4:6] + g[0:1] + s[4:5]
print(answer10)
