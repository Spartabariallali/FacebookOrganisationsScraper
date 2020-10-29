from amnesty_scrape import amnesty_scrape_func
from cafod_scrape import cafod_scrape_func
from oxfamsouthsudan_scrape import oxfam_scrape_func



if __name__ == "__main__":
    # Thread(target = organisation_scrape).start()
    # Thread(target = cafod_scrape_func).start()
    # Thread(target= amnesty_scrape_func).start()
    cafod_scrape_func()
    # amnesty_scrape_func() # Additional Changes Needed
    oxfam_scrape_func()