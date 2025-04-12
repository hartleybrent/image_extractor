#!/usr/bin/env python3

import os
import shutil


IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')


def extract_images(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                source_file = os.path.join(root, file)
                
                destination_file = os.path.join(target_dir, file)

                if os.path.exists(destination_file):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(destination_file):
                        destination_file = os.path.join(target_dir, f"{base}_{counter}{extension}")
                        counter += 1

                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")

def main():
    source_dir = input("Enter the source directory path: ").strip()
    target_dir = input("Enter the target directory path: ").strip()

    if not os.path.isdir(source_dir):
        print(f"Error: The source directory {source_dir} does not exist.")
        return
    if not os.path.isdir(target_dir):
        print(f"Error: The target directory {target_dir} does not exist.")
        return

    extract_images(source_dir, target_dir)
    print(f"Image extraction completed. All images are copied to: {target_dir}")

if __name__ == "__main__":
    main()
