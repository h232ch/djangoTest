

from rest_framework import serializers
from demo.models import Book, Album, Track
from demo.models import Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published']


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


# class AlbumSerializer(serializers.ModelSerializer):
    # String field relationship
    # tracks = serializers.StringRelatedField(many=True)

    # Primary key relationship
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # HiperLink relationship
    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail'
    # )

    # slug
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )

    # class Meta:
    #     model = Album
    #     fields = ['album_name', 'artist', 'tracks']


# hyperlinked

# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ['order', 'title', 'duration']
#
#
# class AlbumSerializer(serializers.HyperlinkedModelSerializer):
#     track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')
#
#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'track_listing']


# nested relation with hyperlinked model serializer
class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration', 'url']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']


# writable nested serializers
# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ['order', 'title', 'duration']
#
#
# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True)
#
#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']
#
#     def create(self, validated_data):
#         tracks_data = validated_data.pop('tracks')
#         album = Album.objects.create(**validated_data)
#         for track_data in tracks_data:
#             Track.objects.create(album=album, **track_data)
#         return album