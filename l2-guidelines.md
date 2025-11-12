```markdown
## Why
Effective prompting is crucial for obtaining accurate and relevant outputs from language models, enhancing user experience and productivity in various applications.

## How
This is achieved by writing clear, specific instructions and allowing the model time to think, which leads to better reasoning and more accurate responses.

## What
The lesson covers principles and tactics for prompt engineering, including using delimiters, structured outputs, and few-shot prompting to guide model behavior effectively.

## Cheatsheet
- **Write clear and specific instructions**
  - **Reason:** Clarity reduces irrelevant responses.
  - **Example:** Use delimiters like triple backticks to define text sections.

- **Ask for structured output**
  - **Reason:** Structured formats like JSON simplify parsing.
  - **Example:** Request outputs in JSON format for easy integration.

- **Check conditions before task completion**
  - **Reason:** Ensures assumptions are met before proceeding.
  - **Example:** Instruct the model to confirm if instructions are present.

- **Use few-shot prompting**
  - **Reason:** Provides context through examples for consistent responses.
  - **Example:** Show examples of desired outputs before the main task.

- **Specify steps for complex tasks**
  - **Reason:** Breaks down tasks for better model understanding.
  - **Example:** Outline multiple actions in a single prompt.

- **Instruct the model to reason before concluding**
  - **Reason:** Encourages thorough analysis and reduces errors.
  - **Example:** Ask the model to solve a problem before evaluating a student's solution.

- **Reduce hallucinations by referencing text**
  - **Reason:** Tracing answers back to sources minimizes inaccuracies.
  - **Example:** Ask the model to find quotes from a text before answering questions.

## Quotes
> "Don't confuse writing a clear prompt with writing a short prompt."  
> "If you give a model a task that's too complex... it may make up a guess which is likely to be incorrect."  
> "Make sure to kind of use some of the techniques that we've gone through to try and avoid this."
```