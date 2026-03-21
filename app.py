import streamlit as st
import os
from google import genai
from google.genai import types
import api_key

os.environ["GEMINI_API_KEY"] = api_key.GEMINI_API_KEY


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
if __name__ == "__main__":
    generate()

st.set_page_config(page_title="AI Assistant", page_icon=":robot:")

st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=200)
st.title("vital image analytics")

st.subheader("Your AI Assistant for Image Analysis")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])    

submit_button = st.button("Analyze Image")

if submit_button:
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("Analyzing the image...")
        # Here you can add your image analysis code and display results
    else:
        st.warning("Please upload an image to analyze.")

