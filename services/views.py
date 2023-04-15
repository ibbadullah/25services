from django.shortcuts import render, redirect
from django.views import View
import calendar
from django.contrib import messages
from .names import *
import random

# function/view for home
def Home(request):
    return render(request,'index.html')

# Contact us view
def ContactUs(request):
    return render(request,'ContactUs.html')

# Terms and conditions view
def TermsConditionsView(request):
    return render(request,'TermsConditions.html')

# privacy policy view
def PrivacyPolicyView(request):
    return render(request,'Privacy.html')


# privacy policy view
def AboutUS(request):
    return render(request,'AboutUs.html')

# all services view
def AllServices(request):
    return render(request,'services/services.html')


'''
Services views
'''
# 1 CV Generator
class CvGenerator(View):
    def get(self,request):
        return render(request,'services/1_cv_maker/1_cv.html')

    def post(self,request):
        if request.method == "POST":
            fullName = request.POST['full_name']
            address = request.POST['address']
            email = request.POST['email']
            bio = request.POST['bio']
            # Experience 1
            job_title1 = request.POST['job_title1']
            job_company1 = request.POST['job_company1']
            job_des1 = request.POST['job_des1']
            job_start_date1 = request.POST['job_start_date1']
            job_end_date1 = request.POST['job_end_date1']

            # Experience 2
            job_title2 = request.POST['job_title2']
            job_company2 = request.POST['job_company2']
            job_des2 = request.POST['job_des2']
            job_start_date2 = request.POST['job_start_date2']
            job_end_date2 = request.POST['job_end_date2']

            # Experience 3
            job_title3 = request.POST['job_title3']
            job_company3 = request.POST['job_company3']
            job_des3 = request.POST['job_des3']
            job_start_date3 = request.POST['job_start_date3']
            job_end_date3 = request.POST['job_end_date3']

            eduaction = request.POST['eduaction']
            skills = request.POST['skills']
            hobbies = request.POST['hobbies']
            certificates_awards = request.POST['certificates_awards']

            # Now strong all the information in one dic
            Data = {
                "FullName": fullName,
                "Address": address,
                "Email": email,
                "Bio": bio,
                "Education": eduaction,
                "Skills": skills,
                "Hobbies": hobbies,
                "CertificatesAwards": certificates_awards,

                # Experiences
                #Exp 1
                "JobTitle1": job_title1,
                "JobCompany1": job_company1,
                "JobDes1": job_des1,
                "JobStartDate1": job_start_date1,
                "JobEndDate1": job_end_date1,

                # Exp 2
                "JobTitle2": job_title2,
                "JobCompany2": job_company2,
                "JobDes2": job_des2,
                "JobStartDate2": job_start_date2,
                "JobEndDate2": job_end_date2,

                # Exp 3
                "JobTitle3": job_title3,
                "JobCompany3": job_company3,
                "JobDes3": job_des3,
                "JobStartDate3": job_start_date3,
                "JobEndDate3": job_end_date3,

            }

            return render(request,'services/1_cv_maker/2_cv_maker.html',Data)





# 2 Text to speech view
def TextToSpeech(request):
    return render(request,'services/2_text_to_speech/2_text_to_speech.html')

# 3 Interned Speed checker
def InternetSpeedChecker(request):
    ip = GetIp(request)
    return render(request,'services/3_internet_speed_checker/3_internet_speed_checker.html',{"Ip":ip})

# 4 Words counter
def WordsCounter(request):
    return render(request,'services/4_words_counter/4_words_counter.html')

# 5 Online signature
def OnlineSignature(request):
    return render(request,'services/5_online_signature/5_online_signature.html')

# 6 Triangle area finder
def TriangleAreaFinder(request):
    return render(request,'services/6_triangle_area_finder/6_triangle_area_finder.html')

# 7 All Units converter
def AllUnitsConverter(request):
    return render(request,'services/7_units_converter/7_units_converter.html')

# 8 Decimal to binary
def DecimalToBinary(request):
    return render(request,'services/8_decimal_to_binary/8_decimal_to_binary.html')

# 9 Assci to binary
def AsciToBinary(request):
    return render(request,'services/9_ascci_to_binary/9_ascii_to_binary.html')

# 10 Assci to binary
def MyIpLocator(request):
    ip = GetIp(request)
    return render(request,'services/10_my_ip_locator/10_my_ip_locator.html',{"Ip":ip})

# 11 Age calculator
def AgeCalculator(request):
    return render(request,'services/11_age_calculator/11_age_calculator.html')

