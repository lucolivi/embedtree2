from bs4 import BeautifulSoup

def __extract_html_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    links = list()

    for a_tag in soup.findAll("a"):

        #If the a tag has no href attr, skip it
        if not a_tag.has_attr("href"):
            continue

        link_href = a_tag['href']
        link_text = a_tag.get_text()

        links.append([link_href, link_text])

    return links


def __filter_wiki_links(links):

    blocked_link_terms = set([
        "(disambiguation)", #Not interested in disambiguation pages
        ":" #Pages with colon are offen special pages. Not sure if there is articles with colon
    ])

    filtered_links = list()

    for link_href, link_text in links:

        #If the href does not starts with "/wiki/", skip it
        if link_href.find("/wiki/") != 0:
            continue

        #Check if some blocked term is present in the href, if so, skip the link
        skip_link = False
        for term in blocked_link_terms:
            if link_href.find(term) != -1:
                skip_link = True
                break
        if skip_link:
            continue

        #Get only the link portion
        #We MUST NOT use last index of / to get the path cause some titles like TCP/IP, have bar in the title
        #We should use the '/wiki/' string length
        filtered_link_href = link_href[6:]

        #Remove hashtag from url if any
        hashIndex = filtered_link_href.find("#")
        if hashIndex != -1:
            filtered_link_href = filtered_link_href[:hashIndex]

        filtered_links.append([filtered_link_href, link_text])

    return filtered_links

def __remove_page_boxes(html):
    """Function to treat the data, remove unecessary things etc."""

    soup = BeautifulSoup(html, 'html.parser')

    #Clear table of contents if any
    for node in soup.findAll(id='toc'):
        node.decompose()

    #Clear top info table if any
    for node in soup.findAll(class_='ambox'):
        node.decompose()

    #Clear info box if any
    for node in soup.findAll(class_='infobox'):
        node.decompose()

    #Clear verticalbox if any
    for node in soup.findAll(class_='vertical-navbox'):
        node.decompose()

    #Clear navbox if any
    for node in soup.findAll(class_='navbox'):
        node.decompose()

    return str(soup)

def __split_html_h2_sections(html):
    """Function to split html document in sections (use h2 tags as divisors)"""

    soup = BeautifulSoup(html, 'html.parser')

    sections = list()

    curr_section = ""

    for tag in soup.children:

        #If it is a valid tag (invalid tags has no 'name' property)
        if tag.name == None:
            continue

        #Start new section in case the tag is h2
        if tag.name == 'h2':
            sections.append(curr_section)
            curr_section = ""

        curr_section += str(tag)

    return sections



def __split_into_sections(htmlObj):
    """Function to split html document in sections (use h2 tags as divisors)"""

    #Init var to store sections
    sectionObjs = [[]]

    for tag in htmlObj.children:
        #Start new section in case the tag is h2
        if tag.name == 'h2':
            sectionObjs.append([])

        #If it is a valid tag (invalid tags has no 'name' property)
        if tag.name != None:
            sectionObjs[len(sectionObjs) - 1].append(tag)

    return sectionObjs