octopus = int(input())
octopus_ganggang = []

for i in range(octopus//2):
    octopus_ganggang.append(1)
    octopus_ganggang.append(2)

if octopus % 2 == 1:
    octopus_ganggang.append(3)

print(*octopus_ganggang)