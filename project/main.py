import re
from enum import Enum

class DirectiveType(Enum):
    index = f"*Index: {content}"


def open_file(file_name):
    # Takes a file name of a myst markdown file in the project directory
    # Opens the myst markdown file and reads the contents
    # Returns the contents of the myst markdown file in a string
    
    with open(f'../{file_name}.md', 'r') as f:
        myst_doc = f.read()
        
    return myst_doc


def find_directives(myst_doc):
    # Takes the contents of a myst markdown file as a string
    # Finds all the directives in the myst markdown file
    # Returns a list of all the directives in the myst markdown file as tuples (location, directive type)
    
    r_directive = r"```{[a-z|A-Z|-]*}"

    directives = []
    for match in re.finditer(r_directive, myst_doc):
        directives.append((myst_doc[match.start()+4:match.end()-1], match))
        
    return directives
    
def main():
    myst = open_file("example01")
    directives = find_directives(myst)
    for directive in directives:
        print(directive[0])
        print(directive[1].start(), directive[1].end())


if __name__ == "__main__":
    main()