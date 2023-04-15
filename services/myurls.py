from django.urls import path, include
from .views import *


urlpatterns = [
    path('',Home,name="HomeView"),
    path('contact-us/',ContactUs,name="ContactUsView"),
    path('terms-conditions/',TermsConditionsView,name="TermsCondtitions"),
    path('privacy-policy/',PrivacyPolicyView,name="PrivacyPolicy"),
    path('sitemap/', UsersSitemap, name="UsersSitemap"),
    path('about-us/', AboutUS, name="AboutUS"),
    path('services/', AllServices, name="AllServices"),

    # Services URLS
    path('cv-maker/',CvGenerator.as_view(),name="CVMaker"),
    path('text-to-speech/',TextToSpeech,name="TextToSpeech"),
    path('words-counter/',WordsCounter,name="WordsCounter"),
    path('online-signature/',OnlineSignature,name="OnlineSignature"),
    path('internet-speed-checker/',InternetSpeedChecker,name="InternetSpeedChecker"),
    path('triangle-area-finder/',TriangleAreaFinder,name="TriangleAreaFinder"),
    path('all-units-converter/',AllUnitsConverter,name="AllUnitsConverter"),
    path('decimal-to-binary/',DecimalToBinary,name="DecimalToBinary"),
    path('ascii-to-binary/',AsciToBinary,name="AsciToBinary"),
    path('ip-locator/',MyIpLocator,name="IpLocator"),
    path('age-calculator/',AgeCalculator,name="AgeCalculator"),
    path('scientific-calculator/', ScientificCalculator, name="ScientificCalculator"),
    path('color-picker/', ColorPicker, name="ColorPicker"),
    path('online-free-drawing/', Drawing, name="Drawing"),
    path('text-to-pdf/', TextToPdf, name="TextToPdf"),
    path('quotes-generator/', RandomQuotesGen, name="RandomQuotesGen"),
    path('password-generator/', RandomPasswordGen, name="RandomPasswordGen"),
    path('case-converter/', CaseConverter, name="CaseConverter"),
    path('car-color-choose/', CarColorChoose, name="CarColorChoose"),
    path('qr-code-generator/', QRcodeGen, name="QRcodeGen"),
    path('year-calender/',YearsCalender.as_view(),name="YearsCalender"),
    path('names-generator/',NamesGenerator.as_view(),name="NamesGenerator"),
    path('future-indicator/', FutureIndicator.as_view(), name="FutureIndicator"),
    path('indicate-future', IndicateFuture, name="IndicateFuture"),
    path('indicate-job', IndicateSuitableJob, name="IndicateSuitableJob"),
    path('suitable-job/',SuitableJob.as_view(),name="SuitableJob"),

    path('periodic-table-elements/', PeroidTable, name="PeroidTable"),
]
