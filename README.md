# mulMoQr

mulMoQr is a little python script to make personalized QR Codes that includes the MulMo_pro logo.

## Dependencies

To run the python script it is necessary to have installed [pillow](https://pypi.org/project/pillow/) and [qrcode](https://pypi.org/project/qrcode/) modules:
```
pip install pillow
pip install qrcode
```
or
```
pip install "qrcode[pil]"
```
to install qrcode with pillow as a dependency (I have not tested it though).

## Usage

To choose the data that will be encoded in QR Code simpy modify the `url` string in the `qrMaker.py` file.
To generate the QR Code run:
```
python3 qrMaker.py
```
The default string will generate a QR Code which leads to this github repository.
