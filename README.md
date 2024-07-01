```markdown
# Simple Image Encryption Tool

This Python program implements a simple image encryption and decryption tool using pixel manipulation. The tool allows you to encrypt an image by swapping pixel values and then decrypt it back to its original form.

## Features

- Encrypt an image by swapping pixel values.
- Decrypt an encrypted image back to its original form.
- Uses the Python Imaging Library (PIL) for image manipulation.

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library), which can be installed via Pillow.

### Installation

To install Pillow, run the following command:

```sh
pip install pillow
```

## Usage

1. Clone the repository or download the `Task-02.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where `Task-02.py` is located.
4. Run the program using the following command:

    ```sh
    python Task-02.py
    ```

### Program Flow

1. The program will prompt you to choose between encryption and decryption.
2. Enter the path to the image you wish to encrypt or decrypt.
3. Enter an encryption key (for demonstration purposes, the key is not used in this basic version).
4. The program will process the image and save the encrypted or decrypted image as `encrypted_image.png` or `decrypted_image.png`, respectively.

### Example

#### Encrypt an Image

```sh
Do you want to encrypt or decrypt an image? (encrypt/decrypt): encrypt
Enter the path to the image to encrypt: path/to/your/image.png
Enter encryption key: my_secret_key
Image encrypted successfully.
```

#### Decrypt an Image

```sh
Do you want to encrypt or decrypt an image? (encrypt/decrypt): decrypt
Enter the path to the encrypted image: path/to/encrypted_image.png
Enter decryption key: my_secret_key
Image decrypted successfully.
```

## Code Explanation

### `encrypt_image(image_path, key)`

This function takes an image path and a key as input, performs a simple encryption operation (swapping the red and blue channels of each pixel), and saves the encrypted image.

### `decrypt_image(encrypted_image_path, key)`

This function takes the path of the encrypted image and a key as input, performs the decryption operation (swapping the red and blue channels back), and saves the decrypted image.

### `main()`

The main function prompts the user for input and calls the appropriate functions to encrypt or decrypt the image.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Ethical Considerations

This tool is intended for educational purposes only. Ensure you have permission to use this tool on the images and systems you are working with.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve this project.
