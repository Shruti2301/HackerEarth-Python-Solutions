 # Read the number of songs in Bob's playlist
# Input is converted from string to integer
num_of_songs = int(input())

# Read the singers of each song as a list of integers
# Example input: "1 1 2 2 4"
seq_of_singer = list(map(int, input().split()))

# Create an empty dictionary to store frequency of each singer
# Key   → singer ID
# Value → number of songs by that singer
freq = {}

# Loop through each singer in the playlist
for singer in seq_of_singer:
    # If singer already exists in dictionary, increase count by 1
    # If singer does not exist, initialize count as 0 and then add 1
    freq[singer] = freq.get(singer, 0) + 1

# Find the maximum number of songs sung by any singer
max_freq = max(freq.values())

# Initialize counter for favourite singers
count_favourite = 0

# Loop through all singers in the frequency dictionary
for singer in freq:
    # If this singer's song count equals the maximum frequency
    if freq[singer] == max_freq:
        # Increment favourite singer count
        count_favourite += 1

# Print the number of favourite singers
print(count_favourite)

