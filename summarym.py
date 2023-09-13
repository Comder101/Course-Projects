import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ''
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    pdf_file.close()
    return text

pdf_path = 'Operations Management.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_words=500):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    
    word_freq = FreqDist(words)
    sentence_scores = {}
    
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    
    summary_sentences = heapq.nlargest(num_words, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary

summary = summarize_text(pdf_text, num_words=500)
print(summary)

