import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.paginator import Paginator
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Student
from .serializers import StudentSerializer, StudentDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from apps.administrator.permissions import IsSubAdminPermission
import qrcode
import smtplib, ssl
from email.mime.image import MIMEImage
from django.core.files import File
from apps.classquantity.models import StudentClassQuantity

def generate_qrcode(stud_id):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(f'http://127.0.0.1:8000/api/student/{stud_id}/')
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'media/qrcode/qrcode_{stud_id}.png')
    file_obj = File(open(f'media/qrcode/qrcode_{stud_id}.png', mode='rb'), name=f'media/qrcode/qrcode_{stud_id}.png')
    return file_obj


def SendMail(ImgFileName, from_email, to_email):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'QR Code'
    msg['From'] = from_email
    msg['To'] = to_email

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('islambaigashkaev@gmail.com', 'lfcxsrckmjmcwdje')
    s.sendmail('islambaigashkaev@gmail.com', to_email, msg.as_string())
    s.quit()


class StudentListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = Student.objects.filter(active=True)
        serializer = StudentSerializer(snippets, many=True)
        data = {
            'count': snippets.count(),
            'data': serializer.data
        }
        return Response(data)


class StudentArchiveListAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = Student.objects.filter(active=False)
        serializer = StudentSerializer(snippets, many=True)
        data = {
            'count': snippets.count(),
            'data': serializer.data
        }
        return Response(data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentCreateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer valid')
            student = Student.objects.create(
                # course=request.data['course'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                second_name=request.data['second_name'],
                phone=request.data['phone'],
                first_month_paid=request.data['first_month_paid'],
                second_month_paid=request.data['second_month_paid'],
                third_month_paid=request.data['third_month_paid'],
                fourth_month_paid=request.data['fourth_month_paid'],
                description=request.data['description'],
                qr_code=generate_qrcode(request.data['email'])
            )
            student.save()
            student.course.set(request.data['course'])
            student.save()
            stud_class_quan = StudentClassQuantity.objects.create(
                student=student,
                course_id=request.data['course'][0],
                quantity_of_classes=request.data['quantity_of_classes']
            )
            stud_class_quan.save()
            print('student created')
            print('qrcode', student.qr_code)
            SendMail(student.qr_code.path, 'islambaigashkaev@gmail.com', student.email)
            serializer_output = StudentDetailSerializer(student)
            return Response(serializer_output.data, status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet2 = StudentClassQuantity.objects.filter(student_id=id)
        courseid_list = [obj.course.id for obj in snippet2]
        print(courseid_list)
        serializer = StudentSerializer(snippet, data=request.data)
        serializer2 = StudentClassQuantity()
        print(request.data['course'])
        studclassquan = StudentClassQuantity.course
        if serializer.is_valid():
            serializer.save()
            for i in request.data['course']:
                if i not in courseid_list:
                    StudentClassQuantity.objects.create(
                        student_id=id,
                        course_id=i,
                        quantity_of_classes=request.data['quantity_of_classes']
                    )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class AddStudentClassQuantity(APIView):
#     permission_classes = [IsSubAdminPermission]
#     # authentication_classes = [SessionAuthentication]
#     parser_classes = [JSONParser]
#
#     post

class StudentUpdateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDeleteAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentSendMailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





