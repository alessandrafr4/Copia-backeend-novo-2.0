from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
# from uploader.models import Image
# from uploader.serializers import ImageSerializer

from fabidecor.models import Produto

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


# class ProdutoSerializer(serializers.ModelSerializer):
#     cover_attachment_key = serializers.SlugRelatedField(
#         source="cover",
#         queryset=Image.objects.all(),       # pylint: disable=no-member
#         slug_field="attachment_key",
#         required=False,
#         write_only=True,
#     )
#     cover = ImageSerializer(required=False, read_only=True)

#     class Meta:
#         model = Produto


# class ProdutoDetailSerializer(serializers.ModelSerializer):
#     cover = ImageSerializer(required=False)
#     tema = serializers.CharField(source="tema.name")

#     class Meta:
#         model = Produto
