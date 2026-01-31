# 3a Create a list with four movies and print it
movies = ["Inception", "The Matrix", "Interstellar", "Gladiator"]
print(movies)

# 3b Add "Fellowship of the Ring" at the end of the list
movies.append("Fellowship of the Ring")
print(movies)

# 3c Add "The Two Towers" at the first position (index 0)
movies.insert(0, "The Two Towers")
print(movies)

# 3d Find out the position (index) of "Fellowship of the Ring"
index_fellowship = movies.index("Fellowship of the Ring")
print("Index of Fellowship of the Ring:", index_fellowship)

# 3e Remove another movie
movies.remove("Inception")
print(movies)

# Check: has Fellowship changed index?
new_index = movies.index("Fellowship of the Ring")
print("New index of Fellowship of the Ring:", new_index)

# 3f Find out how long the list is
print("Length of the list:", len(movies))

# 3g Reverse the list
movies.reverse()
print("Reversed list:", movies)

# 3h Sort the list in alphabetical order
movies.sort()
print("Sorted list:", movies)
