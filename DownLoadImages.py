
'''
Get all the images from a website

'''

from image_scraper import scrape_images
import os
from PIL import Image


def downloadImages(url):
    scrape_images(url, download_path='./images/')


def displayImages():
    for file in os.listdir('./images'):
        im = Image.open(file)
        im.show()



if __name__ == "__main__":
    url = input("Enter the Url of the web page from Where u wanna get images : ")
    downloadImages(url)
    displayImages()
