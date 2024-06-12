import os
from typing import List
from heap import minHeap, Node
from binary_tree import BinaryTree


class HuffmanCode:
    def __init__(self, path: str):
        self.path = path
        self.code_dict = {}

    def __Build_Frequency_From_Text(self, text: str) -> dict:
        freq_dict = {}
        for char in text:
            if char in freq_dict:
                freq_dict[char] = freq_dict[char] + 1
            else:
                freq_dict[char] = 1
        return freq_dict

    def __Build_Encoded_Text(self, text: str) -> str:
        encoded_text = ""
        for char in text:
            encoded_text += self.code_dict[char]
        return encoded_text

    def __Build_Decoded_Text(self, text: str) -> str:
        curr = ""
        decoded_text = ""
        reverse_code_dict = {}

        for key, val in self.code_dict.items():
            reverse_code_dict[val] = key
        for char in text:
            curr += char
            if curr in reverse_code_dict:
                decoded_text += reverse_code_dict[curr]
                curr = ""
        return decoded_text

    def __Build_Padded_text(self, text: str) -> str:
        n = 8 - len(text) % 8
        for i in range(n):
            text += "0"
        padding_info = "{0:08b}".format(n)
        padded_text = padding_info + text
        return padded_text

    def __Remove_padded_text(self, text: str) -> str:
        padding_info = int(text[:8], 2)
        text = text[8:]
        text = text[: -1 * padding_info]
        return text

    def __Build_Byte_array(self, text: str) -> List[int]:
        n = len(text)
        array = []
        for i in range(0, n, 8):
            array.append(int(text[i : i + 8], 2))
        return array

    def compression(self) -> str:
        print("COMPRESSION IN PROGRESS")
        filename, self.extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, "r+") as file, open(output_path, "wb") as output:
            text = file.read()
            text = text.rstrip()

            frequency_dict = self.__Build_Frequency_From_Text(text)
            pq = minHeap()
            for key, val in frequency_dict.items():
                node = Node(key, val)
                pq.push(node)
            bt = BinaryTree(pq)
            bt.build_binary_tree()
            self.code_dict = bt.extract_code()
            encoded_text = self.__Build_Encoded_Text(text)
            padded_encoded_text = self.__Build_Padded_text(encoded_text)
            bytes_array = self.__Build_Byte_array(padded_encoded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
        print("COMPRESSED SUCCESSFULLY")
        return output_path

    def decompression(self, input_path: str) -> str:
        print("DECOMPRESSION IN PROGRESS")
        filename, extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + self.extension
        with open(input_path, "rb") as file, open(output_path, "w") as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bit_string += bits
                byte = file.read(1)
            bit_string = self.__Remove_padded_text(bit_string)
            actual_text = self.__Build_Decoded_Text(bit_string)
            output.write(actual_text)
        print("DECOMPRESSED SUCCESSFULLY")
        return output_path


path = input("ENTER THE FILE PATH: ")
h = HuffmanCode(path)

compressed_path = h.compression()
h.decompression(compressed_path)
