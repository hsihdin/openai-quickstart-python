import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    print("iii")
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=200,
        )
        print(response.choices)
        # result_names = response.choices[0].text.strip()  # Get the generated text from the API response
        #     # result_food = response.choices[1].text.strip()  # Get the generated text from the API response
        # names = parse_result(result_names)
        # # foods = parse_result(result_food)
        # print(result)
        # print(names)
        # print(foods)
        return render_template("index.html", names=None, foods=None)



def generate_name_prompt(animal):
    return f"""Suggest three names for an animal.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline

Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot

Animal: {animal.capitalize()}
Names:"""

def generate_food_prompt(animal):
    return f"""Suggest three foods that the animal likes.

Animal: Cat
Foods: Fish, Chicken, Milk

Animal: Dog
Foods: Beef, Bacon, Peanut Butter

Animal: {animal.capitalize()}
Foods:"""

def generate_prompt(animal):
    name_prompt = generate_name_prompt(animal)
    food_prompt = generate_food_prompt(animal)
    return f"{name_prompt}\n{food_prompt}"



 

import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_name_prompt(animal),
            temperature=0.6,
            max_tokens=200,
        )
        result = response.choices[0].text
        names = result

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_food_prompt(animal),
        temperature=0.6,
        max_tokens=200,
        )
        result = response.choices[0].text
        foods = result

#BREED INFORMATION
        result = response.choices[0].text
        names = result
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_food_prompt(animal),
        temperature=0.6,
        max_tokens=200,
        )
        result = response.choices[0].text
        breeds = result

        # return render_template("index.html", names=names, foods=None)

    return render_template("index.html", names=names, foods=foods , breeds=breeds)



def generate_name_prompt(animal):
    return f"""Suggest three names for an animal.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline

Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot

Animal: {animal.capitalize()}
Names:"""

def generate_food_prompt(animal):
    return f"""Suggest three foods that the animal likes.

Animal: Cat
Foods: Fish, Chicken, Milk

Animal: Dog
Foods: Beef, Bacon, Peanut Butter

Animal: {animal.capitalize()}
Foods:"""

def generate_breed_prompt(animal):
    return f"""Suggest five popular breeds of an animal.

Animal: Cat
Breeds: Maine Coon, Siamese, Persian, Bengal, Ragdoll

Animal: Dog
Breeds: Labrador Retriever, German Shepherd, Golden Retriever, Bulldog, Poodle

Animal: {animal.capitalize()}
Breeds:"""


def generate_prompt(animal):
    name_prompt = generate_name_prompt(animal)
    # food_prompt = generate_food_prompt(animal)
    food_prompt = None  

    return f"{name_prompt}\n{food_prompt}"



 

def parse_result(result):
    print(result)
    lines = result.split("\n")
    names = [name.strip() for name in lines[7:10] if name.strip()]
    foods = [food.strip() for food in lines[14:17] if food.strip()]
    return names, foods




if __name__ == "__main__":
    app.run()


