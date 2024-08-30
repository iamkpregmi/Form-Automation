from django.shortcuts import render
from core.models import *
import pandas as pd
from django.http import HttpResponse
from openpyxl import Workbook
#for the pdf file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def home(request):
    student_obj = Student.objects.all()
    context = {
        'student_obj': student_obj
    }
    return render(request,'index.html',context)

def add_student(request):  
    return render(request,"add_student.html")


def download_students_form(request):
    # Create a new workbook and select the active worksheet
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Students'

    # Define the header row based on the model's fields
    headers = ['student_id', 'student_name', 'city', 'fee']
    sheet.append(headers)

    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students_headers.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response


def download_students_excel(request):
    # Query all students
    students = Student.objects.all()

    # Create a DataFrame
    df = pd.DataFrame(list(students.values('student_id', 'student_name', 'city', 'fee')))

    # Create an HTTP response with Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    # Write the DataFrame to an Excel file
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Students')

    return response


def download_students_pdf(request):
    # Create an HTTP response with PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=students.pdf'

    # Create a PDF object using ReportLab
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Set up the title and other initial configurations
    p.setFont("Helvetica", 12)
    p.drawString(72, height - 72, "Student List")

    # Define the column headers
    headers = ['Student ID', 'Student Name', 'City', 'Fee']
    x_positions = [72, 180, 300, 400]
    
    for x, header in zip(x_positions, headers):
        p.drawString(x, height - 100, header)
    
    # Query all students
    students = Student.objects.all()
    y_position = height - 120  # Start below the header

    for student in students:
        p.drawString(x_positions[0], y_position, student.student_id)
        p.drawString(x_positions[1], y_position, student.student_name)
        p.drawString(x_positions[2], y_position, student.city)
        p.drawString(x_positions[3], y_position, str(student.fee))
        y_position -= 20  # Move to the next line

    p.showPage()
    p.save()

    return response

