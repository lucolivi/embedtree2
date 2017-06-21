#Load data and test data
import os
import json
from collections import Counter


class LearnContent(list):
    def __init__(self, title):
        self.title = title
        self.parent = None

    def _str_version(self):
        return self.title
        #return "{} ({})".format(self.title, self.__len__())

    def content_as_text(self):
        return " ".join([cont.title for cont in self])


    def __str__(self):
        return self._str_version()

    def __repr__(self):
        return self._str_version()

    def __setitem__(self, i, y):
        assert isinstance(y, LearnContent)
        y.parent = self
        return super(LearnContent, self).__setitem__(i, y)

    def append(self, obj):
        assert isinstance(obj, LearnContent)
        obj.parent = self
        return super(LearnContent, self).append(obj)


class LearnContents(list):
    def __init__(self, folder="learn_data", children_folders=None):
        #Load data and create learn content objects
        json_data = self._load_json_data(folder, children_folders)
        for content_data in json_data:
            self._create_and_load_learn_contents(content_data)

        #Create titles frequency counter
        this_list = self
        all_content_titles = [lc.title for lc in this_list]
        self._title_counter = Counter(all_content_titles)


    def _create_and_load_learn_contents(self, content_data):
        lc = LearnContent(content_data['t'])
        self.append(lc) #Append every content to the main list
        if "c" in content_data:
            for subcont in content_data["c"]:
                lc.append(self._create_and_load_learn_contents(subcont))
        return lc

    def __setitem__(self, i, y):
        assert isinstance(y, LearnContent)
        return super(LearnContents, self).__setitem__(i, y)

    def append(self, obj):
        assert isinstance(obj, LearnContent)
        return super(LearnContents, self).append(obj)

    def _load_json_data(self, folder, children_folders=None):

        #Use all folders if none is specified
        if children_folders == None:
            children_folders = list()
            for maybe_dir in os.listdir(folder):
                if os.path.isdir(folder + "/" + maybe_dir):
                    children_folders.append(maybe_dir)

        #Create data paths
        data_paths = list()
        for child_folder in children_folders:
            folder_path = folder + "/" + child_folder
            for f in os.listdir(folder_path):
                data_paths.append(folder_path + "/" + f)

        #Load data
        json_data = list()
        for i, d_path in enumerate(data_paths):
            course_data = json.load(open(d_path))
            json_data.append(course_data)

        return json_data

    def search(self, term, match_case=False):
        """Return words that got the term, sorting by most used."""
        if not match_case:
            term = term.lower()

        results = list()
        this_list = self
        for i, content in enumerate(this_list):
            if not match_case:
                content_title = content.title.lower()
            else:
                content_title = content.title

            if term in content_title:
                results.append((content, self._title_counter[content.title], i))

        sorted_results = sorted(results, key=lambda a: a[1], reverse=True)

        return sorted_results



class LearnData():

    def __init__(self, folder="learn_data", children_folders=None):
        self._data = self._load(folder, children_folders)

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    #Search function to find topics
    def search_topics(term):
        term = term.lower()
        #Return words that got the term, sorting by most used
        results = [(topic, count) for topic, count in topics_counter.items() if term in topic]
        
        #return sorted results by count
        return sorted(results, key=lambda a: a[1], reverse=True)

    def _load(self, folder, children_folders=None):

        #Use all folders if none is specified
        if children_folders == None:
            children_folders = list()
            for maybe_dir in os.listdir(folder):
                if os.path.isdir(folder + "/" + maybe_dir):
                    children_folders.append(maybe_dir)

        #Create data paths
        data_paths = list()
        for child_folder in children_folders:
            folder_path = folder + "/" + child_folder
            for f in os.listdir(folder_path):
                data_paths.append(folder_path + "/" + f)
            
        #Load data       
        learn_data = list()        
        for i, d_path in enumerate(data_paths):
            course_data = json.load(open(d_path))
            learn_data.append(course_data)

        return learn_data



##Backup data load


# #Load data and test data
# import os
# import json


# udemy_folder = "udemy_data"
# udemydata_folders = [
#     'dev', 
#     'acad',
#     "it",
#     'mkt',
#     'op',
#     'packetpub_data'
# ]

# #Create data paths
# data_paths = list()
# for subf in udemydata_folders:
#     folder_path = udemy_folder + "/" + subf
#     for f in os.listdir(folder_path):
#         data_paths.append(folder_path + "/" + f)
        
        
# udemy_data = list()        
# for i, d_path in enumerate(data_paths):
#     course_data = json.load(open(d_path))
#     udemy_data.append(course_data)
#     #print("Done {}/{}".format(i+1, len(data_paths)))

# print("Done")
# print(udemy_data[4]["t"])