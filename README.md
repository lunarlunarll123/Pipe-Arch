# Text Cleaning Pipeline  

## 📌 Introduction  
This project implements a **text cleaning pipeline** using **four Python filters** connected through **command-line pipes (`|`)** to **process and enhance text data step by step**.  

### Features:  
✅ **Sentence Splitting** → Detects `.`, `!`, `?` and splits text into sentences  
✅ **Stopword Removal** → Removes common words like `the, is, in, at, which, on`  
✅ **Spell Correction** → Automatically fixes spelling errors (`teh → the`, `recieve → receive`)  
✅ **Sentence Capitalization** → Ensures the first letter of each sentence is capitalized  

---

## 🛠 How to Use  
### 1️⃣ Set Up Python Environment  
**Install dependencies (`textblob` for spell checking):**  
```bash
pip install textblob

type input.txt | python sentence_splitter.py | python remove_stopwords.py | python spell_checker.py | python capitalize_sentences.py

input.txt：

this is an exampel text. teh project is abut txt cleanning! do you recieve the data?

Pipeline Output:

Example text.
The project about text cleaning!
Receive data?
