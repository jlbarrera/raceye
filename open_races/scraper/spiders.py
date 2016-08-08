from dynamic_scraper.spiders.django_spider import DjangoSpider
from open_races.models import RacesWebsite, Race, RaceItem


class RaceSpider(DjangoSpider):

    name = 'race_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(RacesWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Race
        self.scraped_obj_item_class = RaceItem
        super(RaceSpider, self).__init__(self, *args, **kwargs)