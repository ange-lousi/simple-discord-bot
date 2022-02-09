import discord
from discord.ext import commands
import os, shutil
from google_images_download import google_images_download
import random

class image_cog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot
        self.download_folder = 'downloads'

        self.keywords = "kenpachi"

        self.response = google_images_download.googleimagesdownload()
        self.arguments = {
            "keywords": self.keywords, 
            "limit":10,
            "size":"medium",
            "no_directory": True
            }

        self.image_names = []
        #get the latest in the folder
        self.update_images()

    def update_images(self):
        self.image_names = []
        #store all the names to the files
        for filename in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))

    def clear_folder(self):
        for filename in os.listdir(self.download_folder): #go into downloads folder
            file_path = os.path.join(self.download_folder, filename) #extract path to each individual item
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path): #its a file
                    os.unlink(file_path) #then os.unlink will remove file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path) #if directory will remove folder and all contents of it
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    
    @commands.command(name="get", help="Displays random image from the downloads after searching")
    async def get(self, ctx):
        imgSize = len(self.image_names) -1
        randomImage = random.randint(0, imgSize)
        imgPath = self.image_names[randomImage]      
        await ctx.send(file=discord.File(imgPath))

    @commands.command(name="search", help="searches for an image on google")
    async def search(self, ctx, *args):
        self.clear_folder()

        #fill the folder with new images
        self.arguments['keywords'] = " ".join(args)
        self.response.download(self.arguments)

        self.update_images()





