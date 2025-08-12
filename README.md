# langextract

Implementation of langextract by Google. Extract named entities, custom structured info from unstructured text. Think of it like NER in LLM world.

Input:

<img width="736" height="492" alt="image" src="https://github.com/user-attachments/assets/09c73edb-63eb-4c87-b642-672653d8caf4" />


Output:

<img width="1263" height="495" alt="image" src="https://github.com/user-attachments/assets/9d02ffe8-9c5a-4810-99b9-f030d3136bb2" />


## Overview

It is designed for business and research use cases where structured information needs to be pulled from unstructured documents.  
Details: [https://pypi.org/project/langextract/](https://pypi.org/project/langextract/)

## Steps

1. **Clone the repo**
   ```sh
   git clone https://github.com/notnotrishi/langextract.git
   cd langextract
   ```

2. **Install dependencies**
   ```sh
   pip install langextract
   ```

3. **Add your Gemini API key in `main.py`**
   - Open `main.py`
   - Replace `'API_KEY'` with your actual Gemini API key

4. **Change `input.txt` and examples in `main.py` if needed, and run it**
   - Edit `input.txt` with your desired input text
   - (Optional) Adjust example data in `main.py` for your use case
   - Run the script:
     ```sh
     python main.py
     ```

## License

MIT License

---
