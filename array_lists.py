class Album:
    """
   Represents an album with attributes: albumName (String), albumArtist (String), numberOfSongs (int).

   Attributes:
   - albumName (str): The name of the album.
   - albumArtist (str): The artist of the album.
   - numberOfSongs (int): The number of songs in the album.

   Methods:
   - __str__: Returns a string representation of the Album object.
   """
    def __init__(self, albumName, albumArtist, numberOfSongs):
        """ Initialize Album Object"""
        self.albumName = albumName
        self.albumArtist = albumArtist
        self.numberOfSongs = numberOfSongs

    def __str__(self):
        """ Return a string representation of the Album object. """
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"


# albums1 list
albums1 = [
    Album("rf", "Jane Doe", 10),
    Album("sa", "John Doe", 8),
    Album("gb", "Tom", 12),
    Album("d", "Richard", 9),
    Album("fvf", "Harry", 15)
]

# Print albums1
print("Albums1:")
for album in albums1:
    print(album)


# Sort albums1 by the number of songs
def sort_by_number_of_songs(album):
    """
        Key function for sorting albums by number of songs
    """
    return album.numberOfSongs


albums1.sort(key=sort_by_number_of_songs)

# Print sorted albums1
print("\nSorted Albums1 by Number of Songs:")
for album in albums1:
    print(album)


# Swap elements at positions 1 and 2 in albums1
albums1[1], albums1[2] = albums1[2], albums1[1]

# Print albums1 after swapping
print("\nAlbums1 after swapping:")
for album in albums1:
    print(album)

# Create a new list called albums2
albums2 = []

# Add 5 albums to albums2
albums2.extend([
    Album("subtract", "Ed Sheeran", 13),
    Album("KOD", "J Cole", 11),
    Album("Today", "Slim Shady", 7),
    Album("Tomorrow", "Laufey", 14),
    Album("Yesterday", "Kanye West", 6)
])

# Print albums2
print("\nAlbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2
albums2.extend(albums1)

# Add two new albums to albums2
albums2.extend([
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)
])


# Sort albums2 alphabetically by album name
def sort_by_album_name(album):
    """
        Key function for sorting albums by album name alphabetically.
    """
    return album.albumName


albums2.sort(key=sort_by_album_name)

# Print sorted albums2
print("\nSorted Albums2 by Album Name:")
for album in albums2:
    print(album)

# Search for "Dark Side of the Moon" in albums2 and print its index
searched_album = "Dark Side of the Moon"
index = next((i for i, album in enumerate(albums2) if album.albumName == searched_album), -1)

if index != -1:
    print(f"\n'{searched_album}' is found at index {index} in Albums2.")
else:
    print(f"\n'{searched_album}' is not found in Albums2.")
