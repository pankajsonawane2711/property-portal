from django.http import HttpResponse
def robots_txt(request):
    content = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: /sitemap.xml",
    ]
    return HttpResponse("\n".join(content), content_type="text/plain")
