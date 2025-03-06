class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text, key):
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt_text(self, text, key):
        num_columns = int(len(text) / key)
        num_rows = key
        num_shaded_boxes = (num_columns * num_rows) - len(text)
        
        decrypted_text = [''] * num_columns
        col = 0
        row = 0
        
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            
            if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        return ''.join(decrypted_text)
