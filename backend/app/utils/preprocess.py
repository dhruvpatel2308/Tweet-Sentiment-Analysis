from tensorflow.keras.preprocessing.text import tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_text(text, tokenizer, max_len=32):
    sequence= tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len)
    return padded_sequence