from __future__ import annotations

import pandas as pd
import streamlit as st

from src.data_loader import load_products, load_users
from src.service import GiftRecommendationService

st.set_page_config(page_title="RAG Gift Recommendation Demo", page_icon="🎁", layout="wide")

service = GiftRecommendationService()
users = load_users()
user_lookup = {f"{u['name']} ({u['user_id']})": u["user_id"] for u in users}
products_df = load_products()

st.title("🎁 RAG E-commerce Gift Recommendation System")
st.caption("Portfolio demo: retrieval + reranking + explainable generation for gift recommendations")

with st.sidebar:
    st.header("Scenario setup")
    gifter_label = st.selectbox("Gifter", list(user_lookup.keys()), index=0)
    recipient_label = st.selectbox("Recipient", list(user_lookup.keys()), index=1)
    occasion = st.selectbox("Occasion", ["birthday", "holiday", "anniversary", "selfcare", "casual"])
    min_budget, max_budget = st.slider("Budget", min_value=10, max_value=120, value=(20, 80), step=5)
    top_k = st.slider("Number of ideas", min_value=3, max_value=8, value=5)
    run = st.button("Generate recommendations", type="primary")

left, right = st.columns([1.2, 1])

with left:
    st.subheader("How the prototype works")
    st.markdown(
        """
1. Build a retrieval query from recipient preferences, browsing, purchase history, occasion, and budget.  
2. Retrieve semantically similar products from the catalog.  
3. Rerank results using style match, occasion fit, budget fit, and social closeness.  
4. Generate explainable gift recommendations for the shopper.
"""
    )
    st.subheader("Product catalog sample")
    st.dataframe(products_df[["product_id", "title", "category", "price", "style_tags"]], use_container_width=True)

with right:
    st.subheader("Recipient snapshot")
    recipient_id = user_lookup[recipient_label]
    recipient = next(u for u in users if u["user_id"] == recipient_id)
    st.json(
        {
            "liked_styles": recipient["liked_styles"],
            "favorite_colors": recipient["favorite_colors"],
            "recent_browsing": recipient["recent_browsing"],
            "purchase_history": recipient["purchase_history"],
        }
    )

if run:
    gifter_id = user_lookup[gifter_label]
    recipient_id = user_lookup[recipient_label]
    response = service.recommend(gifter_id, recipient_id, occasion, (min_budget, max_budget), top_k=top_k)

    st.divider()
    st.subheader("Generated summary")
    st.success(response["generated_recommendation"]["summary"])
    st.caption(f"Generator: {response['generated_recommendation']['model_used']}")

    st.subheader("Retrieved and reranked products")
    retrieved = pd.DataFrame(response["retrieved_products"])
    st.dataframe(
        retrieved[["product_id", "title", "price", "style_tags", "retrieval_score"]],
        use_container_width=True,
    )

    st.subheader("Recommendation cards")
    for card in response["generated_recommendation"]["cards"]:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {card['title']}")
                st.write(card["reason"])
            with col2:
                st.metric("Score", card["score"])
                st.write(f"Price: ${card['price']}")
                st.link_button("Open product", card["url"])

    st.subheader("Debug: retrieval query")
    st.code(response["query"], language="text")
else:
    st.info("Choose a scenario in the sidebar, then click **Generate recommendations**.")
