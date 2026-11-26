import json
from pathlib import Path
from uuid import uuid4

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# tips = [
#     {"id": str(uuid4()), "text": "Read the error message carefully.", "likes": 0},
#     {"id": str(uuid4()), "text": "Break problems into smaller steps.", "likes": 2},
# ]

tips = []

DATA_FILE = Path(__file__).with_name("tips.json")

if DATA_FILE.exists():
    with open(DATA_FILE, "r") as file:
        tips = json.load(file)

def save_tips():
    with open(DATA_FILE, "w") as file:
        json.dump(tips, file)

@app.get("/")
def index():
    return render_template("index.html", tips=tips)

@app.post("/tips")
def add_tip():
    # TODO: Implement this yourself
    text = request.form["text"].strip()
    if text != "":
        tipDict = {
            "id": str(uuid4()),
            "text": text,
            "likes": 0,
            "dislikes": 0
        }
        tips.append(tipDict)
    save_tips()
    return redirect("/")

@app.post("/tips/<tip_id>/like")
def like_tip(tip_id):
    # TODO: Implement this yourself
    for tip in tips:
        if tip["id"] == tip_id:
            tip["likes"] += 1
    save_tips()
    return redirect("/")

@app.post("/tips/<tip_id>/dislike") # added dislike function
def dislike_tip(tip_id):
    # TODO: Implement this yourself
    for tip in tips:
        if tip["id"] == tip_id:
            tip["dislikes"] += 1
    save_tips()
    return redirect("/")

@app.post("/tips/<tip_id>/delete")
def delete_tip(tip_id):
    # TODO: Implement this yourself
    for tip in tips:
        if tip["id"] == tip_id:
            tips.remove(tip)
            break
    save_tips()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
