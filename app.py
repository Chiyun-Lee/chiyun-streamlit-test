import streamlit as st

from streamlit_gtag import st_gtag

if st.button("hello"):
    st_gtag(
        key="gtag_send_event_a",
        id="G-4XZZ9XXZ21",
        event_name="app_main_page",
        params={
            "event_category": "test_category_a",
            "event_label": "test_label_a",
            "value": 97,
        },
    )