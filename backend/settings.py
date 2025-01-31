import os

# 添加安全设置
ALLOWED_HOSTS = ['yourdomain.com']

# 添加文件上传设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 