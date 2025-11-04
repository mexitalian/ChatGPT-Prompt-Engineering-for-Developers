# 🧠 ChatGPT Prompt Engineering for Developers

This notebook explores prompt design techniques inspired by DeepLearning.AI's course.
It includes examples, experiments, and reusable templates.

## Notes on using the OpenAI API

To install the OpenAI Python library:
```
!pip install openai
```

The library needs to be configured with your account's secret key, which is available on the [website](https://platform.openai.com/account/api-keys). 

You can either set it as the `OPENAI_API_KEY` environment variable before using the library:
 ```
 !export OPENAI_API_KEY='sk-...'
 ```

Or, set `openai.api_key` to its value:

```
import openai
openai.api_key = "sk-..."
```