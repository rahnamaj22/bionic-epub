## Bionic Reading Python Script

Bionic Reading is a reading technique that enhances the reading experience and comprehension by visually highlighting certain parts of words. The idea is to support the human reading behaviour by making the first few characters, especially of long words, bold to enhance the visual anchor. This assists in easier word recognition, helps reduce reading errors, and improves understanding.

This Python script modifies an ePub ebook file to apply Bionic Reading style to the text. This script uses the `ebooklib` library to handle the ePub file and `BeautifulSoup` to parse and modify the HTML content of the ebook.

## Script Overview

1.  **Import Required Libraries**: The script begins by importing necessary libraries - `ebooklib` for handling ePub files and `BeautifulSoup` for parsing and modifying HTML.
    
2.  **Load the ePub Book**: The `epub.read_epub('input.epub')` function is used to load the ePub file.
    
3.  **Process Each Item in the Book**: The script then loops through each item in the book. If the item is a document (i.e., contains text), it is further processed.
   
4.  **Parse and Modify HTML**: The content of each document item is parsed with BeautifulSoup. For each text node in the HTML, the script splits the text into words and modifies each word based on its length. If the word length is less than 3, the first letter is made bold. If the length is between 3 and 4, the first two letters are made bold. If the length is between 5 and 7, the first three letters are made bold. For words with a length of 8 or more, the first four letters are made bold.
   
5.  **Update the Item Content**: After the modifications, the content of the item is updated with the new HTML.
   
6.  **Write the Book Back to a File**: Finally, the script writes the modified book back to a file named 'book_modified.epub'.  

---

## Usage

To use this script, simply run it in a Python environment where the `ebooklib` and `BeautifulSoup` libraries are installed. Make sure to place the ePub file you wish to modify in the same directory as the script and name it 'input.epub'.

**Please note:** This script will modify the entire ePub book, so it is recommended to use a copy of your original book to avoid losing the original formatting.

---

## Dependencies

-   Python 3
-   `ebooklib`
-   `BeautifulSoup`

To install dependencies, use pip:

Copy code

```
pip install ebooklib beautifulsoup4
```

---

## Contribution

Feel free to fork this repository and enhance the code. Any contributions you make are greatly appreciated.

---

**Disclaimer:** Please note that the Bionic Reading technique might not be suitable for all types of reading materials or for all readers. Always consider your audience and the nature of the text before applying this technique.

# DISCLAIMER

This project is intended strictly for educational and personal testing purposes. It is not affiliated with, endorsed by, or connected to Bionic Reading® or any other third-party. This project does not use any of Bionic Reading®'s proprietary software, APIs, or copyrighted material.

The code in this repository takes an epub file as input and applies formatting to certain characters of each word in the epub file. The purpose of this modification is to experiment with different reading techniques and to observe their impact on readability and comprehension.

## Usage of this Code

This code is provided for personal, non-commercial use only. By using this code, you agree to use it in a manner that complies with all applicable laws, including, but not limited to, copyright and trademark laws.

If you believe any content in this repository infringes your legal rights, please contact the repository owner with detailed information.


