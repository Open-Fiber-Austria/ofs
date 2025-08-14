import os
import re
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page

class AutoGlossaryLinkPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig):
        """
        Load glossary terms and their target URLs from the glossary_links.md file.
        Converts relative URLs to absolute paths to ensure links work from any page.
        """
        glossary_path = os.path.join("includes", "glossary_links.md")
        self.glossary_terms = {}

        if os.path.exists(glossary_path):
            with open(glossary_path, encoding='utf-8') as f:
                for line in f:
                    match = re.match(r"\[([^\]]+)\]:\s*(.+)", line)
                    if match:
                        term, url = match.groups()

                        # Convert relative URLs to absolute paths
                        if not url.startswith("/"):
                            url = "/" + url.lstrip("/")
                        self.glossary_terms[term] = url
        else:
            raise FileNotFoundError(f"Glossary links file not found: {glossary_path}")

    def on_page_markdown(self, markdown: str, page: Page, config: MkDocsConfig, files):
        """
        Automatically link glossary terms in the Markdown pages.
        Only replaces terms with a URL if they appear as their own word, not within other words.
        Longer terms are processed first to avoid partial replacements (e.g., 'PPL' and 'PPo' before 'PP').
        """
        # Sort glossary terms longest to shortest
        for term in sorted(self.glossary_terms, key=len, reverse=True):
            # Match whole words only (no substrings) and avoid replacing text that's already a Markdown link
            pattern = r'(?<!\[)\b' + re.escape(term) + r'\b(?!\])'
            # Add brackets around plain text occurrences of glossary terms
            markdown = re.sub(pattern, f'[{term}]', markdown)

        # Append invisible Markdown reference definitions for the glossary links at the end of each page
        glossary_links = "\n".join(f"[{term}]: {url}" for term, url in self.glossary_terms.items())
        return f"{markdown}\n\n{glossary_links}"

