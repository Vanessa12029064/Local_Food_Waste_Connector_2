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
        company="The Wheat Straw Co.",
        country="United Kingdom",
        website="https://thewheatstrawco.co.uk",
        replaces=["plastic straws", "single-use straws"],
        materials=["wheat stem", "plant fiber"],
        notes="Produces disposable drinking straws made from natural wheat stems.",
    ),
    EcoOption(
        company="PlantSwitch",
        country="United States",
        website="https://www.plantswitch.com",
        replaces=["single-use straws", "plastic utensils", "disposable tableware"],
        materials=["upcycled plant fiber", "biopolymers"],
        notes="Manufactures compostable straws and utensils from upcycled agricultural waste.",
    ),
    EcoOption(
        company="NatureWorks",
        country="United States",
        website="https://www.natureworksllc.com",
        replaces=["petroleum plastic", "plastic cups", "plastic food packaging"],
        materials=["PLA biopolymer", "plant sugars"],
        notes="Makes Ingeo PLA biopolymer used in compostable packaging and food service items.",
    ),
    EcoOption(
        company="New Starch Solutions",
        country="United States",
        website="https://newstarch.com",
        replaces=["expanded polystyrene", "foam packaging", "plastic loose fill"],
        materials=["starch", "compostable biobased blends"],
        notes="Develops starch-based foam alternatives for protective packaging.",
    ),
    EcoOption(
        company="EcoEnclose",
        country="United States",
        website="https://www.ecoenclose.com",
        replaces=["virgin plastic mailers", "bubble mailers", "ecommerce packaging"],
        materials=["recycled paper", "recycled plastic", "compostable materials"],
        notes="Supplies recycled and recyclable ecommerce mailers and shipping packaging.",
    ),
    EcoOption(
        company="Vegware",
        country="United Kingdom",
        website="https://www.vegware.com",
        replaces=["plastic food containers", "plastic cups", "single-use foodservice ware"],
        materials=["plant-based materials", "compostable polymers"],
        notes="Provides compostable foodservice packaging for restaurants and events.",
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
        company="Cove",
        country="United States",
        website="https://cove.eco",
        replaces=["plastic water bottles", "single-use beverage bottles"],
        materials=["PHA", "biopolymers"],
        notes="Develops biodegradable bottled water packaging made from biopolymers.",
    ),
    EcoOption(
        company="Better Packaging Co.",
        country="New Zealand",
        website="https://www.betterpackaging.com",
        replaces=["plastic courier bags", "poly mailers", "shipping satchels"],
        materials=["compostable bioplastics", "recycled materials"],
        notes="Offers compostable shipping mailers and sustainable ecommerce packaging.",
    ),
    EcoOption(
        company="noissue",
        country="United States",
        website="https://noissue.co",
        replaces=["branded plastic packaging", "custom mailers", "packaging tissue"],
        materials=["recycled paper", "compostable mailers", "soy inks"],
        notes="Creates custom sustainable packaging for small and local businesses.",
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
    EcoOption(
        company="Steelcase",
        country="United States",
        website="https://www.steelcase.com",
        replaces=["conventional office furniture", "high-waste office furnishings"],
        materials=["recycled metal", "recycled plastic", "responsibly sourced wood"],
        notes="Designs office furniture with circularity and material transparency programs.",
    ),
    EcoOption(
        company="Humanscale",
        country="United States",
        website="https://www.humanscale.com",
        replaces=["standard office chairs", "non-sustainable office furniture"],
        materials=["recycled components", "durable low-impact materials"],
        notes="Builds ergonomic office furniture with a focus on long lifespan and low footprint.",
    ),
    EcoOption(
        company="Davies Office",
        country="United States",
        website="https://www.daviesoffice.com",
        replaces=["new office desks", "new office chairs", "disposable office furniture"],
        materials=["remanufactured furniture", "reused components"],
        notes="Remanufactures office furniture to extend product life and reduce waste.",
    ),
    EcoOption(
        company="Oakywood",
        country="Poland",
        website="https://oakywood.shop",
        replaces=["plastic desk accessories", "mass-produced office organizers"],
        materials=["solid wood", "cork", "felt"],
        notes="Offers sustainably crafted wooden desk accessories and workspace products.",
    ),
    EcoOption(
        company="Twigs Paper",
        country="United States",
        website="https://twigspaper.com",
        replaces=["virgin paper cards", "conventional greeting cards"],
        materials=["recycled paper", "tree-free paper options"],
        notes="Sells eco-friendly stationery and paper gifts made with recycled content.",
    ),
    EcoOption(
        company="A Good Company",
        country="Sweden",
        website="https://agood.com",
        replaces=["plastic phone cases", "single-use notebooks", "high-impact lifestyle products"],
        materials=["plant-based plastics", "stone paper", "recycled materials"],
        notes="Creates low-impact everyday products including plant-based and recycled goods.",
    ),
    EcoOption(
        company="Tree-Free Greetings",
        country="United States",
        website="https://www.tree-free.com",
        replaces=["traditional greeting cards", "virgin paper stationery"],
        materials=["100% post-consumer recycled paper", "chlorine-free processing"],
        notes="Produces greeting cards and office paper goods using recycled, tree-free inputs.",
    ),
    EcoOption(
        company="Clean Cut",
        country="United States",
        website="https://www.cleancutwood.com",
        replaces=["conventional disposable cutlery", "plastic utensils"],
        materials=["FSC-certified wood"],
        notes="Manufactures wooden cutlery as a renewable alternative to plastic utensils.",
    ),
    EcoOption(
        company="Dr. Bronner's",
        country="United States",
        website="https://www.drbronner.com",
        replaces=["synthetic cleaning products", "conventional soaps"],
        materials=["organic oils", "plant-based ingredients", "recycled packaging"],
        notes="Provides plant-based soaps and cleaners with strong environmental and ethical sourcing standards.",
    ),
    EcoOption(
        company="EcoFlow",
        country="United States",
        website="https://www.ecoflow.com/us",
        replaces=["diesel backup generators", "grid-only business power"],
        materials=["battery storage", "portable solar hardware"],
        notes="Offers modular battery and solar systems businesses can deploy without owning a building.",
    ),
    EcoOption(
        company="Common Energy",
        country="United States",
        website="https://www.commonenergy.us",
        replaces=["fossil-fuel grid electricity", "on-site-only solar options"],
        materials=["community solar credits", "clean energy subscriptions"],
        notes="Connects businesses to community solar programs without rooftop installation.",
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
