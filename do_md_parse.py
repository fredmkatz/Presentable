import markdown
from bs4 import BeautifulSoup as Soup

# from plantuml import PlantUML
from do_plantweb import render_puml_png

from utils_pom.util_fmk_pom import read_text, write_text
from csv2html import csv2html
CONTENT = """
    actor Foo1
    boundary Foo2
    control Foo3
    entity Foo4
    database Foo5
    Foo1 -> Foo2 : To boundary
    Foo1 -> Foo3 : To control
    Foo1 -> Foo4 : To entity
    Foo1 -> Foo5 : To database
    """

n_pumls = 0
# def get_plantuml_url(plant_uml_text):
#     plantUML = PlantUML(url='http://www.plantuml.com/plantuml/img/', basic_auth={}, form_auth={}, http_opts={}, request_opts={})
#     url = plantUML(plant_uml_text)
    
#     print("PLANTUML URL is ", url)
#     return url


def as_prose_html(markdown_string) -> str:
    
    # translate to html text
    html_str = markdown.markdown(markdown_string, extensions=['extra',  'toc'])
    
    # parse the html, to make reprairs
    html_soup = Soup(html_str, 'html.parser')
    
    # make repairs
    for codeblock in html_soup.find_all("code"):
        print("SOUP found codeblock", codeblock)
        current_classes = codeblock.get("class")
        print("Current soup classes are ", current_classes)
        if "language-mermaid" in current_classes:
            newclasses = current_classes + ["mermaid"]
            print("setting new code classes to ", newclasses)
            codeblock['class'] = newclasses
            print(f"New code classes: {codeblock.get('class')}")
            continue
        
        if "language-csv" in current_classes:
            csv = codeblock.get_text()
            print("FOUND CSV CODEBLOCK.  CSV is")
            print(csv)
            table_html = csv2html(csv)
            print("HTML table is")
            print(table_html)
            table_soup = Soup(table_html, 'html.parser')
            codeblock.parent.insert_after(table_soup)
            continue
        
        if "language-puml" in current_classes:
            puml = codeblock.get_text()
            print("FOUND PUML CODEBLOCK.  PUML is")
            print(puml)
            puml = puml.replace("@startuml", "")
            puml = puml.replace("@enduml", "")
            print("... and clean PUML is")
            print(puml)

            
            global n_pumls
            n_pumls += 1

            png_file_name = f"diagram{n_pumls}.png"
            print(f"creating png in {png_file_name}")
            url = render_puml_png(puml, png_file_name)
            # table_html = csv2html(csv)
            # print("HTML table is")
            # print(table_html)
            # table_soup = Soup(table_html, 'html.parser')
            # codeblock.parent.insert_after(table_soup)
            continue

            


    html_str2 = html_soup.prettify()
    return html_str2




if __name__ == "__main__":

    input_path = r"ldm\ldm_models\Literate.md"

    input_path = r"ldm\ldm_models\LiterateTester.md"
    input_path = "mdtestdocs/mdtest_doc.md"
    input_path = r"ldm\ldm_models\LiterateTester.md"

    
    output_path = f"{input_path}_2.html"

    markdown_string = read_text(input_path)
    html = as_prose_html(markdown_string)

    # html = markdown.markdown(markdown_string, extensions=['extra', 'codehilite', 'toc'])
    write_text(output_path, html)

