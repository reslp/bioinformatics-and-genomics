import re
import os

# script to convert some mgithub flavoured markdown into something that can be rendered properly with sphinx

def process_markdown_files(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			if "NEW_" in file:
				continue
			if file.endswith('.md'):
				file_path = os.path.join(root, file)
				outfile_path = os.path.join(root, "NEW_" + file)
				print(file_path)
				print(outfile_path)
				# Read the original Markdown file content
				with open(file_path, 'r') as f:
					found = 0
					outtext = ""
					for line in f.readlines():
						if line.startswith(">[!TIP]"):
							print("Found TIP admonition in md file:", f)
							line = line.replace(">[!TIP]", "```{tip}")
							found = 1
							outtext += line
							continue
						if line.startswith(">[!NOTE]"):
							print("Found NOTE admonition in md file:", f)
							line = line.replace(">[!NOTE]", "```{note}")
							found = 1
							outtext += line
							continue
						if line.startswith(">[!IMPORTANT]"):
							print("Found IMPORTANT admonition in md file:", f)
							line = line.replace(">[!IMPORTANT]", "```{important}")
							found = 1
							outtext += line
							continue
						if line.startswith(">[!WARNING]"):
							print("Found WARNING admonition in md file:", f)
							line = line.replace(">[!WARNING]", "```{warning}")
							found = 1
							outtext += line
							continue
						if line.startswith(">[!CAUTION]"):
							print("Found CAUTION admonition in md file:", f)
							line = line.replace(">[!CAUTION]", "```{caution}")
							found = 1
							outtext += line
							continue
						if found == 1 and line.startswith(">"):
							line = line.replace(">", "")
							outtext += line
							continue
						if found == 1 and line.startswith(">") == False:
							line = "```\n\n"
							found = 0
							outtext += line
							continue
						outtext += line

				# Overwrite the file with converted content
				with open(file_path, 'w') as f:
					f.write(outtext)

if __name__ == "__main__":
# Assuming 'docs_source_path' is where your markdown files are stored
	docs_source_path = [path for path in os.listdir() if os.path.isdir(path)]
	print(docs_source_path)
	for p in docs_source_path:
		process_markdown_files(p) 
