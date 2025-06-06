from logging import DEBUG

from pom_grammar import PresentableGrammar
from utils.util_fmk import read_text
from utils.util_flogging import flogger
from utils.util_lark import pretty_print_parse_tree
from utils.util_text_markup import markup_text_lines

# from utils.util_lark_debug import debug_parse_with_trace, debug_tokens_detailed


def test_pom():
    flogger.info("Starting to test POM")
    flogger.setLevel(DEBUG)

    lark_config = {
        "case_sensitive": False,
        "ambiguity": "explicit",
        "debug": True,
        "lexer": "dynamic",
        "start": "start0",
    }

    g = PresentableGrammar("Lit_01", format_name="dull", config=lark_config)
    flogger.info("Grammar created")
    print(g)

    path = "models/Lit_01/SamplerClass0.md"
    flogger.infof(f"Trying file {path}")
    try_file(g, path)
    flogger.info("Done testing POM")


def try_file(g, path):
    text = read_text(path)
    print("Text is: ", text)

    lines = text.split("\n")

    print(f"\nLines are: ({len(lines)})")
    for line in lines:
        print("\n", line)
    # marked_lines = markup_text_lines(lines, debug=True)

    # print(f"\nMarkedLines are: ({len(marked_lines)})")
    # trimmed_lines = []
    # for line in marked_lines:
    #     if "===" in line:
    #         break
    #     trimmed = line.replace(" ; \n", "")
    #     trimmed_lines.append(trimmed.rstrip())
    #     print("\t", line)

    # print(f"\nTrimmed lines are: ({len(trimmed_lines)})")
    trimmed_lines = lines
    for line in trimmed_lines:
        print("\t", line)

    marked_text = "\n".join(trimmed_lines) + "\n"
    print("\nMarked text is: \n[", marked_text, "\n]")

    # Run debugging functions
    print("\nDEBUG TOKENS")

    g.debug_tokens(marked_text)
    print("\nDEBUG INCREMENTAL")

    g.debug_incremental_parse(marked_text)

    # Optional: add trace debugging
    print("\nDEBUG WITH TRACE")
    g.debug_with_trace(marked_text)
    return
    result = g.parse(marked_text)

    print("---- Prettier Parse Tree ----")
    print(
        pretty_print_parse_tree(
            result.parse_tree, max_text_length=30, text_column_width=35
        )
    )
    print("-----------------------------")


def try_file2(g, path):
    text = read_text(path)
    print("Text is: ", text)

    # Debug grammar and tokens before parsing
    g.debug_grammar_and_tokens(text)

    result = g.parse(text)
    print("parse tree = ", result.parse_tree)


test_pom()
