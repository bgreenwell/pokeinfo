import requests
import streamlit as st

st.set_page_config(page_title="PokeInfo", page_icon="⚡")
st.title("⚡ PokeInfo")

pokemon_name = st.text_input("Enter Pokémon name or ID", value="charizard")

if pokemon_name:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.strip().lower()}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()

            # Pokémon image (official artwork with fallback to standard sprite)
            image_url = (
                data.get("sprites", {})
                .get("other", {})
                .get("official-artwork", {})
                .get("front_default")
                or data.get("sprites", {}).get("front_default")
            )
            if image_url:
                st.image(image_url, width=250)

            # Pokémon details
            st.subheader(data["name"].title())
            st.write(f"**Height:** {data['height']} decimetres")
            st.write(f"**Weight:** {data['weight']} hectograms")
            types = [t["type"]["name"].title() for t in data.get("types", [])]
            st.write(f"**Types:** {', '.join(types)}")
        elif response.status_code == 404:
            st.error(f"Pokémon '{pokemon_name}' not found.")
        else:
            st.error(f"Error: Received status code {response.status_code}")
    except requests.RequestException as e:
        st.error(f"Network error: {e}")
