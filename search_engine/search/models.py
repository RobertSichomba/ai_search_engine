from django.db import models

class ScrapedData(models.Model):
    url = models.URLField(unique=True)  # URL of the scraped page
    title = models.CharField(max_length=255)  # Title of the page
    content = models.TextField()  # Main content of the page
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title