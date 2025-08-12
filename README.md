# langextract

Implementation of langextract by Google. Extract named entities, custom structured info from unstructured text. Think of it like NER in LLM world.

Input:

<img width="670" height="477" alt="image" src="https://github.com/user-attachments/assets/9b9a6ae4-e7cd-42e7-873f-d960c85a4d66" />

Output:

<img width="1265" height="496" alt="image" src="https://github.com/user-attachments/assets/b15a59c1-62da-4d52-b4c4-cff9010e6883" />


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
