import secrets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

from .models import OTPCode
from django.utils import timezone
from datetime import timedelta


def generate_otp_code(l=4) -> str:
    return "".join(secrets.choice("0123456789") for _ in range(l))


class SendOTPView(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")

        if not email:
            return Response({"error": "No email provided!"},
                            status=status.HTTP_400_BAD_REQUEST)

        "@@@box.ru"
        "xm@xm.x"
        # normalize

        otp_code = generate_otp_code()

        OTPCode.objects.create(
            email=email,
            otp_code=otp_code,
        )

        try:
            send_mail(
                "Azza Verification Code",
                f"Your OTP code is: {otp_code}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
        except Exception as err:
            print("Error while sending mail...")

        return Response({"message": "Send OTP code!"},
                        status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    def post(self, request):
        data = request.data
        otp_code = data.get("otp_code")

        stored_otp_code = OTPCode.objects.filter(
            email=data.get("email"),
            expires_at__gte=timezone.now()
        ).last()

        if not stored_otp_code:
            return Response({"error": "Invalid or expired OTP code!"},
                            status=status.HTTP_400_BAD_REQUEST)

        if otp_code != stored_otp_code.otp_code:
            return Response({"error": "OTP code is invalid!"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Logged in successfully!"},
                        status=status.HTTP_200_OK)
