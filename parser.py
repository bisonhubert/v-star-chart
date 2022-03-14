from bs4 import BeautifulSoup


class PlanetParser:
    def __init__(self, html=None):
        self.html = html
        self.soup = None if html is None else BeautifulSoup(html, "html.parser")
        self.planets = None

    def _get_planets(self):
        # HTML node tree for planets:
        # html node tree has all planets and descriptions as sibling <p> tags.
        # the first 11 p tags with 'zp-subheading' class are the collection of planets.
        # the sibling p tags without a class name after a 'zp-subheading' p tag
        # contain the descriptions of the planetary alignment.
        nodes = []
        node = None
        node_counter = 0
        current_node_name = None  # ie: 'sun', 'ascendant', 'pluto'
        p_tags = self.soup.findAll("p")
        # Logic for setting planets:
        # 1. get all <p> tags on the page
        # 2. filter up to (excluding) the 12th <p> tag with class 'zp-subheading'
        for tag in p_tags:
            if tag.attrs.get("class") is None:
                for content in tag.contents:
                    new_content = str(content)
                    if "</" in new_content:
                        new_content = "".join(content.contents)
                    if new_content:
                        content = "".join(new_content)
                        if node["content"]:
                            content = f'{node["content"]}\n{content}'
                        node["content"] = content
            else:
                content = f"{tag.contents[0]}\n"
                current_node_name = content.split(" ")[0].lower()
                if node is None:
                    node = {"name": current_node_name, "content": content}
                if node["name"] != current_node_name:
                    node_counter += 1
                    if node_counter > 11:
                        break
                    nodes.append(node)
                    node = {"name": current_node_name, "content": content}
        return nodes

    def run(self):
        if self.soup is None:
            return self
        self.planets = self._get_planets()
        return self
