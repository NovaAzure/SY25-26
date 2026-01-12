# The initial lineup
lineup = [
    ( "Code Play" , "Indie" , 30),
    ( "The Pythonistas" , "Rock" , 45),
    ( "Syntax Error" , "Metal" , 60)
]

# 1. Add the headliner
headliner = ( "The Byte Beats" , "Synthwave" , 90)
lineup.append(headliner)

# 2. Add another band using insert at index 0 (as the opener)
opener = ( "The Semicolons" , "Pop-Punk" , 20)
lineup.insert(0, opener)

# 3. Add a couple more bands to the end
more_bands = [
    ( "Logical Operators" , "Electronic" , 50),
    ( "Runtime Error" , "Noise Rock" , 35)
]
lineup.extend(more_bands)

# 4. Remove 'Syntax Error' (they had a scheduling conflict)
band_to_remove = ( "Syntax Error" , "Metal" , 60)
lineup.remove(band_to_remove)

# 5. Determine and print the total duration of the show in minutes
total_duration = 0
for band in lineup:
    duration = band[2] # Duration is the third element in the tuple
    total_duration += duration

print(f"The final lineup is: {lineup}")
print(f"The total show duration is: {total_duration} minutes")