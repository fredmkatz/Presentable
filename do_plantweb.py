from plantweb.render import render, render_cached

def render_puml_png(puml_text, output_file):

    print('==> INPUT to render_puml_png:')
    print(puml_text)

    plantuml_server_url = "http://www.plantuml.com/plantuml"
    try:
        (png_output, sha)= render_cached(plantuml_server_url, "png", puml_text)
        
        
        with open(output_file,"wb") as f:
            f.write(png_output)

        print(f"PUML PNG file saved to: {output_file}")
    except Exception:
        print("PUML Failed with input ", puml_text, " - ", output_file)
    return output_file





if __name__ == '__main__':
    
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
    
    CONTENT2 = """
    nwdiag {
        network {
            Component;

            Component -- Literate;
            Component -- Subject;
            Component -- Class;
            Component -- AttributeSection;
            Component -- Attribute;

            Subject [description = "Domain entity"];
            Literate [description = "Core implementation"];
            Class [description = "Schema definition"];
            AttributeSection [description = "Property group"];
            Attribute [description = "Individual property"];
        }
    }
    """
    output_file = "PlantUML.png"

    
    outfile = render_puml_png(CONTENT2, output_file=output_file)

