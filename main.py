import langextract as lx
import textwrap
from collections import Counter, defaultdict

# Define comprehensive prompt and examples for extracting business entities
prompt = textwrap.dedent("""\
    Extract people, companies, and actions from the given text.

    Provide meaningful attributes for every entity to add context and depth.

    Important: Use exact text from the input for extraction_text. Do not paraphrase.
    Extract entities in order of appearance with no overlapping text spans.""")

examples = [
    lx.data.ExampleData(
        text=textwrap.dedent("""\
            The following connectors are now available to search by chat in addition to deep research.

            Plus: Box, Canva, Dropbox, HubSpot, Notion, Microsoft SharePoint, and Microsoft Teams

            Pro: Microsoft Teams and Github

            Rollout begins today, and all eligible accounts will have access in the coming days."""),
        extractions=[
            lx.data.Extraction(
                extraction_class="action",
                extraction_text="search by chat",
                attributes={"type": "functionality", "context": "connectors"}
            ),
            lx.data.Extraction(
                extraction_class="action",
                extraction_text="deep research",
                attributes={"type": "functionality", "context": "connectors"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="Box",
                attributes={"product_tier": "Plus", "type": "cloud_storage"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="Canva",
                attributes={"product_tier": "Plus", "type": "design_platform"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="Dropbox",
                attributes={"product_tier": "Plus", "type": "cloud_storage"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="HubSpot",
                attributes={"product_tier": "Plus", "type": "crm_platform"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="Notion",
                attributes={"product_tier": "Plus", "type": "productivity_platform"}
            ),
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="Github",
                attributes={"product_tier": "Pro", "type": "code_repository"}
            ),
            lx.data.Extraction(
                extraction_class="action",
                extraction_text="Rollout begins",
                attributes={"type": "deployment", "timing": "today"}
            ),
        ]
    )
]

# Process text from input.txt file
print("Processing text from input.txt...")

# Read the text from input.txt
with open("input.txt", "r") as f:
    input_text = f.read()

result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    api_key='API_KEY',
    model_id="gemini-2.5-pro",
    extraction_passes=3,      # Multiple passes for improved recall
    max_workers=20,           # Parallel processing for speed
    max_char_buffer=1000      # Smaller contexts for better accuracy
)

print(f"Extracted {len(result.extractions)} entities from {len(result.text):,} characters")

# Save and visualize the results
lx.io.save_annotated_documents([result], output_name="business_entity_extractions.jsonl", output_dir=".")

# Generate the interactive visualization
html_content = lx.visualize("business_entity_extractions.jsonl")
with open("business_entity_visualization.html", "w") as f:
    f.write(html_content)

print("Interactive visualization saved to business_entity_visualization.html")
