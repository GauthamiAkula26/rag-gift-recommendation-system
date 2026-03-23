from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd

from src.config import DATA_DIR


def load_products(path: Path | None = None) -> pd.DataFrame:
    product_path = path or DATA_DIR / "products.csv"
    df = pd.read_csv(product_path)
    return df.fillna("")


def load_users(path: Path | None = None) -> List[Dict]:
    user_path = path or DATA_DIR / "users.json"
    return json.loads(user_path.read_text(encoding="utf-8"))


def load_social_graph(path: Path | None = None) -> List[Dict]:
    graph_path = path or DATA_DIR / "social_graph.json"
    return json.loads(graph_path.read_text(encoding="utf-8"))


def get_user(user_id: str) -> Dict:
    users = load_users()
    user = next((u for u in users if u["user_id"] == user_id), None)
    if not user:
        raise ValueError(f"Unknown user_id: {user_id}")
    return user


def get_relationship(source_user_id: str, target_user_id: str) -> Dict:
    relationships = load_social_graph()
    default = {
        "source_user_id": source_user_id,
        "target_user_id": target_user_id,
        "closeness": 0.3,
        "interaction_days_ago": 30,
    }
    return next(
        (
            item
            for item in relationships
            if item["source_user_id"] == source_user_id and item["target_user_id"] == target_user_id
        ),
        default,
    )


def create_product_text(df: pd.DataFrame) -> pd.Series:
    return (
        "Title: " + df["title"] + ". "
        + "Category: " + df["category"] + ". "
        + "Brand: " + df["brand"] + ". "
        + "Price: $" + df["price"].astype(str) + ". "
        + "Styles: " + df["style_tags"] + ". "
        + "Occasions: " + df["occasion_tags"] + ". "
        + "Description: " + df["description"]
    )


def build_user_context(gifter_id: str, recipient_id: str, occasion: str, budget: Tuple[float, float]) -> Dict:
    gifter = get_user(gifter_id)
    recipient = get_user(recipient_id)
    relationship = get_relationship(gifter_id, recipient_id)
    return {
        "gifter": gifter,
        "recipient": recipient,
        "relationship": relationship,
        "occasion": occasion,
        "budget": budget,
    }
