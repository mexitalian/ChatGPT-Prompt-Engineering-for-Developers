
## Why
Building a custom chatbot enhances user interaction and automates tasks, making processes like customer service more efficient and accessible.

## How
By utilizing the OpenAI Python package, developers can create chatbots that handle multi-turn conversations through structured message inputs and outputs.

## What
The lesson covers setting up the chatbot, defining helper functions, and using system messages to guide the assistant's behavior in conversations.

## Cheatsheet
- **Set up OpenAI Python package**
  - **Reason:** Essential for accessing the chat model functionalities.
  - **Example:** Install using `pip install openai`.

- **Define helper functions**
  - **Reason:** Streamlines the process of sending messages and receiving responses.
  - **Example:** Create a `get_completion` function to handle message inputs.

- **Use system messages to set behavior**
  - **Reason:** Guides the assistant's responses without user awareness.
  - **Example:** "You are a friendly chatbot" sets the tone for interactions.

- **Collect user messages in context**
  - **Reason:** Maintains conversation continuity and context for the model.
  - **Example:** Append user inputs to a list called `context`.

- **Create a JSON summary of orders**
  - **Reason:** Formats the order data for submission to an order system.
  - **Example:** "Create a JSON summary of the previous food order."

## Quotes
- "You could use it to build a custom chatbot with only a modest amount of effort."
- "Each conversation with a language model is a standalone interaction."
- "Feel free to customize it yourself and play around with the system message."
