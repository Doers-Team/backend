from django.core.exceptions import ValidationError

def validate_video_file(value):
    if not value:
        return

    uploaded_file = getattr(value, 'file', None)

    content_type = getattr(uploaded_file, 'content_type', None)

    if content_type:
        if not content_type.startswith('video/'):
            raise ValidationError("Uploaded file is not a valid video")
    else:
        import os
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in ['.mp4', '.mov', '.avi', '.webm']:
            raise ValidationError("Unsupported video format")
