import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import random

player = [0, 0]
treasure = [3, 2]
moves = 0

def move_player(direction):
    global player, moves

    if not (found_treasure() or is_game_over()):
        if direction == "up" and player[1] != 0 and moves != 10:
            player[1] -= 1
            moves += 1
        elif direction == "down" and player[1] != 4 and moves != 10:
            player[1] += 1
            moves += 1
        elif direction == "left" and player[0] != 0 and moves != 10:
            player[0] -= 1
            moves += 1
        elif direction == "right" and player[0] != 4 and moves != 10:
            player[0] += 1
            moves += 1

def found_treasure():
    return True if player == treasure else False

def is_game_over():
    return True if found_treasure() or moves == 10 else False

def reset_game():
    global player, moves, treasure

    player = [0, 0]
    moves = 0
    treasure = [random.randint(0, 4), random.randint(0, 4)]

def get_game_state():
    return {
        "player": player,
        "found": found_treasure(),
        "moves": moves,
        "game_over": is_game_over(),
    }


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)

        if url.path == "/":
            html = Path("index.html").read_text(encoding="utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif url.path == "/move":
            direction = parse_qs(url.query).get("direction", [""])[0]
            # Note from Armaan: If you're confused about the above line of code...
            # url.query -> "direction=up"
            # parse_qs(url.query) -> {"direction": ["up"]}
            # parse_qs(url.query).get("direction", [""]) -> ["up"]
            # parse_qs(url.query).get("direction", [""])[0] -> "up"

            move_player(direction)

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif url.path == "/reset":
            reset_game()

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())


server = HTTPServer(("localhost", 3000), MyHandler)
print("Server running at http://localhost:3000")
server.serve_forever()
