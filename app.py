from dataclasses import dataclass
from typing import List

from flask import Flask, render_template, request


@dataclass
class EcoOption:
    """Represents a sustainable supplier and product alternatives."""

    company: str
    country: str
    website: str
    replaces: List[str]
    materials: List[str]
    notes: str


ECO_OPTIONS: List[EcoOption] = [
    EcoOption(
        company="Biofase",
        country="Mexico",
        website="https://biofase.com.mx",
        replaces=["plastic forks", "plastic spoons", "plastic knives", "single-use cutlery"],
        materials=["avocado pits", "biopolymer"],
        notes="Turns avocado seed waste into compostable cutlery and straws.",
    ),
    EcoOption(
        company="Ecovative",
        country="United States",
        website="https://ecovative.com",
        replaces=["foam packaging", "plastic trays", "protective shipping foam"],
        materials=["mycelium", "agricultural waste"],
        notes="Makes mushroom-based packaging that can replace plastic foam.",
    ),
    EcoOption(
        company="Notpla",
        country="United Kingdom",
        website="https://www.notpla.com",
        replaces=["plastic sauce packets", "plastic-lined food boxes", "single-use films"],
        materials=["seaweed", "plant fiber"],
        notes="Produces seaweed-based packaging that naturally breaks down.",
    ),
    EcoOption(
        company="TIPA",
        country="Israel",
        website="https://tipa-corp.com",
        replaces=["plastic produce bags", "plastic flexible packaging"],
        materials=["compostable polymers"],
        notes="Creates compostable flexible packaging for food and retail.",
    ),
]


app = Flask(__name__)


def tokenize(text: str) -> List[str]:
    """Lowercase + split query into basic words used for keyword matching."""

    return [word.strip().lower() for word in text.replace(",", " ").split() if word.strip()]


def option_matches(option: EcoOption, query_tokens: List[str]) -> bool:
    """Very simple matching: all query tokens must appear in searchable text."""

    haystack = " ".join(
        [
            option.company,
            option.country,
            option.website,
            option.notes,
            " ".join(option.replaces),
            " ".join(option.materials),
        ]
    ).lower()
    return all(token in haystack for token in query_tokens)


@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").strip()

    if not query:
        return render_template("index.html", options=[], query="", searched=False)

    tokens = tokenize(query)
    matches = [option for option in ECO_OPTIONS if option_matches(option, tokens)]

    return render_template("index.html", options=matches, query=query, searched=True)


if __name__ == "__main__":
    app.run(debug=True)
