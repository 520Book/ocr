import ddddocr
import sys

ocr = ddddocr.DdddOcr()
print(ocr.classification(sys.argv[1]))
