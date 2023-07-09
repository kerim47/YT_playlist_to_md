import requests

def get_playlist(playlist_id: str, api_key: str):
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
    part = "snippet"
    max_results = 50
    headers = {"Accept": "application/json"}

    videos = []

    next_page_token = None

    while True:
        params = {
            "part": part,
            "playlistId": playlist_id,
            "maxResults": max_results,
            "key": api_key,
            "pageToken": next_page_token
        }

        response = requests.get(base_url, headers=headers, params=params)
        data = response.json()

        if "items" in data:
            videos.extend(data["items"])

        if "nextPageToken" not in data:
            break

        next_page_token = data["nextPageToken"]

    return videos

def get_playlist_title_and_id(playlist_id: str, api_key: str):
    data = get_playlist(playlist_id, api_key)
    video_titles = []

    for item in data:
        video_info = item["snippet"]
        if "title" in video_info and "resourceId" in video_info:
            video_title = video_info["title"]
            video_id = video_info["resourceId"]["videoId"]
            video_titles.append({"title": video_title, "id": video_id})
    return video_titles

def get_playlist_titles(playlist_id, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
    part = "snippet"
    max_results = 50  # Her istekte en fazla 50 sonuç alacağız
    headers = {"Accept": "application/json"}

    titles = []

    # İlk istek için nextPageToken yok
    next_page_token = None

    while True:
        params = {
            "part": part,
            "playlistId": playlist_id,
            "maxResults": max_results,
            "key": api_key,
            "pageToken": next_page_token
        }

        response = requests.get(base_url, headers=headers, params=params)
        data = response.json()

        # Her sayfadan başlıkları alıp listeye ekleyelim
        for item in data["items"]:
            title = item["snippet"]["title"]
            titles.append(title)

        # Tüm sayfaları dolaştıysak döngüden çık
        if "nextPageToken" not in data:
            break

        # Sonraki sayfa için nextPageToken'ı güncelle
        next_page_token = data["nextPageToken"]
 
    return titles

def get_regular_titles(playlist_id, api_key, re = None):
    play_list_title = []
    for video_name in get_playlist_titles(playlist_id, api_key):
        if re is None:
            if len(video_name) > 1:
                play_list_title.append(video_name)
        elif re in video_name:
            parts = video_name.split(re, 1)
            if len(parts) > 1:
                play_list_title.append(parts)
    return play_list_title
