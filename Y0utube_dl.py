import youtube_dl
import os
import time

"""Y0utube_dl is a small and comprehensive library of the major youtube_dl library,
    created solely for the convenience of downloading files from YouTube."""

class Y0utube_dl:

    """Y0utube_dl Class only can use for download video,
    for download audio use Y0utube (subclass <<Y0utube_dl>>)
    Attention don't use Y0utube_Audio for downloading video"""

    ex_error = youtube_dl.utils.ExtractorError
    dl_error = youtube_dl.utils.DownloadError

    dic = ""

    def __init__(self,
                 url,):
        self.url = url


    @property
    def extract_info(self):

        """This function returns the required information to us from YouTube """

        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

        with ydl:
            result = ydl.extract_info(self.url,
                download=False  # We just want to extract the info
            )

        if 'entries' in result:
            # Here we want all the entries,Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result

        return video

    def list_download(self):

        """ This function prints the list of available files to us """

        print("\n\n!!..Attention Download By Code..!!\n\n")

        time.sleep(3)

        print("Size---Code for Dl--Quality--Type")

        print(50 * "-")

        for i in self.extract_info["formats"]:
            size = str(i["filesize"])

            if size != "None":

                if len(size) == 6:

                    v = int(size) / 1000
                    if i["height"] != None:

                        print(50 * "-")
                        print(int(v), "KB", f'Code : {i["format_id"]} ', f"{i['height']}p", i["ext"])


                elif len(size) == 7:
                    w = int(size) / 1000000
                    if i["height"] != None:
                        print(50 * "-")
                        print(int(w), "Mb", f'Code : {i["format_id"]} ', f"{i['height']}p", i["ext"])

                elif len(size) == 8:
                    x = int(size) / 1000000
                    if i["height"] != None:
                        print(50 * "-")
                        print(int(x), "Mb", f'Code : {i["format_id"]} ', f"{i['height']}p", i["ext"])


                elif len(size) == 9:
                    y = int(size) / 1000000
                    if i["height"] != None:
                        print(50 * "-")
                        print(int(y), "Mb", f'Code : {i["format_id"]} ', f"{i['height']}p", i["ext"])

                elif len(size) == 10:
                    z = int(size) / 1000000
                    if i["height"] != None:
                        print(50 * "-")
                        print(int(z), "Gb", f'Code : {i["format_id"]} ', f"{i['height']}p", i["ext"])

        print("\n---------------","\nNone Size's:\n","Bellow ⬇⬇⬇⬇\n")
        for i in self.extract_info["formats"]:
            size = str(i["filesize"])
            if size == "None":
                print(f'Code : {i["format_id"]} ',"qulity :",i["height"],i["ext"])


        return (i["filesize"], i["format_id"], i["height"], i["ext"])



    def modified_list_download(self):
        """This function only prints modified code and real size,
        its better use this function when the self.list_download function has a exceptions (Index Error)"""
        
        dict_dl = {}
        size_dict = {}

        my_list = []
        file_sizes = []
        all_sizes = []
        qulity = []

        for list_dl in self.extract_info["formats"]:
            format_list = list_dl["format_id"]

            filesize = str(list_dl["filesize"])
            file_sizes.append(filesize)

            if not filesize == "None":

                if len(filesize) == 6:

                    v = int(filesize) / 1000

                    if list_dl["height"] != None:
                        all_sizes.append(v)
                        qulity.append(list_dl["height"])

                elif len(filesize) == 7:

                    w = int(filesize) / 1000000

                    if list_dl["height"] != None:
                        all_sizes.append(int(w))
                        qulity.append(list_dl["height"])

                elif len(filesize) == 8:
                    x = int(filesize) / 1000000

                    if list_dl["height"] != None:
                        all_sizes.append(int(x))
                        qulity.append(list_dl["height"])

                elif len(filesize) == 9:
                    y = int(filesize) / 1000000

                    if list_dl["height"] != None:
                        all_sizes.append(int(y))
                        qulity.append(list_dl["height"])


                elif len(filesize) == 10:
                    z = int(filesize) / 1000000

                    if list_dl["height"] != None:
                        all_sizes.append(int(z))
                        qulity.append(list_dl["height"])

            if filesize == 'None':
                pass


            my_list.append(format_list)

        w,x, y, z = 0, 0, 0,0
        for index in my_list:

            dict_dl.update({x : index})

            x += 1

        for item in all_sizes:
            size_dict.update({y : item})
            y += 1

        try:
            e = 0
            for key, val in dict_dl.items():

                if type(size_dict[z]) == float:

                    print("Size : ", int(size_dict[z]),"Kb"," | Qulity :",f"{qulity[z]}p",end="   ")
                    print(f"Code : {key}")

                elif file_sizes[z] == "None":
                    print(f'Code : {key} ', "qulity :", none_quilty[z], none_type[e])




                else:
                    print("Size : ", size_dict[z],"Mb"," | Qulity :",f"{qulity[z]}p",end="   ")
                    print(f"Code : {key}")

                z += 1
                e += 1

        except KeyError:
            pass


        print("\n---------------", "\nNone Size's:\n\n","Bellow ⬇⬇⬇⬇\n")

        if filesize == "None":
            pass
            # print(f'Code : {list_dl["format_id"]} ', list_dl["height"], list_dl["ext"])

    @property
    def return_my_list(self):

        """ This function is a property and only modifies the code for the except_list_download function """

        my_list = []

        for list_dl in self.extract_info["formats"]:
            if list_dl["height"] != None:
                format_list = list_dl["format_id"]

                my_list.append(format_list)

        return my_list


    def download_by_list_downloader(self,choice,its_dic = False,dic = dic):

        """This function downloads the files with the original code for us,
         if the code is not correct, an error will occur"""

        available_formats = self.return_my_list
        if its_dic == False:
            if str(choice) in available_formats:
                os.system(fr'youtube-dl -f {choice}+bestaudio -o ".\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError


        elif its_dic == True:
            if str(choice) in available_formats:
                os.system(fr'youtube-dl -f {choice}+bestaudio -o "{dic}\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError


    def download_by_modified_list(self,choice,its_dic = False,dic = dic):

        """This function downloads the files with the modified code for us."""
        order_choice = int(choice)

        available_formats = self.return_my_list
        if its_dic == False:
            if str(choice) in order_choice:
                os.system(fr'youtube-dl -f {self.return_my_list[order_choice]}+bestaudio -o ".\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError


        elif its_dic == True:
            if str(choice) in order_choice:
                os.system(fr'youtube-dl -f {self.return_my_list[order_choice]}+bestaudio -o "{dic}\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError
  



#Class Audio Downloader
#_________________________________________________________________________________________________________________________________________________________________________________________


class Y0utube_Audio(Y0utube_dl):

    dic = ""

    def list_audio(self):

        """ This function prints the list of available Audios to us. """

        print("\n\n!!..Attention Download By Code..!!\n\n")
        time.sleep(3)

        for i in self.extract_info["formats"]:
            size = str(i["filesize"])

            if not size == "None":

                if len(size) == 6:

                    v = int(size) / 1000

                    if i["height"] == None:

                        print(50 * "-")

                        i["height"] = "Audio"
                        print(int(v) ,"KU",f'Code : {i["format_id"]} ', i['height'], i["ext"])

                elif len(size) == 7:

                    w = int(size) / 1000000

                    if i["height"] == None:

                        print(50 * "-")

                        i["height"] = "Audio"
                        print(int(w) ,"Mb",f'Code : {i["format_id"]} ', i['height'], i["ext"])

                elif len(size) == 8:
                    x = int(size) / 1000000

                    if i["height"] == None:

                        print(50 * "-")

                        i["height"] = "Audio"
                        print(int(x) ,"Mb",f'Code : {i["format_id"]} ', i['height'], i["ext"])


                elif len(size) == 9:
                    y = int(size) / 1000000

                    if i["height"] == None:

                        print(50 * "-")

                        i["height"] = "Audio"
                        print(int(y) ,"Mb",f'Code : {i["format_id"]} ', i['height'], i["ext"])

                elif len(size) == 10:

                    z = int(size) / 1000000

                    if i["height"] == None:

                        print(50 * "-")

                        i["height"] = "Audio"
                        print(int(z) ,"Gb",f'Code : {i["format_id"]} ', i['height'], i["ext"])


    def except_audio_list(self):

        """This function only prints modified code and real size,
        its better use this function when the self.list_audio function has a exceptions (Index Error)"""

        dict_dl = {}
        size_dict = {}

        my_list = []
        all_sizes = []

        for list_dl in self.extract_info["formats"]:
            format_list = list_dl["format_id"]

            filesize = str(list_dl["filesize"])

            if not filesize == "None":

                if len(filesize) == 6:

                    v = int(filesize) / 1000

                    if list_dl["height"] == None:

                        list_dl["height"] = "Audio"
                        all_sizes.append(int(v))

                elif len(filesize) == 7:
                    w = int(filesize) / 1000000

                    if list_dl["height"] == None:

                        list_dl["height"] = "Audio"
                        all_sizes.append(int(w))

                elif len(filesize) == 8:
                    x = int(filesize) / 1000000

                    if list_dl["height"] == None:

                        list_dl["height"] = "Audio"
                        all_sizes.append(int(x))

                elif len(filesize) == 9:
                    y = int(filesize) / 1000000

                    if list_dl["height"] == None:

                        list_dl["height"] = "Audio"
                        all_sizes.append(int(y))


                elif len(filesize) == 10:
                    z = int(filesize) / 1000000

                    if list_dl["height"] == None:

                        list_dl["height"] = "Audio"
                        all_sizes.append(int(z))


            elif filesize == "None":
                print(25 * "✩")
                print("Best Quality", f'Code : {list_dl["format_id"]} ', list_dl["height"], list_dl["ext"])
                print(25 * "✩")

            my_list.append(format_list)

        x = 0
        for index in my_list:

            dict_dl.update({x : index})

            x += 1

        y = 0
        for item in all_sizes:
            size_dict.update({y : item})
            y += 1

        z = 0
        try:
            for key, val in dict_dl.items():
                print(50 * "-")
                print("Size : ", size_dict[z], "Mb", end="   ")
                print(f"Code : {key}")
                z += 1

        except KeyError:
            pass

    @property
    def return_my_list(self):

        """ This function is a property and only modifies the code for the except_list_download function """

        my_list = []

        for list_dl in self.extract_info["formats"]:
            if list_dl["height"] == None:
                format_list = list_dl["format_id"]

                my_list.append(format_list)

        return my_list


    def download_audio(self,choice):

        """This function downloads the Audio with the original code for us,
         if the code is not correct, an error will occur"""

        for i in self.extract_info["formats"]:

            available_formats = self.return_my_list
            if its_dic == False:
                if str(choice) in available_formats:
                    os.system(fr'youtube-dl -f {choice}+bestaudio -o ".\%(title)s.%(ext)s" {self.url}')

                    print("\n Your Download has been completed..!!")
                else:
                    raise IndexError


            elif its_dic == True:
                if str(choice) in available_formats:
                    os.system(fr'youtube-dl -f {choice}+bestaudio -o "{dic}\%(title)s.%(ext)s" {self.url}')

                    print("\n Your Download has been completed..!!")
                else:
                    raise IndexError

    def modified_audio_download(self,its_dic = False,dic = dic):

        """This function downloads the Audio with the modified code for us."""

        order_choice = int(choice)

        available_formats = self.return_my_list
        if its_dic == False:
            if str(choice) in order_choice:
                os.system(fr'youtube-dl -f {self.return_my_list[order_choice]}+bestaudio -o ".\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError


        elif its_dic == True:
            if str(choice) in order_choice:
                os.system(fr'youtube-dl -f {self.return_my_list[order_choice]}+bestaudio -o "{dic}\%(title)s.%(ext)s" {self.url}')

                print("\n Your Download has been completed..!!")
            else:
                raise IndexError


if __name__ == "__main__":
    pass
