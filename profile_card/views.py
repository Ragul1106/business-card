from django.http import HttpResponse
from django.shortcuts import render

def profile_view(request):
    user_data = {
        "name": "Ragul R",
        "title": "Full Stack Developer & Designer",
        "email": "ragul@example.com",
        "phone": "+91 98765 43210",
        "bio": "I build modern web apps, design creative UI, and love coding in Python & React.",
        "linkedin": "https://www.linkedin.com/in/ragul-r-9928aa211/",
        "github": "https://github.com/Ragul116",
    }
    return render(request, "profile.html", {"user": user_data})


def download_vcard(request):
    vcard_content = """BEGIN:VCARD
VERSION:3.0
FN:Ragul R
TITLE:Full Stack Developer & Designer
EMAIL:ragul@example.com
TEL:+91 98765 43210
URL:https://www.linkedin.com/in/ragul-r-9928aa211/
URL:https://github.com/Ragul116
END:VCARD
"""
    response = HttpResponse(vcard_content, content_type="text/vcard")
    response["Content-Disposition"] = 'attachment; filename="ragul.vcf"'
    return response
