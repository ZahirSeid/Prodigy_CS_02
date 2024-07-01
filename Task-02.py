from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # swapping red and blue channels
            encrypted_pixel = (pixel[2], pixel[1], pixel[0])
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    width, height = encrypted_image.size
    decrypted_image = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            # swapping red and blue channels back
            decrypted_pixel = (encrypted_pixel[2], encrypted_pixel[1], encrypted_pixel[0])
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").lower()
    if choice == "encrypt":
        image_path = input("Enter the path to the image to encrypt: ")
        key = input("Enter encryption key: ")
        encrypt_image(image_path, key)
    elif choice == "decrypt":
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        key = input("Enter decryption key: ")
        decrypt_image(encrypted_image_path, key)
    else:
        print("Invalid choice. Please enter either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
