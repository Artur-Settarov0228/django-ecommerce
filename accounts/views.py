import json
from django.views import View

from django.http import HttpRequest , JsonResponse
from . models import User, Profile


class AccountView(View):

    def post(self, request: HttpRequest) -> JsonResponse:

        data = json.loads(request.body.decode())

        try:
            User.objects.get(username = data['username'])

            return JsonResponse({'massage': 'Username yaratib bo`lgan'}, status=400)
        except User.DoesNotExist:
            user = User(
                username = data['username'],
                password = data['password'],
                email = data.get('email'),
                phone = data.get('phone')

            )
            user.save()

            profile = Profile(user = user)
            profile.save()

            return JsonResponse(data={'massage': 'user yaratildi'}, status = 201)


        
       
    