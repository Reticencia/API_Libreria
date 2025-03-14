from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_published_date(self, value):
        if value > date.today():
            raise ValueError('Error')
        return value
        
