from datetime import datetime


class BlogPost:
    def __init__(self, title, description, publish_date):
        self.title = title
        self.description = description
        self.publish_date = publish_date


def print_blog_post(item):
    print('Title: ' + item.title)
    print('Description: ' + item.description)
    print('Published date: ' + item.publish_date)


title = 'Clean Code Is Great!'
description = 'Actually, writing Clean Code can be pretty fun. You\'ll see!'
now = datetime.now()
forrmated_date = now.strftime('%Y-%m-%d %H:%M')

blog_post = BlogPost(title, description, forrmated_date)

print_blog_post(blog_post)
