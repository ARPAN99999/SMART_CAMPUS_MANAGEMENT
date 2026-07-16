locations = {
    "library": "Ground Floor, Block A",
    "canteen": "Near Main Gate",
    "it department": "Second Floor, Block B",
    "computer lab": "Third Floor, Block C",
    "principal office": "Administrative Block",
    "accounts office": "Ground Floor, Admin Block"
}

def find_location(place):

    place = place.lower()

    for key in locations:

        if key in place:
            return locations[key]

    return "Location not found."