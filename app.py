from dataclasses import dataclass
from typing import List

from flask import Flask, render_template, request


@dataclass
class EcoOption:
    """Represents a sustainable supplier and product alternatives."""

    company: str
    country: str
    website: str
    category: str
    replaces: List[str]
    materials: List[str]
    notes: str


CATEGORY_LABELS = {
    "furniture": "Furniture",
    "silverware": "Silverware & Tableware",
    "packaging": "Packaging Materials",
    "plastic-materials": "Plastic Alternatives",
    "clean-power": "Clean Power & Energy",
    "cleaning-supplies": "Cleaning Supplies",
    "office-supplies": "Office Supplies",
    "textiles": "Textiles & Apparel",
    "food-service": "Food Service",
}


ECO_OPTIONS: List[EcoOption] = [
    EcoOption(
        company="Biofase",
        country="Mexico",
        website="https://biofase.com.mx",
        category="silverware",
        replaces=["plastic forks", "plastic spoons", "plastic knives", "single-use cutlery"],
        materials=["avocado pits", "biopolymer"],
        notes="Turns avocado seed waste into compostable cutlery and straws.",
    ),
    EcoOption(
        company="Ecovative",
        country="United States",
        website="https://ecovative.com",
        category="packaging",
        replaces=["foam packaging", "plastic trays", "protective shipping foam"],
        materials=["mycelium", "agricultural waste"],
        notes="Makes mushroom-based packaging that can replace plastic foam.",
    ),
    EcoOption(
        company="Notpla",
        country="United Kingdom",
        website="https://www.notpla.com",
        category="food-service",
        replaces=["plastic sauce packets", "plastic-lined food boxes", "single-use films"],
        materials=["seaweed", "plant fiber"],
        notes="Produces seaweed-based packaging that naturally breaks down.",
    ),
    EcoOption(
        company="TIPA",
        country="Israel",
        website="https://tipa-corp.com",
        category="plastic-materials",
        replaces=["plastic produce bags", "plastic flexible packaging"],
        materials=["compostable polymers"],
        notes="Creates compostable flexible packaging for food and retail.",
    ),
    EcoOption(
        company="Green Ocean Trading",
        country="United States",
        website="https://www.greenoceantrading.com",
        category="silverware",
        replaces=["plastic cups", "disposable plates", "plastic utensils"],
        materials=["palm leaf", "bagasse", "bamboo"],
        notes="Provides compostable tableware for restaurants and events.",
    ),
    EcoOption(
        company="Inside Weather",
        country="United States",
        website="https://insideweather.com",
        category="furniture",
        replaces=["conventional particleboard furniture", "synthetic-fabric sofas"],
        materials=["FSC-certified wood", "recycled textiles"],
        notes="Builds modern furniture with lower-impact materials and domestic production.",
    ),
    EcoOption(
        company="Avocado",
        country="United States",
        website="https://www.avocadogreenmattress.com",
        category="furniture",
        replaces=["traditional polyurethane mattresses", "synthetic bedding"],
        materials=["organic latex", "organic cotton", "wool"],
        notes="Offers certified organic mattresses and furniture pieces.",
    ),
    EcoOption(
        company="EcoEnclose",
        country="United States",
        website="https://www.ecoenclose.com",
        category="packaging",
        replaces=["virgin plastic mailers", "new corrugated shipping boxes"],
        materials=["recycled cardboard", "recycled polyethylene"],
        notes="Shipping packaging focused on high recycled content and right-sizing.",
    ),
    EcoOption(
        company="Sustainable Office Solutions",
        country="United States",
        website="https://sustainableofficesolutions.com",
        category="office-supplies",
        replaces=["virgin copy paper", "disposable office products"],
        materials=["post-consumer recycled paper", "recycled plastics"],
        notes="Carries greener office products for startups and small teams.",
    ),
    EcoOption(
        company="Who Gives A Crap",
        country="Australia",
        website="https://us.whogivesacrap.org",
        category="office-supplies",
        replaces=["traditional tissue and paper towels"],
        materials=["bamboo", "recycled paper"],
        notes="Sells plastic-free wrapped tissue products suitable for workplaces.",
    ),
    EcoOption(
        company="Blueland",
        country="United States",
        website="https://www.blueland.com",
        category="cleaning-supplies",
        replaces=["single-use plastic cleaner bottles", "conventional detergent packaging"],
        materials=["reusable bottles", "tablet refills"],
        notes="Refillable cleaning systems designed to reduce plastic waste.",
    ),
    EcoOption(
        company="Dropps",
        country="United States",
        website="https://www.dropps.com",
        category="cleaning-supplies",
        replaces=["liquid detergents in plastic jugs"],
        materials=["dissolvable pods", "cardboard packaging"],
        notes="Low-waste laundry and dishwasher detergents with compostable shipping.",
    ),
    EcoOption(
        company="Allbirds",
        country="United States",
        website="https://www.allbirds.com",
        category="textiles",
        replaces=["petroleum-based uniform footwear"],
        materials=["merino wool", "eucalyptus fiber", "sugarcane EVA"],
        notes="Lower-carbon shoes and apparel useful for staff uniforms.",
    ),
    EcoOption(
        company="Pact",
        country="United States",
        website="https://wearpact.com",
        category="textiles",
        replaces=["conventional cotton workwear"],
        materials=["organic cotton", "Fair Trade textiles"],
        notes="Organic basics and apparel options for branded team clothing.",
    ),
    EcoOption(
        company="Arcadia",
        country="United States",
        website="https://www.arcadia.com",
        category="clean-power",
        replaces=["fossil-fuel-heavy utility energy mix"],
        materials=["community solar credits", "renewable energy plans"],
        notes="Helps small businesses access community solar and clean energy programs.",
    ),
    EcoOption(
        company="Goal Zero",
        country="United States",
        website="https://www.goalzero.com",
        category="clean-power",
        replaces=["gas generators for backup power"],
        materials=["solar panels", "portable battery storage"],
        notes="Portable renewable backup energy systems for storefronts and events.",
    ),
]


app = Flask(__name__)


def tokenize(text: str) -> List[str]:
    return [word.strip().lower() for word in text.replace(",", " ").split() if word.strip()]


def option_matches(option: EcoOption, query_tokens: List[str]) -> bool:
    haystack = " ".join(
        [
            option.company,
            option.country,
            option.website,
            option.category,
            option.notes,
            " ".join(option.replaces),
            " ".join(option.materials),
        ]
    ).lower()
    return all(token in haystack for token in query_tokens)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", categories=CATEGORY_LABELS)


@app.route("/catalog", methods=["GET"])
def catalog():
    query = request.args.get("q", "").strip()
    selected_category = request.args.get("category", "").strip().lower()

    filtered = ECO_OPTIONS
    if selected_category and selected_category in CATEGORY_LABELS:
        filtered = [option for option in filtered if option.category == selected_category]

    if query:
        tokens = tokenize(query)
        filtered = [option for option in filtered if option_matches(option, tokens)]

    selected_label = CATEGORY_LABELS.get(selected_category, "All Categories")

    return render_template(
        "index.html",
        options=filtered,
        query=query,
        searched=bool(query),
        categories=CATEGORY_LABELS,
        selected_category=selected_category,
        selected_label=selected_label,
    )


if __name__ == "__main__":
    app.run(debug=True)
