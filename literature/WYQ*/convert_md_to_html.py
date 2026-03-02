#!/usr/bin/env python3
"""
Convert markdown papers to HTML format
"""
import re
import sys
from pathlib import Path

def markdown_to_html(md_content):
    """Convert markdown content to HTML"""
    html = md_content
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    # Horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # Lists
    lines = html.split('\n')
    in_list = False
    result = []
    for line in lines:
        if re.match(r'^[-*]\s+', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            content = re.sub(r'^[-*]\s+', '', line)
            result.append(f'<li>{content}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    if in_list:
        result.append('</ul>')
    html = '\n'.join(result)
    
    # Paragraphs (lines that aren't already HTML tags)
    lines = html.split('\n')
    result = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not (line.startswith('<') or line.startswith('#')):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    html = '\n'.join(result)
    
    return html

def create_html_wrapper(title, authors, content, source_info=""):
    """Create a complete HTML document"""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            background-color: #fff;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 5px;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
        }}
        h4 {{
            color: #666;
        }}
        .abstract {{
            background-color: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin: 20px 0;
        }}
        .authors {{
            font-style: italic;
            color: #666;
            margin: 10px 0;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 3px solid #3498db;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        .source-info {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #ecf0f1;
            font-size: 0.9em;
            color: #666;
        }}
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    
    <div class="authors">
        {authors}
    </div>

    {content}
    
    {f'<div class="source-info"><p><strong>Source:</strong> {source_info}</p></div>' if source_info else ''}
</body>
</html>"""
    return html_template

def main():
    # Get the directory
    script_dir = Path(__file__).parent
    
    # Process aaai25_paper.md
    aaai25_md = script_dir / "aaai25_paper.md"
    if aaai25_md.exists():
        print(f"Processing {aaai25_md}...")
        with open(aaai25_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract title and authors
        title_match = re.search(r'^# (.+?)(?:\n|$)', md_content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Paper Title"
        
        authors_match = re.search(r'\*\*Authors\*\*: (.+?)(?:\n\n|\*\*|\n\*\*)', md_content, re.DOTALL)
        if authors_match:
            authors_text = authors_match.group(1).strip()
            authors_html = f"<p><strong>Authors:</strong> {authors_text}</p>"
        else:
            authors_html = "<p><strong>Authors:</strong> Not specified</p>"
        
        # Extract abstract
        abstract_match = re.search(r'## Abstract\n\n(.+?)\n\n---', md_content, re.DOTALL)
        if abstract_match:
            abstract_text = abstract_match.group(1).strip()
            abstract_html = f'<div class="abstract"><h2>Abstract</h2><p>{abstract_text}</p></div>'
            # Remove abstract from main content
            md_content = re.sub(r'## Abstract\n\n.+?\n\n---\n\n', '', md_content, flags=re.DOTALL)
        else:
            abstract_html = ""
        
        # Convert rest of markdown to HTML
        body_html = markdown_to_html(md_content)
        
        # Combine
        full_content = abstract_html + "\n<hr>\n" + body_html if abstract_html else body_html
        
        html_output = create_html_wrapper(
            title,
            authors_html,
            full_content,
            "Converted from markdown version of arXiv:2412.10703v21 (AAAI 2025)"
        )
        
        output_file = script_dir / "aaai25_paper.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Created {output_file}")
    
    # Process COCO_paper.md
    coco_md = script_dir / "COCO_paper.md"
    if coco_md.exists():
        print(f"Processing {coco_md}...")
        with open(coco_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract title and authors
        title_match = re.search(r'^# (.+?)(?:\n|$)', md_content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Paper Title"
        
        authors_match = re.search(r'\*\*Authors\*\*: (.+?)(?:\n\n|\*\*|\n\*\*)', md_content, re.DOTALL)
        if authors_match:
            authors_text = authors_match.group(1).strip()
            authors_html = f"<p><strong>Authors:</strong> {authors_text}</p>"
        else:
            authors_html = "<p><strong>Authors:</strong> Not specified</p>"
        
        # Extract abstract
        abstract_match = re.search(r'## Abstract\n\n(.+?)\n\n---', md_content, re.DOTALL)
        if abstract_match:
            abstract_text = abstract_match.group(1).strip()
            abstract_html = f'<div class="abstract"><h2>Abstract</h2><p>{abstract_text}</p></div>'
            # Remove abstract from main content
            md_content = re.sub(r'## Abstract\n\n.+?\n\n---\n\n', '', md_content, flags=re.DOTALL)
        else:
            abstract_html = ""
        
        # Convert rest of markdown to HTML
        body_html = markdown_to_html(md_content)
        
        # Combine
        full_content = abstract_html + "\n<hr>\n" + body_html if abstract_html else body_html
        
        html_output = create_html_wrapper(
            title,
            authors_html,
            full_content,
            "Converted from markdown version of arXiv:2310.18955v3 (NeurIPS 2024)"
        )
        
        output_file = script_dir / "COCO_paper.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Created {output_file}")

if __name__ == "__main__":
    main()
