import gradio as gr
import pickle as pick
import numpy as np

# Load the scaler and the model
scalar = pick.load(open('scaler.pkl', 'rb'))  # The scaler
model = pick.load(open('regressor.pkl', 'rb'))  # The trained model


def calculate_gold_rate(usd_inr):
    # Reshape input to a 2D array, with a single value and no feature names
    scaled_input = scalar.transform(np.array(usd_inr).reshape(1,-1))  # Note the double brackets for a 2D array
    # Predict using the model
    return model.predict(scaled_input)[0][0].round(3)  # Corrected .round method


# Set up the Gradio interface
app = gr.Interface(
    fn=calculate_gold_rate,
    inputs=['number'],
    outputs=['number'],
    title='Shows the price of 1 gram of gold in INR based on the current USD/INR exchange rate.'
)

# Launch the app
app.launch(share=True)
