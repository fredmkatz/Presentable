from lark import Lark
from utils.util_lark import (
    pretty_print_parse_tree,
    lark_to_json_pretty,
    lark_to_yaml_pretty,
)

from utils.util_fmk import read_text, write_text


def try_lark(g_path: str, d_path: str) -> bool:
    doc_text = read_text(d_path)

    print(f"Grammar path: {g_path}")
    print(f"Document path: {d_path}")
    parser = parse_grammar_file(g_path)
    if not parser:
        print(f"Error: Failed to create parser from grammar at {g_path}")
        return False

    print(f"Parser created successfully")
    # Parse the document text

    parse_tree = parse_text(parser, doc_text)
    if parse_tree:
        print("Parse tree created successfully")
        ptree1 = parse_tree.pretty()
        out1 = d_path + ".pretty.txt"
        write_text(out1, ptree1)
        print(f"Parse tree written to {out1}")
        # print(f"Parse tree: {ptree1}")

        ptree2 = pretty_print_parse_tree(
            parse_tree, max_text_length=30, text_column_width=35, indent_size=1
        )

        out2 = d_path + ".prettier.txt"
        write_text(out2, ptree2)

        print("YAMLing parse tree")
        ptree4 = lark_to_yaml_pretty(parse_tree, indent=2)
        out4 = d_path + ".lark.yaml"
        write_text(out4, ptree4)
        print(f"Parse tree YAML written to {out4}")

        # # print(parse_tree.pretty())
        # print(ptree2)
    else:
        print("Error: Failed to parse document text")
        return False


def parse_grammar_file(grammar_file_path, start_rule="start"):
    """
    Parses a grammar file using Lark and returns the parse tree.

    Args:
        grammar_file_path (str): The path to the grammar file.
        start_rule (str, optional): The starting rule for parsing. Defaults to 'start'.

    Returns:
        lark.Tree: The parse tree if parsing is successful, None otherwise.
    """
    try:
        with open(grammar_file_path, "r", encoding="utf-8") as f:
            grammar_text = f.read()
    except FileNotFoundError:
        print(f"Error: Grammar file not found at {grammar_file_path}")
        return None

    try:
        # parser = Lark(grammar_text, start=start_rule)
        # Parser configuration
        parser = Lark(grammar_text, start="start", parser="earley", lexer="dynamic")
        # parser = Lark(grammar_text, start="start", parser="lalr", lexer="contextual")
        return parser
    except Exception as e:
        print(f"Error: Failed to create parser: {e}")
        return None


def parse_text(parser, text):
    """Parses text using the provided Lark parser."""
    try:
        tree = parser.parse(text)
        return tree
    except Exception as e:
        print(f"Error: Failed to parse text: {e}")
        return None


if __name__ == "__main__":
    grammar_path = "larks/ldm_blocks.lark"
    doc_path = "samples/LDMMeta.md"
    try_lark(grammar_path, doc_path)

    # Example grammar (saved in grammar.lark)
    # expr: term (("+"|"-") term)*
    # term: factor (("*"|"/") factor)*
    # factor: ID | NUMBER | "(" expr ")"
    # ID: /[a-zA-Z]+/
    # NUMBER: /[0-9]+/
    # %import common.WS
    # %ignore WS
