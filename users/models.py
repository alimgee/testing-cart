from django.db import models
from django.contrib.auth.models import User #importing built in user model to extend
from PIL import Image #importing pillow image 


class Profile(models.Model): # creating model for profile - one to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE) # when user is deleted profile is removed too
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # default location of default profile image

    def __str__(self): # returning profile name
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): #overwriting save method, save method of parent class super()
        super().save()
        # resize image
        img = Image.open(self.image.path)
        # if image size is greater ythan 300 resize
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) # save new image back over the original image path