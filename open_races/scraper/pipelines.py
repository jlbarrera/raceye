import logging
import datetime
import locale
from time import strptime
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

locale.setlocale(locale.LC_ALL, "")


class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:  # Necessary since DDS v.0.9+
            try:
                item['races_website'] = spider.ref_object

                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt
                item['date'] = self.process_date(item['date'], spider)
                item['city'] = self.process_city(item['city'], spider)
                item['province'] = self.process_province(item['province'], spider)
                item.save()
                spider.action_successful = True
                spider.log("Item saved.", logging.INFO)

            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")

        return item

    def process_date(self, date, spider):
        if spider.ref_object.name == "Ges&con-chip":
            try:
                date_scraped = date.split()
                day = int(date_scraped[1])
                month = int(strptime(date_scraped[3], '%B').tm_mon)
                year = int(date_scraped[5])
                date = datetime.date(year, month, day)
            except:
                pass

        return date

    def process_city(self, place, spider):
        if spider.ref_object.name == "Ges&con-chip":
            try:
                place_scraped = place.split("en")
                place = place_scraped[1].split("(")[0]
            except:
                pass

        return place

    def process_province(self, place, spider):
        if spider.ref_object.name == "Ges&con-chip":
            try:
                place_scraped = place.split("en")
                place = place_scraped[1].split("(")[1].replace(")", "")
            except:
                pass

        return place

