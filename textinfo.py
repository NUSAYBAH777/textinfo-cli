
import sys

# ANSI colors 
RESET       = "\x1b[0m"
COLOR_LABEL = "\x1b[36m"   # cyan for labels
COLOR_VALUE = "\x1b[32m"   # green for values
COLOR_ERROR = "\x1b[31m"   # red for errors


def main():
    # 1. Validate that at least one argument
    if len(sys.argv) < 2:
        print(f"{COLOR_ERROR}Error:{RESET} no text provided.")
        print("Usage: textinfo <text>")
        sys.exit(1)

    # 2. Join all words into one string
  
    text = " ".join(sys.argv[1:])

    # 3. Extra validation: check that it’s not just spaces
    if text.strip() == "":
        print(f"{COLOR_ERROR}Error:{RESET} text is empty or only spaces.")
        sys.exit(1)

    # 4. Processing
    characters = len(text)
    words = len(text.split())

    # 5. Output with colors
    print(f"{COLOR_LABEL}Text:      {RESET}{text}")
    print(f"{COLOR_LABEL}Characters:{RESET} {COLOR_VALUE}{characters}{RESET}")
    print(f"{COLOR_LABEL}Words:     {RESET} {COLOR_VALUE}{words}{RESET}")


if __name__ == "__main__":
    main()
