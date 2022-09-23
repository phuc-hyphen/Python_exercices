# from cgi import print_arguments
import pytube
import sys
from colorama import Fore, Style

#
# class downloadvideo:
#     def __init__(self, filename, video):
agr_dict = {
    'v_url': "",
    'v_type': "mp4",
    'v_name': "",
    'v_location': "/home/huu-phuc-le/Downloads",
    'v_infor': False
}
help = f'''
---------------------------------------------------------------------------------------------------
{Fore.BLUE}NAME {Style.RESET_ALL}
    DownloadVideo
{Fore.BLUE}DESCRIPTION{Style.RESET_ALL}
    ▒█▀▄▀█ █░░█ ▒█▀▀▄ █▀▀█ █░░░█ █▀▀▄ █░░ █▀▀█ █▀▀█ █▀▀▄ ▒█░░▒█ ░▀░ █▀▀▄ █▀▀ █▀▀█ 
    ▒█▒█▒█ █▄▄█ ▒█░▒█ █░░█ █▄█▄█ █░░█ █░░ █░░█ █▄▄█ █░░█ ░▒█▒█░ ▀█▀ █░░█ █▀▀ █░░█ 
    ▒█░░▒█ ▄▄▄█ ▒█▄▄▀ ▀▀▀▀ ░▀░▀░ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ░░▀▄▀░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀▀
{Fore.BLUE}SYNOPSIS{Style.RESET_ALL}
    {Fore.GREEN}python DownloadVideo.py [options]{Style.RESET_ALL}
{Fore.BLUE}OPTIONS{Style.RESET_ALL}
    {Fore.CYAN}-h, --help{Style.RESET_ALL}
            Show basic help message and exit
    {Fore.CYAN}-i, --infor{Style.RESET_ALL}
            Show some basic information of the video of which is gonna be downloaded
    {Fore.CYAN}-l, --location   LOCATION{Style.RESET_ALL}
            Set the location where you want to save the video(default: C:/users/p.le-huu/Downloads)
    {Fore.CYAN}-u, --url    URL{Style.RESET_ALL}
            Set the url where you want to download the video
    {Fore.CYAN}-t, --type  TYPE{Style.RESET_ALL}
            Set the type of video to be saved (audio-mp3, video-mp4)(default: video)  
    {Fore.CYAN}-n, --name  TYPE{Style.RESET_ALL}
            Set the name of video to be saved (default: video title)  
{Fore.LIGHTRED_EX}EXAMPLE{Style.RESET_ALL}
    python DownloadVideo.py --help
    python DownloadVideo.py -i -u https://www.youtube.com/watch?v=6WtQkEw8wcQ -l C:/users/p.le-huu/Downloads -t mp4
{Fore.YELLOW}VERSION : 1.0.0{Style.RESET_ALL}
---------------------------------------------------------------------------------------------------     
'''


def my_parser(arguments):
    i = 1
    while (i < len(arguments)):
        if arguments[i] == "-u" or arguments[i] == "--url":
            agr_dict['v_url'] = arguments[i+1]
            i += 2
        elif arguments[i] == "-t" or arguments[i] == "--type":
            agr_dict['v_type'] = arguments[i+1]
            i += 2
        elif arguments[i] == "-l" or arguments[i] == "--location":
            agr_dict['v_location'] = arguments[i+1]
            i += 2
        elif arguments[i] == "-i" or arguments[i] == "--infor":
            agr_dict['v_infor'] = True
            i += 1
        elif arguments[i] == "-n" or arguments[i] == "--name":
            agr_dict['v_name'] = arguments[i+1]
            i += 2
        elif arguments[i] == "-h" or arguments[i] == "--help":
            exit(help)
        else:
            exit("Unknown argument: " + arguments[i])


def print_infor(yt):
    print("Title", yt.title)
    print("Author", yt.author)
    print("Publish date", yt.publish_date)
    print("Lenght of video", yt.length, "seconds")


def download(yt):
    if agr_dict['v_infor']:
        print_infor(yt)
    if agr_dict['v_type'] == "mp4":
        try:
            yt.streams.get_highest_resolution().download(
                agr_dict['v_location'], filename=agr_dict['v_name'] + '.mp4')
        except pytube.exceptions.RegexMatchError as e:
            exit("Error downloading video")
    elif agr_dict['v_type'] == "mp3":
        try:
            yt.streams.get_audio_only().download(
                agr_dict['v_location'], filename=agr_dict['v_name'] + '.mp3')
        except pytube.exceptions.RegexMatchError as e:
            exit("Error downloading video!!!")


if(len(sys.argv) < 2):
    print("Syntax error !! At least 1 argument required!, got " + str(len(sys.argv)-1))
    exit("HELP : python DownloadVideo.py --help ")

my_parser(sys.argv)

if agr_dict['v_url'] == '':
    exit('Error: URL missing !!!')
try:
    yt = pytube.YouTube(agr_dict['v_url'])
except Exception as e:
    exit(e)
if agr_dict['v_name'] == '':
    agr_dict['v_name'] = yt.title
# print(agr_dict)
download(yt)
print("Download finish !!!, the file saved at " + agr_dict['v_location'])
