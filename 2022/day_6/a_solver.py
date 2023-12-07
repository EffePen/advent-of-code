
with open('a_input.txt') as f:
    input_txt = f.read()

paket_len = 14
for idx in range(len(input_txt)-3):
    substr = input_txt[idx:idx+paket_len]
    if len(set(substr)) == len(substr):
        print(idx+paket_len)
        break

if __name__ == "__main__":
    pass
