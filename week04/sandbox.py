metals={
    "Ag" : "Silver",
    "Al" : "Aluminum",
    "Au" : "Gold",
    "Cu" : "Copper",
}

print(metals["Au"])

if "Ag" in metals:
    print("Ag exists in the metals dictionary")
else:
    print("Ag does not exist in the metals dictionary")

print(len(metals))