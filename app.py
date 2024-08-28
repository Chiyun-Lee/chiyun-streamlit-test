import streamlit as st
import streamlit.components.v1 as components

def inject_gtag(gtag_id, height=0, width=0, scrolling=False, display=True):
    """
    Injects Google Tag (gtag.js) into the Streamlit app.
    
    Parameters:
        gtag_id (str): Your Google Tag Manager ID (e.g., 'G-XXXXXXXXXX').
        height (int): The height of the HTML component. Default is 0 to minimize space usage.
        width (int): The width of the HTML component. Default is 0 to minimize space usage.
        scrolling (bool): Whether to allow scrolling within the HTML component. Default is False.
        display (bool): If False, the script will not be injected. Default is True.
    """
    if not display:
        return  # Skip injection if display is set to False

    components.html(
        f'''
        <script>
          // Create the script tag
          var gtagScript = document.createElement('script');
          gtagScript.async = true;
          gtagScript.src = "https://www.googletagmanager.com/gtag/js?id={gtag_id}";
          document.head.appendChild(gtagScript);

          // Initialize Google Analytics
          gtagScript.onload = function() {{
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{gtag_id}');
          }};
        </script>
        ''',
        height=height,
        width=width,
        scrolling=scrolling
    )

# Example usage:
inject_gtag('G-5PQ2K3S5JG')



if st.button("toast"):
    st.toast("toast")