Act as an expert Python developer and UI/UX designer.

Project Objective:
I want to build a simple, single-page web application using Streamlit and the Google Gemini API (google-generativeai). The app will act as an "AI Hari Raya Greeting Generator" to create customized Eid al-Fitri wishes.

Core Features & UI Requirements:

1. Title & Description: A festive header (e.g., "✨ AI Hari Raya Greeting Generator").

2. User Inputs:

    A text input field for the "Recipient's Name".

    A dropdown menu or radio buttons for the "Tone of Voice". Options should include: Formal, Funny, Poetic (Pantun style), and Casual.

    An optional text input for "Specific Details" (e.g., "Apologize for not visiting this year", "Mention the delicious Rendang").

3. Action Button: A "Generate Greeting" button.

4. Output Display: A visually distinct container (like st.success or a styled markdown box) to display the generated message cleanly.

Technical Requirements:

- API Integration: Use the gemini-1.5-flash model for fast text generation. Read the API key securely using the python-dotenv package and os.getenv.

- Prompt Engineering Logic: Construct a prompt within the code that takes the user inputs and instructs the Gemini model to write a culturally accurate Hari Raya greeting. The model should be instructed to output a natural mix of Malay and English, capturing the authentic festive vibe.

- Cloud-Ready Deployment: Ensure the code is clean, modular, and handles state correctly, as I plan to deploy this application on a GCP Virtual Machine once testing is complete.

Expected Output from You:
Please provide the complete, copy-pasteable code for the following files:

app.py (The main Streamlit application code, properly commented and structured).

requirements.txt (All necessary dependencies, specifically streamlit, google-generativeai, and python-dotenv).

.env.example (A template showing how to structure the hidden environment variables).

Please also include brief terminal commands on how to run the app locally.