import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString, Tag

# Load the epub book
book = epub.read_epub('input.epub')

# Loop through all the items
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        
        # Make the first N letters of each word bold, depending on word length
        for text_node in soup.find_all(text=True):
            if isinstance(text_node, NavigableString):
                words = text_node.split(' ')
                for i in range(len(words)):
                    if len(words[i]) > 0:
                        word_soup = BeautifulSoup('', 'html.parser')
                        bold_tag = word_soup.new_tag('b')
                        if len(words[i]) < 3:
                            bold_tag.string = words[i][:1]
                            word_soup.append(bold_tag)
                            word_soup.append(words[i][1:])
                        elif len(words[i]) < 5:
                            bold_tag.string = words[i][:2]
                            word_soup.append(bold_tag)
                            word_soup.append(words[i][2:])
                        elif len(words[i]) < 8:
                            bold_tag.string = words[i][:3]
                            word_soup.append(bold_tag)
                            word_soup.append(words[i][3:])
                        else:
                            bold_tag.string = words[i][:4]
                            word_soup.append(bold_tag)
                            word_soup.append(words[i][4:])
                        words[i] = word_soup
                new_text_node = BeautifulSoup('', 'html.parser')
                for word in words:
                    new_text_node.append(word)
                    new_text_node.append(' ')
                text_node.replace_with(new_text_node)
        
        # Update the content of the item
        item.set_content(str(soup).encode('utf-8'))  # Make sure to encode the string into bytes

# Write the book back to a file
epub.write_epub('book_modified.epub', book)
