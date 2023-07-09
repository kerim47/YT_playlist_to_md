import md_create as md_c
import playlist_tube as playtube
import toml

with open('config.toml', 'r') as file:
    config = toml.load(file)

playlist_id = config['playlist_id']
api_key = config['api_key']
path = config['path']


def get_result_playlist(playlist_id, api_key):
    regular_titles = playtube.get_playlist_title_and_id(playlist_id, api_key)
    result = []
    for video in regular_titles:
        iframe_tag = md_c.html_iframe_tag(video['id'])
        title_tag = md_c.generate_html_tag("s", video['title'])
        result_tag = title_tag + iframe_tag
        result.append(md_c.create_both_markdown(result_tag, "d"))
    return result

def run():
    md_result = get_result_playlist(playlist_id, api_key)[50:]
    result = ''.join([sub for sub in md_result])
    md_c.write_to_markdown_file(result, path)


if __name__ == "__main__":
    run()
