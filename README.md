# HTML Tag Normalizer

This is a small Python script I wrote to make the output from a website export
readable again for a human.

The original site stripped all line breaks and compacted everything into a
single long paragraph, which made it hard to inspect or edit manually.

This was written as a for-fun / helper script for a very specific, niche task.

## What it does

- Reads a text file containing HTML-like markup
- Looks for opening and closing tags
- Reconstructs sensible line breaks
- Buffers content when tags are split across lines
- Handles a few special embed-style tags that needed extra cleanup
- Writes the result to a new file with a timestamped name

The goal is readability, not correctness or full HTML validation.

## Why this exists

This started as a quick attempt to make a giant one-line export readable again.
As more edge cases showed up in the file, small fixes were added until the output
was “good enough” to work with by hand.

It’s intentionally simple and tailored to the patterns in the original export.

## Usage

1. Put the input text file in the same directory as the script
2. Update the input filename in `main()` if needed
3. Run the script with Python 3

A new output file will be created with a timestamp so the original stays untouched.

## Notes

- The input is not valid or well-formed HTML
- This uses string-based processing on purpose
- There is verbose print output to make it easier to see what the script is doing
- This probably won’t generalize well to other exports, and that’s fine

## License

MIT License.
