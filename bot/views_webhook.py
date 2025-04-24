# views_webhook.py
import hmac
import hashlib
import subprocess
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

GITHUB_SECRET = '928751372'.encode('utf-8')  # теперь всё ок
# тот же, что в GitHub Webhook
REPO_PATH = '/home/yourusername/yourproject/'
WSGI_FILE = '/var/www/yourusername_pythonanywhere_com_wsgi.py'

@csrf_exempt
def github_webhook(request):
    if request.method != 'POST':
        return HttpResponse("Only POST requests are accepted", status=405)

    signature = request.headers.get('X-Hub-Signature')
    if signature is None:
        return HttpResponseForbidden("No signature")

    body = request.body
    mac = hmac.new(GITHUB_SECRET, msg=body, digestmod=hashlib.sha1)
    expected = f'sha1={mac.hexdigest()}'
    if not hmac.compare_digest(expected, signature):
        return HttpResponseForbidden("Invalid signature")

    subprocess.run(['git', 'pull'], cwd=REPO_PATH)
    subprocess.run(['touch', WSGI_FILE])

    return HttpResponse("Updated", status=200)

