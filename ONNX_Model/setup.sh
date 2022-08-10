#!/bin/bash
python3 convert_to_onnx.py
uvicorn app:app --reload --host 0.0.0.0 --port 8000