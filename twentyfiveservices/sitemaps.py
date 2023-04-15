from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class CustomSitemaps(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ["HomeView","AllServices","ContactUsView","TermsCondtitions","UsersSitemap","PrivacyPolicy","CVMaker",
                "TextToSpeech","WordsCounter","OnlineSignature","InternetSpeedChecker","TriangleAreaFinder",
                "AllUnitsConverter","DecimalToBinary","AsciToBinary","IpLocator","AgeCalculator","ScientificCalculator",
                "ColorPicker","Drawing","TextToPdf","RandomQuotesGen","RandomPasswordGen","CaseConverter",
                "CarColorChoose","QRcodeGen","YearsCalender","NamesGenerator","FutureIndicator","SuitableJob","PeroidTable"]

    # builtin view for reversing
    def location(self, item):
        return reverse(item)


