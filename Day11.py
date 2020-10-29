# Question :
# Dan Rented two movies to watch last night.
# The first was 100 minutes long, the second 110 minutes long.
# How many hours did it take for Dan to watch the two movies

def minutes_to_hours(length):
    return length / 60


length_movie1 = 100
length_movie2 = 110

total_length = length_movie1 + length_movie2

print("Total hours : ", minutes_to_hours(total_length))
