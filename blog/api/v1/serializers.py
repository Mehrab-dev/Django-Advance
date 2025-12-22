from rest_framework import serializers
from blog.models import Post , Category


# class PostSerializers(serializers.Serializer) :
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ['id','name']

class PostSerializers(serializers.ModelSerializer) :
    # content = serializers.ReadOnlyField()
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())

    class Meta :
        model = Post
        fields = ['id','title','content','snippet','status','category','author','relative_url','absolute_url','created_date','published_date']
        read_only_fields = ['content']
    
    def get_absolute_url(self,object) :
        request = self.context.get('request')
        return request.build_absolute_uri(object.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep =  super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk') :
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('absolute_url',None)
        else :
            rep.pop('content',None)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

