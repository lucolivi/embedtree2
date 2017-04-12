from download import __download_page_data
from parse import __extract_html_links, __filter_wiki_links, __split_html_h2_sections, __remove_page_boxes


if __name__ == "__main__":

    def test_module():
        href, title, pageid, html = __download_page_data("MQTT", "en", 60)
        links = __extract_html_links(html)
        filtered_links = __filter_wiki_links(links)

        for sec in __split_html_h2_sections(__remove_page_boxes(html)):
            print("")
            print(sec)
            #for s in sec:
                #print("")
                #print(s)


        #print(filtered_links)

    test_module()