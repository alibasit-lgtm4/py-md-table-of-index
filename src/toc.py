import re

def generate_toc(md_text):
    headings = re.findall(r"^##? (.+)$", md_text, flags=re.M)
    toc = []
    for h in headings:
        anchor = h.lower().replace(" ", "-")
        toc.append(f"- [{h}](#{anchor})")
    return "\n".join(toc)

if __name__ == "__main__":
    sample = "# Main Title\n## Section One\n## Section Two"
    print(generate_toc(sample))
