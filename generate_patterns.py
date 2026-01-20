import sys
from io import StringIO
from main import (
    pattern_a, pattern_b, pattern_c, pattern_d, pattern_e, pattern_f,
    pattern_g, pattern_h, pattern_i, pattern_j, pattern_k, pattern_l,
    pattern_m, pattern_n, pattern_o, pattern_p, pattern_q, pattern_r
)

def capture_pattern_output(pattern_func, n=5):
    """Capture the output of a pattern function"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    pattern_func(n)
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    return output

# List of all pattern functions
patterns = [
    ('pattern_a', pattern_a),
    ('pattern_b', pattern_b),
    ('pattern_c', pattern_c),
    ('pattern_d', pattern_d),
    ('pattern_e', pattern_e),
    ('pattern_f', pattern_f),
    ('pattern_g', pattern_g),
    ('pattern_h', pattern_h),
    ('pattern_i', pattern_i),
    ('pattern_j', pattern_j),
    ('pattern_k', pattern_k),
    ('pattern_l', pattern_l),
    ('pattern_m', pattern_m),
    ('pattern_n', pattern_n),
    ('pattern_o', pattern_o),
    ('pattern_p', pattern_p),
    ('pattern_q', pattern_q),
    ('pattern_r', pattern_r),
]

# Generate markdown content
markdown_content = "# Pattern Printing Outputs\n\n"
markdown_content += "This document contains the outputs of all pattern printing functions with n=5.\n\n"
markdown_content += "---\n\n"

for pattern_name, pattern_func in patterns:
    output = capture_pattern_output(pattern_func, 5)
    
    markdown_content += f"## {pattern_name}\n\n"
    markdown_content += "```\n"
    markdown_content += output
    markdown_content += "```\n\n"

# Write to markdown file
with open('PATTERNS.md', 'w') as f:
    f.write(markdown_content)

print("✅ Successfully generated PATTERNS.md with all pattern outputs!")
