from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'error': 'fg:ansired',
    'warning': 'fg:ansiyellow',
    'success': 'fg:ansigreen',
    'info': 'fg:ansiblue',
    'debug': 'fg:violet'
})

error = "<error>[ERROR]</error>"
warning = "<warning>[WARN]</warning>"
success = "<success>[DONE]</success>"
info = "<info>[INFO]</info>"
debug = "<debug>[DEBUG]</debug>"

print_formatted_text(HTML(debug+'测试文本'), style=style)