import secrets

from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def generate_otp_code(length=4) -> str:
    return "".join(secrets.choice("0123456789") for _ in range(length))


class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "No email provided!"},
                            status=status.HTTP_400_BAD_REQUEST)

        # generate OTP
        otp_code = generate_otp_code()

        # store in cache (expire in 5 minutes)
        cache_key = f"otp_{email}"
        cache.set(cache_key, otp_code, timeout=300)  # 300s = 5min
        
        # send via email
        try:
            send_mail(
                subject="Azza Verification Code",
                message=f"Your OTP code is: {otp_code}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as err:
            print("Error sending email:", err)
            return Response({"error": "Error sending email"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "OTP code sent!"},
                        status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp_code = request.data.get("otp_code")

        if not email or not otp_code:
            return Response({"error": "Email and OTP code are required!"},
                            status=status.HTTP_400_BAD_REQUEST)

        cache_key = f"otp_{email}"
        stored_otp = cache.get(cache_key)

        if not stored_otp:
            return Response({"error": "Invalid or expired OTP code!"},
                            status=status.HTTP_400_BAD_REQUEST)

        if otp_code != stored_otp:
            return Response({"error": "OTP code is invalid!"},
                            status=status.HTTP_400_BAD_REQUEST)

        cache.delete(cache_key)

        return Response({"message": "Logged in successfully!"},
                        status=status.HTTP_200_OK)