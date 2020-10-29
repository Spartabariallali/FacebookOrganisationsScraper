from amnesty_scrape import amnesty_scrape_func
from cafod_scrape import cafod_scrape_func
from oxfamsouthsudan_scrape import oxfam_scrape_func
from threading import Thread


if __name__ == "__main__":
    # Thread(target = cafod_scrape_func).start()
    # Thread(target= oxfam_scrape_func).start()

    # Uncomment the function that you want to run, running them at the same time will sometimes lead to errors due to cookies disabling
    cafod_scrape_func()
    #oxfam_scrape_func()