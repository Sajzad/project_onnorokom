from rest_framework import serializers

from base.models import *

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('id','first_name', 'last_name', 'username')

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = '__all__'

# class SubMaterialSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = SubMaterial
# 		fields = '__all__'
		
# class MaterialSerializer(serializers.ModelSerializer):
# 	sub_materials = SubMaterialSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Material
# 		fields = '__all__'

# class GetMaterialSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Material
# 		fields = '__all__'

# class MaterialImageSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = MaterialImage
# 		fields = '__all__'
# 		depth = 1

# class SubMatSerializer(serializers.ModelSerializer):
# 	images = MaterialImageSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = SubMaterial
# 		fields = '__all__'

# class ProjectSubMatSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ProjectSubMaterial
# 		fields = '__all__'
# 		depth = 1

# class ProjectMatSerializer(serializers.ModelSerializer):
# 	sub_materials = ProjectSubMatSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = ProjectMaterial
# 		fields = ('id', 'user', 'project', 'material', 'sub_materials')
# 		depth = 1

# class ProjectSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Project
# 		fields = ('id', 'user', 'timestamp', 'project_name',)
# 		depth = 1

# class ProjectEditSerializer(serializers.ModelSerializer):
# 	materials = ProjectMatSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Project
# 		fields = ('id', 'user', 'project_name', 'materials')
