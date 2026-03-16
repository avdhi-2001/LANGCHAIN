# recursive character based text splitting

# \n\n paragraph

# \n line

# '_'  words

#  '' character

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# loader=PyPDFLoader('dl-curriculum.pdf')

# docs=loader.load()

split=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)

chunks=split.split_text(text)

print(len(chunks))

print(chunks)

print(type(chunks))
