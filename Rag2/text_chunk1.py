from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader(Path(__file__).parent / "data" / "源赖光.txt", encoding="utf-8")
docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
)

chunks = text_splitter.split_documents(docs)

print(f"文本被切分为 {len(chunks)} 个块，每个块的大小为 {text_splitter._chunk_size}，重叠为 {text_splitter._chunk_overlap}。")
print("---前五个块内容示例---")
for i, chunk in enumerate(chunks[:5]):
    print("=" * 60)
    print(f'块 {i+1} (长度：{len(chunk.page_content)}): "{chunk.page_content}"')