# 12 Scientific calculator
def ScientificCalculator(request):
    return render(request,'services/12_scientific_calculator/12_scientific_calculator.html')

# 13 Color picker
def ColorPicker(request):
    return render(request,'services/13_color_picker/13_color_picker.html')

# 14 Color picker
def Drawing(request):
    return render(request,'services/14_drawing/14_Drawing.html')

# 15 Color picker
def TextToPdf(request):
    return render(request,'services/15_text_to_pdf/15_text_to_pdf.html')


# 16 Random quotes genrator
def RandomQuotesGen(request):
    return render(request,'services/16_random_quotes_generator/16_random_quotes_generator.html')

# 17 Random password genrator
def RandomPasswordGen(request):
    return render(request,'services/17_password_generator/17_password_generator.html')

# 18 Random password genrator
def CaseConverter(request):
    return render(request,'services/18_case_converter/18_case_converter.html')

# 19 Random password genrator
def CarColorChoose(request):
    return render(request,'services/19_car_painter/19_car_painter.html')

# 20 QR code generator
def QRcodeGen(request):
    return render(request,'services/20_qr_code_generator/20_qr_code_generator.html')



# 22 future indicator
class FutureIndicator(View):
    def get(self, request):
        return render(request, "services/22_future_indicator/future_indicator.html")


def IndicateFuture(request):
    try:
        if request.method == "GET":
            nameupper = request.GET['name'].capitalize()
            name = request.GET['name'].lower()
            uName = request.GET['name']
            gender = request.GET['gender']
            return render(request, 'services/22_future_indicator/futureIndicatorSearchPage.html',
                          {"Name": name[0], "Gender": gender, "NameU": nameupper,"UrlName":uName.replace(' ','+')})
    except:
        return redirect('HomeView')


# 23 Suitable job indicator
class SuitableJob(View):
    def get(self, request):
        return render(request, "services/23_suitable_job_for_you/suitabeJob.html")

# Indicate suitable job
def IndicateSuitableJob(request):
    try:
        if request.method == "GET":
            nameupper = request.GET['name'].capitalize()
            name = request.GET['name'].lower()
            uName = request.GET['name']
            return render(request, 'services/23_suitable_job_for_you/suitableJobSearch.html',
                          {"Name": name[0], "NameU": nameupper,"UrlName":uName.replace(' ','+')})
        else:
            return redirect('HomeView')
    except:
        return redirect('HomeView')

# 24 peroid
class YearsCalender(View):
    def get(self,request):
        return render(request,"services/24_every_year_calender/years-calender.html")



# 25 peroid
def PeroidTable(request):
    return render(request,'services/25_periodic_table/25_periodic_table.html')




# 21 names generator
class NamesGenerator(View):
    def get(self, request):
        return render(request, "services/21_names_generator/names-generator.html",{"display":"none"})

    def post(self, request):
        gender = request.POST['gender']
        category = request.POST['category']
        range = request.POST['range']

        if gender == "Male" and category == "Muslim" and range == "1-50":
            data = male_muslim[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Male" and category == "Muslim" and range == "50+":
            data = male_muslim
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

        elif gender == "Male" and category == "English" and range == "1-50":
            data = male_english[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Male" and category == "English" and range == "50+":
            data = male_english
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

        elif gender == "Male" and category == "Hindi" and range == "1-50":
            data = male_hindi[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Male" and category == "Hindi" and range == "50+":
            data = male_hindi
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

        elif gender == "Female" and category == "Hindi" and range == "1-50":
            data = female_hindi[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Female" and category == "Hindi" and range == "50+":
            data = female_hindi
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

        elif gender == "Female" and category == "Muslim" and range == "1-50":
            data = female_muslim[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Female" and category == "Muslim" and range == "50+":
            data = female_muslim
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

        elif gender == "Female" and category == "English" and range == "1-50":
            data = female_english[0:50]
            random.shuffle(data)
            return render(request,'services/21_names_generator/names-generator.html',{"Data":data,"display":"inline-block"})

        elif gender == "Female" and category == "English" and range == "50+":
            data = female_english
            random.shuffle(data)
            return render(request, 'services/21_names_generator/names-generator.html',
                          {"Data": data, "display": "inline-block"})

















# Sitemap for user
def UsersSitemap(request):
    return render(request,'user-sitemap.html')





# Returning Ip ADDRESS
def GetIp(request):
    x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forward:
        ip = x_forward.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

