from cgi import test
#from tkinter import CASCADE
from django.db import models
from django.forms import DateField, DateTimeField
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    wallet=models.CharField(max_length=255,unique=True ,null=False,blank=False)
    def __str__(self):
        return self.wallet

class Domain(models.Model):
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="Domain")
    profile = models.CharField(max_length= 255)
    domain = models.CharField(max_length= 255, unique=True)
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain
        #return "Nombre: %s, ID_dominio:%s"%(self.domain,self.id)

class DomainCredentials(models.Model):
    domain=models.OneToOneField(Domain,null=False,on_delete=models.CASCADE, primary_key=True)
    seedPhrase = models.CharField(max_length= 255)
    secretKey = models.CharField(max_length= 255)
    publicKey = models.CharField(max_length= 255)

    def __str__(self):
        return self.domain.domain 
        #return "Dominio: %s, ID_credential:%s"%(self.domain.domain,self.domain.id)

class PurchasedDomain(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="Domain")
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.wallet

# class ProfileLibrary(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="library")
#     domains = models.ManyToManyField(Domain, blank=True)
#     def __str__(self):
#         return self.profile.wallet

# def post_save_profile_receiver(sender, instance, created, **kwargs):
#     if created:
#         library=ProfileLibrary.objects.create(profile=instance)

#         purchased_domains = PurchasedDomain.objects.filter(profile=instance)

#         for purchased_domain in purchased_domains:
#             library.domains.add(purchased_domain.domain)

# post_save.connect(post_save_profile_receiver, sender=Profile)