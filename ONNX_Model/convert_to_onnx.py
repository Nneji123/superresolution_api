# simple script to convert rdn model to onnx
import os 
from ISR.models import RDN
rdn = RDN(weights='noise-cancel') 
rdn.model.save("my_model")
os.system("python -m tf2onnx.convert --saved-model my_model --output model.onnx --opset 13")