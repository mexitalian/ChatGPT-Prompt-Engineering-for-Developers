```markdown
## Why
Understanding how to infer sentiment and extract information from text is crucial for improving customer insights and enhancing user experience in various applications.

## How
By utilizing large language models, users can quickly generate results through simple prompts, eliminating the need for extensive model training and deployment.

## What
The lesson covers techniques for sentiment analysis, emotion extraction, and information retrieval from text using prompts, enabling efficient natural language processing tasks.

## Cheatsheet

- **Sentiment Analysis**
  - Write a prompt asking for sentiment classification (e.g., "What is the sentiment of the following product review?").
    - **Reason:** This allows for quick sentiment identification without model training.
    - **Example:** "The sentiment of the product review is positive."
  - Modify the prompt for concise responses (e.g., "Respond with 'positive' or 'negative'.").
    - **Reason:** Simplifies output for easier processing.
    - **Example:** Output is "positive."

- **Emotion Extraction**
  - Create a prompt to identify emotions expressed in a review (e.g., "Identify a list of emotions...").
    - **Reason:** Helps understand customer feelings towards products.
    - **Example:** Extracted emotions could include "satisfaction, happiness, contentment."
  - Ask specific questions about emotional states (e.g., "Is the writer expressing anger?").
    - **Reason:** Prioritizes customer support responses based on emotional cues.
    - **Example:** Output is "false."

- **Information Extraction**
  - Prompt for specific items and brands in a review (e.g., "Identify the item purchased and the company.").
    - **Reason:** Useful for summarizing reviews and tracking trends.
    - **Example:** Output as JSON: `{"Item": "lamp", "Brand": "Lumina"}`.
  - Combine multiple extraction requests into one prompt.
    - **Reason:** Streamlines the process and reduces the number of API calls.
    - **Example:** Output includes sentiment, anger, item, and brand in one JSON response.

- **Topic Inference**
  - Use prompts to extract topics from longer texts (e.g., "Determine five topics discussed in the following text.").
    - **Reason:** Helps categorize and index content efficiently.
    - **Example:** Topics extracted could include "NASA, job satisfaction, government."
  - Implement zero-shot learning by asking if topics are covered in a text.
    - **Reason:** Allows for flexible topic identification without labeled training data.
    - **Example:** Output is a list indicating presence of topics.

## Quotes
"In just a few minutes, you can build multiple systems for making inferences about text that previously just would have taken days or even weeks."
```