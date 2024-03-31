
def get_full_image_url(request,image_url):
    if image_url:
        return request.build_absolute_uri(image_url)
    return None