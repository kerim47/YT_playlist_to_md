
tag_templates = {
    "d":{
        "open" : "<details>\n",
        "close": "</details>\n"
    },
    "s":{
        "open" : "<summary>",
        "close": "</summary>\n"
    } 
}


def create_both_markdown(tag_list, parent_tagname):
    markdown_text = ""
    first_tag = tag_templates[parent_tagname]['open']
    last_tag  = tag_templates[parent_tagname]['close']

    markdown_text += first_tag

    markdown_text +=  tag_list 

    markdown_text += last_tag
    return markdown_text


def write_to_markdown_file(markdown_text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown_text)

def generate_html_tag(tag_name, content):
    template = tag_templates.get(tag_name)
    if template:
        return f"{template['open']}{content}{template['close']}"
    else:
        return ""

def html_iframe_tag(video_id):
    return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\n'

def generate_nested_structure_details_summary(tags, indent_level=0):
    if not isinstance(tags, dict):
        return ""

    structure = ""
    indent = "    " * indent_level
    for tag, content in tags.items():
        tag_template = tag_templates.get(tag)
        if tag_template:
            # inner_indent = "    " * (indent_level + 1)
            if tag == "d":
                inner_structure = generate_nested_structure_details_summary(content, indent_level=indent_level + 1)
                structure += f"{indent}<details>\n{inner_structure}{indent}</details>\n"
            elif tag == "s":
                structure += f"{indent}<summary>{content}</summary>\n"
    return structure

