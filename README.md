# Huffman-Compressor-Decompressor
# Huffman Coding Compression and Decompression

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Overview

This project implements Huffman Coding for text compression and decompression. Huffman Coding is a Greedy lossless data compression algorithm that uses variable-length codes to represent characters based on their frequencies. This project includes classes for managing binary trees, min-heaps, and custom queues, providing a comprehensive example of how Huffman Coding can be applied.

## Requirements 

- Binary Tree 
- Priority_queue
- Heap
- File handling
- Huffman Coding Algorithm

## Project Structure

```
huffman/
|-- init.py
|-- binary_tree.py
|-- custom_queue.py
|-- heap.py
|-- huffman_code.py
|-- README.md
```


- `binary_tree.py`: Contains the `BinaryTree` class for managing binary tree operations.
- `custom_queue.py`: Contains the `Queue` and `QueueNode` classes for queue operations.
- `heap.py`: Contains the `minHeap` and `Node` classes for heap operations.
- `huffman_code.py`: Contains the `HuffmanCode` class for compression and decompression.

## Installation

To use this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/rohanmittal1163/Huffman-Compressor-Decompressor.git
cd huffman-coding
```

## Usage
### Compression
To compress a file, use the HuffmanCode class:

```python
from huffman.huffman_code import HuffmanCode

path = "path/to/your/textfile.txt"
huffman = HuffmanCode(path)
compressed_path = huffman.compression()
print(f"File compressed to: {compressed_path}")
```

### Decompression
To decompress a file, use the HuffmanCode class:

```python
decompressed_path = huffman.decompression(compressed_path)
print(f"File decompressed to: {decompressed_path}")
```

## Example
Here's a complete example of how to compress and decompress a text file:
```python
from huffman.huffman_code import HuffmanCode

# Initialize with the path to the file to compress
path = "path/to/your/textfile.txt"
huffman = HuffmanCode(path)

# Compress the file
compressed_path = huffman.compression()
print(f"File compressed to: {compressed_path}")

# Decompress the file
decompressed_path = huffman.decompression(compressed_path)
print(f"File decompressed to: {decompressed_path}")
```
## Algorithm
1. Calculate the frequency of each character in the input text.
2. Initialize a priority queue (min-heap) with nodes containing characters and their frequencies.
3. Construct a binary tree using the priority queue:
     - Extract two nodes with the lowest frequencies from the priority queue.
     - Create a new node with these two nodes as children, and the sum of their frequencies as its frequency.
     - Insert the new node back into the priority queue.
     - Repeat until only one node remains in the priority queue, forming the Huffman tree.
4. Traverse the Huffman tree to generate binary codes for each character:
     - Start at the root of the tree.
     - Traverse left for '0' and right for '1'.
     - Record the binary code for each character encountered along the way.
5. Replace each character in the input text with its corresponding Huffman code.
6. Concatenate the binary codes to form the compressed text.
7. Add padding to the compressed text to ensure the length is a multiple of 8 (if needed).
8. Record the number of padding bits added.
9. Output the compressed text along with any padding information.
10. Read the compressed text and padding information.
11. Remove the padding bits to restore the original length.
12. Traverse the Huffman tree using the binary codes to decode the compressed text back to its original form.


## Features

- **Compression**: Compresses text files using Huffman Coding.
- **Decompression**: Decompresses files back to their original text.
- **Binary Tree Management**: Constructs and traverses binary trees.
- **Min-Heap Implementation**: Efficient priority queue operations.
- **Custom Queue**: Supports queue operations for Huffman tree construction.
  
##  Contribute
This project is open source and we are happy to receive contributions. If you would like to contribute, please follow these steps:

1. Make a fork of the repository.
2. Create a branch for your feature or bugfix (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added my new feature'`)
4. Push your branch (`git push origin my-new-feature`)
5. Create a pull request.

<p align="center">
  <img src="https://user-images.githubusercontent.com/104341274/210186277-0d434bb0-80c0-43a9-b6b0-2e42e18c31a9.png" width="400" />
</p>
