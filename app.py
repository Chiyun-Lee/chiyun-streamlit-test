import streamlit as st

from streamlit_gtag import st_gtag

st_gtag(
    key="gtag_send_event_a",
    id="G-5PQ2K3S5JG",
    event_name="app_main_page"
)


if st.button("hello"):
    st.toast("hi")
    
    st_gtag(
        key="gtag_send_event_b",
        id="G-HXSDMRLF54",
        event_name="app_main_page_b"
    )