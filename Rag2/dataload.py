from unstructured.partition.auto import partition

pdf_path = "../../data/C2/pdf/rag.pdf"

elements = partition(
	filename=pdf_path,
	content=type="application/pdf"
)

print(f"解析完了：{len(elements)} 個要素、{sum(len(str(e)) for e in elements)} バイト")

from collections import Counter
types = Counter(e.category for e in elements)
print(f"要素タイプ：{dict(types)}")

print(f"全ての要素：")
for i, element in enumerate(elements, 1):
	print(f"Elements {i} ({elements.category}):")
	print(element)
	print("=" * 60)
