from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create a visited
visited = {}

# Create a way to move between rooms
move = []

# Create a way to move backwards
backwards = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}

# Create a starting room for visited that gathers the exits of the room
visited[player.current_room.id] = player.current_room.get_exits()

# Create a while that checks if we have been to every room and breaks out if we have
while len(visited) < len(room_graph):
    # Check if the current room we are in is not in visited
    if player.current_room.id not in visited:
        # If it is not then add the current room to our visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # Create a way to remove the room we came from to visited
        previous_room = move[-1]
        visited[player.current_room.id].remove(previous_room)
    else:
        # If we have been to this current room before then back track until there is a new route to go to
        while len(visited[player.current_room.id]) < 1:
            # Go back to a previous room
            # Remove that room because it is a room we have been to before, and store it
            previous_room = move.pop()
            # Append traversal_path with previous_room
            traversal_path.append(previous_room)
            # Append where our player is traveling
            player.travel(previous_room)

        # Store the next room once a new opening is found
        next_room = visited[player.current_room.id].pop()
        # Append room to our traversal_path
        traversal_path.append(next_room)
        # Add the opposite of our move to our backwards list, best used for when we need to back track previously visited rooms
        move.append(backwards[next_room])
        # Travel to the next room and updates what room the player is currently in
        player.travel(next_room)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
