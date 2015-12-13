def representative_image_upload_to(instance, filename):
    return "tumblr/{blog_slug}/{post_id}/{filename}.{extension}".format(
        blog_slug=instance.blog.slug,
        post_id=instance.post_id,
        filename='representative',
        extension=filename.split('.')[-1],
    )


def screenshot_image_upload_to(instance, filename):
    return "tumblr/{blog_slug}/{post_id}/{filename}.{extension}".format(
        blog_slug=instance.blog.slug,
        post_id=instance.post_id,
        filename='screenshot',
        extension=filename.split('.')[-1],
    )
