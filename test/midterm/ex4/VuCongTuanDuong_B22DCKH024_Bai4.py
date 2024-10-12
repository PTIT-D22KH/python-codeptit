import matplotlib.pyplot as plt
from collections import Counter
import re

def process_text(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count word frequencies
    word_freq = Counter(words)
    
    # Sort the dictionary by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_freq

def plot_histogram(word_freq):
    # Extract words and their frequencies
    words = list(word_freq.keys())
    frequencies = list(word_freq.values())
    
    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title('Word Frequency Histogram')
    plt.xticks(rotation=90)
    plt.show()

def main():
    # Input text
    text = input("Enter the text: ")
    
    # Process the text
    word_freq = process_text(text)
    
    # Print the sorted word frequencies
    print("Word Frequencies (sorted):")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
    
    # Plot the histogram
    plot_histogram(word_freq)

if __name__ == "__main__":
    main()