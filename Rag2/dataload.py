from pathlib import Path
from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf

pdf_path = Path(__file__).parent / "data" / "課題10-12.pdf"

elements = partition_pdf(
	filename=pdf_path,
	strategy="fast",
	language="jpn",
)

print(f"解析完了：{len(elements)} 個要素、{sum(len(str(e)) for e in elements)} バイト")

from collections import Counter
types = Counter(e.category for e in elements)
print(f"要素タイプ：{dict(types)}")

print(f"全ての要素：")
for i, element in enumerate(elements, 1):
	print(f"Elements {i} ({element.category}):")
	print(element)
	print("=" * 60)
