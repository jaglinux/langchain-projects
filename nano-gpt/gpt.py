import torch

with open("./nano-gpt/tinyshakespeare.txt", 'r', encoding='utf-8') as f:
    data = f.read()

vocab = "".join(sorted(set(data)))
vocab_size = len(vocab)
print(vocab, vocab_size)

char2vector = {j:i for i,j in enumerate(vocab)}
print(char2vector)

vector2char = {i:j for i, j in enumerate(vocab)}
print(vector2char)

def encode(a):
    vector = []
    for i in a:
        vector.append(char2vector[i])
    return vector

def decode(vector):
    a = ""
    for i in vector:
        a += vector2char[i]
    return a

temp = encode("hii there")
print(temp)
temp = decode(temp)
print(temp)
assert temp == "hii there"

data_vector = encode(data)
data_vector = torch.tensor(data_vector, dtype=torch.long)
print(data_vector, len(data_vector), data_vector.shape, data_vector.dim())
