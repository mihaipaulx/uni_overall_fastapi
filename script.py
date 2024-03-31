from bs4 import BeautifulSoup
# from collections import defaultdict

import time
import random

from util.CustomDriver import CustomDriver
from util.cookies import accept_cookies
from util.domain import get_domain
from util.to_utf8 import to_utf8
from util.Link import Link
from util.update_loading import update_loading

from keywords import keywords

LOADING_PROGRESS_UNIT = 100 / (len(keywords))

def get_overall(uni_url):
  loading_progress = 0

  link = Link()

  with CustomDriver() as driver:
    for field, keyword_types in keywords.items():
      found_link = False
      field_query = keyword_types["query"]
      uni_url_domain = get_domain(uni_url)
      query = f'"{uni_url_domain}" {field_query}'
      url = link.build(query)

      driver.get(url)

      driver.implicitly_wait(2)

      accept_cookies(driver)

      soup = BeautifulSoup(driver.page_source, "html.parser")

      anchors = soup.find_all("a")

      if anchors:
        for anchor in anchors:
          result_url = anchor.get("href")

          result_domain = get_domain(result_url)
          uni_domain = get_domain(uni_url)

          # Ensure both domains are of the same type and anchor is part of main results before processing
          if uni_domain not in result_domain or not anchor.has_attr("aria-label"):
            continue

          if any(substring in result_url for substring in keyword_types["url"]):
            found_link = True
            time.sleep(random.uniform(2, 3))
            loading_progress = update_loading(loading_progress, LOADING_PROGRESS_UNIT)
            yield to_utf8({
              "data": {
                "label": field_query,
                "url": result_url,
              },
              "progress": loading_progress
            })

            print(f"Found {field_query} link: {result_url}")
            break

        if found_link == False:
          loading_progress = update_loading(loading_progress, LOADING_PROGRESS_UNIT)
          yield to_utf8({
            "progress": loading_progress
          })