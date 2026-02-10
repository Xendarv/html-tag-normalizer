"""
HTML Tag Normalizer

This script reads an input text file containing HTML-like markup,
tracks unmatched opening/closing tags across lines, and writes a
cleaned, reformatted version to a timestamped output file.

Author: Peter N
"""

from datetime import datetime
import sys


def get_timestamped_filename(base_name: str) -> str:
    """
    Generate a filename prefixed with the current date and time.

    Colons are replaced with dashes to ensure filesystem compatibility.
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
    return f"{timestamp} {base_name}"


def process_file(input_path: str) -> list[str]:
    """
    Read and process the input file line-by-line, ensuring that
    opening and closing tags are properly balanced.

    Returns:
        A list of processed lines ready to be written to a new file.
    """
    processed_lines = []
    buffer = ""          # Stores incomplete lines that span multiple lines
    line_counter = 0

    with open(input_path, "r") as file:
        for raw_line in file:
            line_counter += 1
            print(f"\nProcessing line {line_counter}")

            # Trim leading/trailing whitespace
            line = raw_line.strip()

            # Determine whether we're dealing with embed tags
            if "embed" in line:
                print("Detected embed tags")
                open_token = "<emb"
                close_token = "/><emb"
            else:
                print("Detected standard tags")
                open_token = "<"
                close_token = "</"

            # Prepend buffered content if previous line was incomplete
            if buffer:
                line = buffer + line

            open_count = line.count(open_token)
            close_count = line.count(close_token)

            print(f"Open tags: {open_count}, Close tags: {close_count}")

            # Case 1: Line contains no tags
            if open_count == 0 and close_count == 0:
                print("No tags found, skipping")
                buffer = ""

            # Case 2: Standard tags are balanced
            # Each standard tag pair contributes one '<' in opening and one in closing
            elif open_token == "<" and open_count == (2 * close_count):
                print("Standard tags balanced, writing line")
                processed_lines.append(line)
                buffer = ""

            # Case 3: Embed tags need to be split into separate lines
            elif open_token == "<emb" and open_count == (close_count + 1):
                print("Embed tags balanced after formatting")
                line = line.replace("/><emb", "/> <emb")

                # Split into individual tag lines
                split_lines = [segment + ">" for segment in line.split(">") if segment]
                processed_lines.extend(split_lines)
                buffer = ""

            # Case 4: Line is incomplete, store it in the buffer
            else:
                if len(line) >= 3:
                    print("Unbalanced tags detected, buffering line")
                    buffer = line

    return processed_lines


def write_output_file(lines: list[str], output_path: str) -> None:
    """
    Write processed lines to a new file.
    """
    with open(output_path, "x") as output_file:
        for line in lines:
            print(line)
            output_file.write(f"{line}\n")


def main() -> None:
    """
    Main execution flow.
    """
    input_file = "Music Webpage.txt"
    output_file = get_timestamped_filename("Music Page.txt")

    processed_lines = process_file(input_file)
    write_output_file(processed_lines, output_file)

    input("\nPress any key to exit...")
    sys.exit(0)


if __name__ == "__main__":
    main()
