#!/usr/bin/env python3
"""
Extract text from the Screenmate OneCable PDF manual
"""
import sys
import os

def extract_with_pypdf2(pdf_path):
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            return text
    except ImportError:
        return None
    except Exception as e:
        print(f"Error with PyPDF2: {e}", file=sys.stderr)
        return None

def extract_with_pdfplumber(pdf_path):
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n\n"
        return text
    except ImportError:
        return None
    except Exception as e:
        print(f"Error with pdfplumber: {e}", file=sys.stderr)
        return None

def main():
    pdf_path = "Screenmate - OneCable - Handleiding.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found", file=sys.stderr)
        sys.exit(1)
    
    # Try pdfplumber first (better text extraction)
    text = extract_with_pdfplumber(pdf_path)
    if text:
        print(text)
        return
    
    # Fallback to PyPDF2
    text = extract_with_pypdf2(pdf_path)
    if text:
        print(text)
        return
    
    print("Error: No PDF extraction library available. Install with: pip install pdfplumber", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()

