
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models  import Post, Comment, Subly
from users.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch',
        allow_null=True
    )
    image = serializers.ImageField(required=False, allow_null=True)

    author_id = serializers.SerializerMethodField( read_only = True)
    def get_author_id(self, obj):
        if obj.author:
           return obj.author.id
        else:
            return None

    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'author_id', 'like', 'image')
        read_only_fields =  ['like', 'author', 'author_id' , 'image']

    


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch',
        allow_null=True
     )

    author_id = serializers.SerializerMethodField( read_only = True)
    def get_author_id(self, obj):
        if obj.author:
           return obj.author.id
        else:
            return None



    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'author', 'parent', 'author_id', 'like' )
        read_only_fields =  ['like', ]


class SublySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch'
     )
    class Meta:
        model = Subly
        fields = ('id', 'body', 'comment', 'author',)

        