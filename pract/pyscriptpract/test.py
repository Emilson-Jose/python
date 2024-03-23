import random
from pyscript import document

def printRandom(event):
    output = document.querySelector("#output")
    output.innerText = random.randint(0,100)